"""Pinned static Alloy process with explicit profile and bounded resources."""
import hashlib
import os
from pathlib import Path
import platform
import resource
import shutil
import subprocess
import tarfile
import zipfile

from protocol import Rejection, digest, encoded, loads, unsupported
from runtime import download

HERE = Path(__file__).resolve().parent
JAR_SHA = "6b8c1cb5bc93bedfc7c61435c4e1ab6e688a242dc702a394628d9a9801edb78d"
JAR_URL = "https://github.com/AlloyTools/org.alloytools.alloy/releases/download/v6.2.0/org.alloytools.alloy.dist.jar"
JDK_SHA = "3808d1d15e3ec6bd5b84057fb5d84c33d8a1536a258146bcea2e603fc726e08e"
JDK_URL = "https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.20.1%2B1/OpenJDK17U-jdk_x64_linux_hotspot_17.0.20.1_1.tar.gz"


def java_env():
    return {k: v for k, v in os.environ.items() if k not in ("JAVA_TOOL_OPTIONS", "JDK_JAVA_OPTIONS", "_JAVA_OPTIONS", "CLASSPATH")}


def prepare():
    cache = Path(os.environ.get("CLAFER_ALLOY_CACHE", Path.home() / ".cache/clafer-comparison")).resolve()
    if cache.is_relative_to(HERE.parents[1]):
        unsupported("runtime_in_repository")
    cache.mkdir(parents=True, exist_ok=True)
    jar = Path(os.environ.get("CLAFER_ALLOY_JAR", cache / "alloy/alloy-6.2.0.jar")).resolve()
    if "CLAFER_ALLOY_JAR" not in os.environ:
        jar.parent.mkdir(parents=True, exist_ok=True)
        download(JAR_URL, jar, JAR_SHA)
    if hashlib.sha256(jar.read_bytes()).hexdigest() != JAR_SHA:
        unsupported("alloy_jar_identity")
    with zipfile.ZipFile(jar) as z:
        manifest = z.read("META-INF/MANIFEST.MF").decode().replace("\r\n ", "")
    for line in ("Bundle-Version: 6.2.0.202501090817", "Git-SHA: 794226dd07b536fe35c5ca44b529417183cd629b"):
        if line not in manifest.splitlines():
            unsupported("alloy_manifest_identity")
    java_home = os.environ.get("CLAFER_JAVA_HOME") or os.environ.get("JAVA_HOME")
    java = Path(java_home) / "bin/java" if java_home else Path(shutil.which("java") or "/missing/java")
    version = subprocess.run([str(java), "-version"], capture_output=True, env=java_env(), timeout=20)
    if b'version "17.' not in version.stderr:
        if java_home or (platform.system(), platform.machine()) != ("Linux", "x86_64"):
            unsupported("java_profile", "Java 17 JDK required")
        archive = cache / "jdk.tar.gz"
        download(JDK_URL, archive, JDK_SHA)
        destination = cache / "jdk"
        java = destination / "jdk-17.0.20.1+1/bin/java"
        if not java.exists():
            with tarfile.open(archive) as packed:
                packed.extractall(destination, filter="data")
    javac = java.resolve().with_name("javac")
    if not javac.is_file():
        unsupported("missing_javac", "Java 17 JDK required")
    key = hashlib.sha256((HERE / "AlloyBridge.java").read_bytes() + JAR_SHA.encode()).hexdigest()
    classes = cache / "bridge" / key
    classes.mkdir(parents=True, exist_ok=True)
    # Do not trust stale writable class files: compile from current reviewed source.
    subprocess.run([str(javac), "--release", "17", "-cp", str(jar), "-d", str(classes), str(HERE / "AlloyBridge.java")],
                   check=True, capture_output=True, env=java_env(), timeout=60)
    version = subprocess.run([str(java), "-version"], capture_output=True, check=True, env=java_env(), timeout=20)
    return dict(java=java.resolve(), jar=jar, classes=classes,
                identity=dict(jar=digest(jar.read_bytes()), bridge_source=digest((HERE / "AlloyBridge.java").read_bytes()),
                              java_binary=digest(java.read_bytes()), java_version=version.stderr.decode(),
                              bridge_class=digest((classes / "AlloyBridge.class").read_bytes())))


def solve(runtime, directory, request, timeout=30, heap_mb=512):
    if type(timeout) is not int or timeout <= 0 or type(heap_mb) is not int or heap_mb < 64:
        unsupported("resource_profile")
    directory = Path(directory)
    (directory / "request.json").write_bytes(encoded(request))
    options = [f"-Xmx{heap_mb}m", "-Xss1m", "-XX:ActiveProcessorCount=1", "-XX:+UseSerialGC",
               "-XX:ReservedCodeCacheSize=64m", "-XX:CompressedClassSpaceSize=64m"]
    address_mb = heap_mb + 2048
    def limits():
        resource.setrlimit(resource.RLIMIT_AS, (address_mb * 1024**2,) * 2)
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    args = [str(runtime["java"]), *options, "-cp", os.pathsep.join(map(str, (runtime["classes"], runtime["jar"]))), "AlloyBridge"]
    (directory / "profile.json").write_bytes(encoded(dict(runtime["identity"], jvm_options=options,
        wall_seconds=timeout, heap_mb=heap_mb, address_space_mb=address_mb, workers=1)))
    def interrupted(status,detail):
        checkpoint=directory/"execution.json"
        try:observed=loads(checkpoint.read_bytes()) if checkpoint.exists() else {}
        except Rejection:observed={}
        if type(observed) is not dict or observed.get("schema") not in (None,"clafer-alloy-bridge/1"):
            observed={}
        # A process failure before execute_command is not a solver observation.
        outcome=observed.get("outcome")
        if outcome is None and observed.get("stage")=="solver":outcome=status
        return dict(observed,outcome=outcome,status=status,
                    stage=observed.get("stage","jvm_start"),detail=detail)
    with (directory / "stdout.log").open("wb") as out, (directory / "stderr.log").open("wb") as err:
        try:
            process = subprocess.run(args, cwd=directory, stdout=out, stderr=err, timeout=timeout,
                                     env=java_env(), preexec_fn=limits)
        except subprocess.TimeoutExpired:
            return interrupted("timeout","solver wall-clock limit")
    if process.returncode:
        log = (directory / "stderr.log").read_bytes() + (directory / "stdout.log").read_bytes()
        memory = b"memory" in log.lower() or b"OutOfMemory" in log
        return interrupted("resource_limit" if memory else "error", f"JVM exit {process.returncode}")
    if not (directory / "solver.json").exists():
        return interrupted("error","missing solver result")
    try:result=loads((directory / "solver.json").read_bytes())
    except Rejection as error:return interrupted("error","malformed solver result: "+str(error))
    if (type(result) is not dict or result.get("schema")!="clafer-alloy-bridge/1" or
            result.get("status") not in ("ok","unsupported","error","resource_limit") or
            result.get("outcome") not in (None,"sat","unsat")):
        return interrupted("error","invalid solver result schema")
    if result.get("status")=="unsupported":result["unsupported"]=True
    return result
