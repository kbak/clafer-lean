module

import DPGraph
public meta import Lean.Elab.Command

/-! Public foundation smoke test: no upper layer or examples are imported. -/
#check DPGraph
#check DPGraph.Signature
#check DPGraph.Formula
#check DPGraph.Formula.translate
#check DPGraph.Formula.translate_id
#check DPGraph.Formula.translate_comp
#check DPGraph.Hom
#check DPGraph.Hom.ext
#check DPGraph.Hom.ext_of_obj_map
#check DPGraph.Hom.comp_preserves
#check DPGraph.Hom.id_comp
#check DPGraph.Hom.comp_id
#check DPGraph.Hom.comp_assoc
#check DPGraph.category
#check DPGraph.Interpretation
#check DPGraph.Interpretation.Satisfies
#check DPGraph.Interpretation.satisfies_translate
#check DPGraph.Interpretation.IsModel
#check DPGraph.Interpretation.isModel_reduct
#check DPGraph.Interpretation.Model
#check DPGraph.Interpretation.reduct
#check DPGraph.Interpretation.reduct_id
#check DPGraph.Interpretation.reduct_comp

example (σ : DPGraph.Signature) : CategoryTheory.Category (DPGraph σ) := inferInstance

/-! Public pushout interfaces retain the fixed carrier universes and independent
signature universes. These examples also fix the explicit argument order. -/
#check DPGraph.Pushout.CarrierCocone
#check DPGraph.Pushout.obj
#check DPGraph.Pushout.inl
#check DPGraph.Pushout.inr
#check DPGraph.Pushout.cocone
#check DPGraph.Pushout.CompatibleModels

noncomputable section
open CategoryTheory CategoryTheory.Limits
universe s va ua v u
variable {σ : DPGraph.Signature.{s, va, ua}}
variable {S T U : DPGraph.{s, va, ua, v, u} σ}
variable (F : DPGraph.Hom S T) (J : DPGraph.Hom S U)
variable (c : DPGraph.Pushout.CarrierCocone F J) (hc : IsColimit c)
variable {Ω : Quiv.{v, u}} (I : DPGraph.Interpretation σ Ω)

example : IsColimit (DPGraph.Pushout.cocone F J c) :=
  DPGraph.Pushout.isColimit F J c hc

example : I.Model (DPGraph.Pushout.obj F J c) ≃ DPGraph.Pushout.CompatibleModels I F J :=
  DPGraph.Pushout.modelEquiv F J c I hc

example (m : I.Model (DPGraph.Pushout.obj F J c)) :
    (DPGraph.Pushout.modelEquiv F J c I hc m).val.1 =
      I.reduct (DPGraph.Pushout.inl F J c) m :=
  DPGraph.Pushout.modelEquiv_fst F J c I hc m

example (m : I.Model (DPGraph.Pushout.obj F J c)) :
    (DPGraph.Pushout.modelEquiv F J c I hc m).val.2 =
      I.reduct (DPGraph.Pushout.inr F J c) m :=
  DPGraph.Pushout.modelEquiv_snd F J c I hc m
end

open Lean in
run_cmd do
  let env ← getEnv
  for name in env.header.moduleNames do
    if (`FormalCD).isPrefixOf name || (`Clafer).isPrefixOf name ||
        (`DPGraph.Examples).isPrefixOf name || (`DPGraph.SemanticsExamples).isPrefixOf name then
      throwError "independent DPGraph entrypoint imported {name}"
