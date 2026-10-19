module

public import Clafer.Verification.ImportProofs
public meta import Clafer.Verification.ImportProofs

/-! Internal adapter for canonical JSON emitted by capture.py after strict
external decoding (including duplicate-key rejection). Lean.Json.parse alone
does not enforce that lexical boundary. Parsing and runtime execution are outside
the kernel proof boundary; decoded records pass `Import.admit` before a verdict. -/

@[expose] public section
namespace Clafer.Verification.Import
open Lean

def strictKeys (j : Json) (keys : List String) : Except String Unit := do
  let obj ← j.getObj?
  let actual := obj.toList.map Prod.fst
  if actual.length = keys.length ∧ actual.all (· ∈ keys) then pure ()
  else .error "unexpected_fields"

def response (status : String) (code : String := "") : Json :=
  Json.mkObj [("status", toJson status), ("code", toJson code)]

def execute (json : Json) : Except String Json := do
  strictKeys json ["schema", "declarations", "candidate"]
  let schema ← json.getObjValAs? String "schema"
  if schema != "clafer-import/1" then return response "unsupported" "version"
  let declarations ← json.getObjValAs? (Array Json) "declarations"
  for row in declarations do
    strictKeys row ["uid", "name", "parent", "abstract", "super", "mode", "target",
      "card", "group", "parentRank", "superRank", "unused"]
  let r : Input := ⟨← json.getObjValAs? (List Row) "declarations"⟩
  match admit r with
  | .error .unsupportedOrInvalidCertificate => return response "unsupported" "fragment_or_certificate"
  | .error e => return response "malformed" (reprStr e)
  | .ok _ =>
    let candidate ← json.getObjVal? "candidate"
    if let .null := candidate then return response "admitted"
    strictKeys candidate ["objects", "root", "members", "containment", "references"]
    let c : UidCandidate ← fromJson? candidate
    let c ← c.translate r
    match verify r.normalize c with
    | .malformed error => return response "malformed" (reprStr error)
    | .satisfies => return response "satisfies"
    | .violates => return response "violates"

end Clafer.Verification.Import

public def main : IO Unit := do
  let stdin ← IO.getStdin
  let input ← stdin.readToEnd
  let output := do
    let json ← Lean.Json.parse input
    Clafer.Verification.Import.execute json
  let result := match output with
    | .ok value => value
    | .error error => Clafer.Verification.Import.response "malformed" error
  (← IO.getStdout).putStrLn result.compress
