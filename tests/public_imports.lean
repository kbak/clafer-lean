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

open Lean in
run_cmd do
  let env ← getEnv
  for name in env.header.moduleNames do
    if (`FormalCD).isPrefixOf name || (`Clafer).isPrefixOf name ||
        (`DPGraph.Examples).isPrefixOf name || (`DPGraph.SemanticsExamples).isPrefixOf name ||
        (`DPGraph.Span.Examples).isPrefixOf name ||
        (`DPGraph.Predicates.Examples).isPrefixOf name then
      throwError "independent DPGraph entrypoint imported {name}"

-- Independent public use with three distinct endpoint/link universe levels.
universe u v z w w'

example {A : Type u} {B : Type v} (q : DPGraph.Span.{u, v, w} A B) :
    DPGraph.Span.Iso q.toFamily.toSpan q := q.familySpanIso

example {A : Type u} {B : Type v} (f : DPGraph.IndexedFamily.{u, v, w} A B) :
    DPGraph.IndexedFamily.Equivalence f.toSpan.toFamily f := f.spanFamilyEquivalence

example {A : Type u} {B : Type v} {C : Type z}
    (q : DPGraph.Span.{u, v, w} A B) (r : DPGraph.Span.{v, z, w'} B C) :
    (q.comp r).red = DPGraph.relationComp q.red r.red := q.red_comp r

example {A : Type u} {B : Type v} (q : DPGraph.Span.{u, v, w} A B) :
    q.JointlyInjective ↔ Nonempty (DPGraph.Span.Iso q (DPGraph.Span.ofRelation q.red)) :=
  q.jointlyInjective_iff_iso_relation

example {A : Type u} {B : Type v} (q : DPGraph.Span.{u, v, w} A B) :
    DPGraph.Span.Iso (q.comp (DPGraph.Span.identity B)) q := q.rightUnit

example {A : Type u} {B : Type v} (q : DPGraph.Span.{u, v, w} A B) :
    q.inverse.inverse = q := q.inverse_inverse

#check DPGraph.Span.associator
#check DPGraph.IndexedFamily.compSpanIso
#check DPGraph.Span.compFamilyEquivalence
#check DPGraph.Span.compToRelation_surjective
#check DPGraph.Span.comp_iso_relation_iff
#check DPGraph.Span.relations_comp_jointlyInjective_iff
#check DPGraph.Span.relations_comp_injective_of_first_singleValued
#check DPGraph.Span.relations_comp_injective_of_converse_second_singleValued

#check DPGraph.Predicates.signature
#check DPGraph.Predicates.interpretation
#check DPGraph.Predicates.Inverse
#check DPGraph.Predicates.Commutation
#check DPGraph.Predicates.Key
#check DPGraph.Predicates.Cover
#check DPGraph.Predicates.Disjoint
#check DPGraph.Predicates.Inclusion
#check DPGraph.Predicates.TargetMultiplicity
#check DPGraph.Predicates.SourceMultiplicity
#check DPGraph.Predicates.targetMultiplicity_distinct
#check DPGraph.Predicates.sourceMultiplicity_distinct

example (U : Type u) : CategoryTheory.Quiv.{max u w + 1, u} :=
  DPGraph.Predicates.semanticGraph.{u,w} U

example {A : Type u} {B : Type v} (q : DPGraph.Span.{u,v,w} A B) :
    DPGraph.Predicates.SingleValued q ↔ ∀ a, Subsingleton (q.toFamily.Index a) :=
  DPGraph.Predicates.singleValued_fibers q

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
universe ps pva pua pv pu
variable {σ : DPGraph.Signature.{ps, pva, pua}}
variable {S T U : DPGraph.{ps, pva, pua, pv, pu} σ}
variable (F : DPGraph.Hom S T) (J : DPGraph.Hom S U)
variable (c : DPGraph.Pushout.CarrierCocone F J) (hc : IsColimit c)
variable {Ω : Quiv.{pv, pu}} (I : DPGraph.Interpretation σ Ω)

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
