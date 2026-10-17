module

import FormalCD
public meta import Lean.Elab.Command

/-! FormalCD is reusable without Clafer or acceptance example imports.
The existing public_imports test independently guards the DPGraph root. -/

#check FormalCD.Registry
#check FormalCD.Raw
#check FormalCD.Raw.WellFormed
#check FormalCD.CD
#check FormalCD.Hom.ext
#check FormalCD.Hom.ext_of_map
#check FormalCD.Hom.toDPHom_id
#check FormalCD.Hom.toDPHom_comp

open Lean in
run_cmd do
  let env ← getEnv
  for name in env.header.moduleNames do
    if (`Clafer).isPrefixOf name || (`FormalCD.Examples).isPrefixOf name ||
        (`FormalCD.SemanticsExamples).isPrefixOf name then
      throwError "independent FormalCD entrypoint imported {name}"

universe p v₁ u₁ v₂ u₂ v₃ u₃ vm um
open FormalCD CategoryTheory
variable {R : Registry.{p}} {S : CD.{p,v₁,u₁} R} {T : CD.{p,v₂,u₂} R}
variable {U : CD.{p,v₃,u₃} R} (F : Hom S T) (J : Hom T U)
variable {Ω : Quiv.{vm,um}} (I : DPGraph.Interpretation DPGraph.Predicates.signature Ω)

example : (Hom.id S).comp F = F := Hom.id_comp F
example : F.comp (Hom.id T) = F := Hom.comp_id F
example (m : I.Model T.toDPGraph) : I.Model S.toDPGraph := F.reduct I m
example (m : I.Model U.toDPGraph) :
    (F.comp J).reduct I m = F.reduct I (J.reduct I m) := Hom.reduct_comp I F J m
