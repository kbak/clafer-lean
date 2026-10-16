module

import all ClaferLean
import all ClaferLean.Basic
import all ClaferLean.DPGraph
import all ClaferLean.DPGraph.Signature
import all ClaferLean.DPGraph.Formula
import all ClaferLean.DPGraph.Basic
import all ClaferLean.DPGraph.Morphism
import all ClaferLean.DPGraph.Examples
import Lean.Util.CollectAxioms

/-!
Audit every declaration originating in the project, including generated/private
ones. Reject new axioms, unsafe/partial declarations and transitive dependencies
outside Lean's standard logical axioms. The shared check retains this output.
-/

open Lean in
run_cmd do
  let env ← getEnv
  let moduleNames := env.header.moduleNames
  for mod in env.header.modules do
    if (`ClaferLean).isPrefixOf mod.module && !mod.importAll then
      throwError "audit must import all of project module {mod.module}"
  let standard := #[``propext, ``Classical.choice, ``Quot.sound]
  let mut count := 0
  let mut used : Array Name := #[]
  for (name, info) in env.constants.toList do
    let some idx := env.getModuleIdxFor? name | continue
    unless (`ClaferLean).isPrefixOf moduleNames[idx.toNat]! do continue
    count := count + 1
    if info.isUnsafe || info.isPartial then
      throwError "unsafe or partial project declaration: {name}"
    if let .axiomInfo _ := info then
      throwError "new project axiom: {name}"
    let axioms ← collectAxioms name
    for ax in axioms do
      unless standard.contains ax do
        throwError "unapproved axiom {ax} in {name}"
      unless used.contains ax do used := used.push ax
    if info matches .thmInfo _ then
      logInfo m!"{name}: {axioms}"
  if count == 0 then throwError "audit found no project declarations"
  logInfo m!"Audited {count} project declarations. Standard axioms used: {used}. New assumptions: none."
