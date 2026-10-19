"""Bounded request stream to the existing Lean importer/checker entrypoint."""
import atexit
import os
from pathlib import Path
import select
import subprocess
import tempfile
import time

from protocol import Rejection, digest, encoded, loads

ROOT=Path(__file__).resolve().parents[2]


class Checker:
    def __init__(self, source):
        self.source=source
        self.sequence=0
        # Lake validates source/options/transitive traces before any verdict;
        # matching .lean bytes alone would not exclude stale imported .oleans.
        subprocess.run(["lake","build","+Clafer.Verification.ImportMain"],cwd=ROOT,
                       capture_output=True,check=True,timeout=900)
        self.errors=tempfile.TemporaryFile()
        self.process=subprocess.Popen(["lake","env","lean","--run","Clafer/Verification/ImportMain.lean","--stream"],
            cwd=ROOT,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=self.errors,bufsize=0,start_new_session=True)
        try:
            header=self.receive()
            expected=(ROOT/"lean-toolchain").read_text().strip().removeprefix("leanprover/lean4:v")
            if set(header)!={"schema","lean","limit","executable"} or header["schema"]!="clafer-checker-stream/1" or header["lean"]!=expected or header["limit"]!=1000000:
                raise RuntimeError("checker stream/toolchain identity mismatch")
            self.identity=dict(schema=header["schema"],lean=header["lean"],max_requests=header["limit"],
                               executable=digest(Path(header["executable"]).read_bytes()),request_timeout_seconds=120,
                               build=["lake","build","+Clafer.Verification.ImportMain"],
                               importer_olean=digest((ROOT/".lake/build/lib/lean/Clafer/Verification/ImportMain.olean").read_bytes()))
        except BaseException:
            self.close();raise

    def receive(self):
        deadline=time.monotonic()+120;data=b""
        while b"\n" not in data:
            remaining=deadline-time.monotonic()
            if remaining<=0 or not select.select([self.process.stdout],[],[],remaining)[0]:
                raise TimeoutError("Lean checker request timed out")
            part=os.read(self.process.stdout.fileno(),65536)
            if not part:
                self.errors.seek(0)
                raise RuntimeError("checker stream closed: "+self.errors.read().decode(errors="replace")[-4000:])
            data+=part
        if data.count(b"\n")!=1 or not data.endswith(b"\n"):
            raise RuntimeError("multiple/malformed checker response frames")
        try:result=loads(data)
        except Rejection as error:raise RuntimeError("malformed checker response: "+str(error)) from error
        if type(result) is not dict:raise RuntimeError("checker response is not an object")
        return result

    def request(self, core, candidate):
        try:
            if self.sequence>=1000000:raise RuntimeError("checker request limit exhausted")
            if select.select([self.process.stdout],[],[],0)[0]:raise RuntimeError("unsolicited checker response")
            pending=memoryview(encoded(dict(core,candidate=candidate)))
            deadline=time.monotonic()+120
            os.set_blocking(self.process.stdin.fileno(),False)
            while pending:
                remaining=deadline-time.monotonic()
                if remaining<=0 or not select.select([],[self.process.stdin],[],remaining)[1]:
                    raise TimeoutError("Lean checker input timed out")
                sent=os.write(self.process.stdin.fileno(),pending)
                if sent<=0:raise RuntimeError("checker input closed")
                pending=pending[sent:]
            result=self.receive()
            if set(result)!={"sequence","verdict"} or result["sequence"]!=self.sequence:
                raise RuntimeError("checker response sequence mismatch")
            self.sequence+=1
            return result["verdict"]
        except BaseException:
            self.close();raise

    def close(self):
        if self.process.poll() is None:
            import signal
            os.killpg(self.process.pid,signal.SIGTERM)
            try:self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(self.process.pid,signal.SIGKILL);self.process.wait()
        self.process.stdin.close();self.process.stdout.close();self.errors.close()


worker=None


def stop():
    global worker
    if worker is not None:worker.close();worker=None


atexit.register(stop)


def execute(core,candidate,source):
    global worker
    if worker is not None and (worker.source!=source or worker.process.poll() is not None):stop()
    if worker is None:worker=Checker(source)
    try:return worker.request(core,candidate),worker.identity
    except BaseException:stop();raise
