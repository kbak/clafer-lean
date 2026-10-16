module

public import DPGraph.Category

/-!
# Abstract interpretation and contravariant model restriction

SoSyM B.5, Theorem 3, abstracted over a semantic graph and predicate meanings.
For each symbol, an interpretation selects the satisfying arity diagrams in
that graph. Formula satisfaction and the model condition are derived from this
selection. Restriction uses only declaration preservation and associativity of
graph-map composition; no closure or invariance axiom on meanings is required.

Semantic vertex/arrow universes are independent of signature and carrier
universes. No graph of all types, concrete span interpretation, or resizing
axiom is supplied here.
-/

@[expose] public section

universe s va ua v₁ u₁ v₂ u₂ v₃ u₃ vm um

namespace DPGraph

open CategoryTheory

/-- Meaning of each predicate on diagrams of its arity in the chosen semantic
graph. This data does not assume the model restriction theorem. -/
structure Interpretation (σ : Signature.{s, va, ua}) (Ω : Quiv.{vm, um}) where
  meaning : (p : σ.Symbol) → Set (σ.arity p ⥤q Ω)

namespace Interpretation

variable {σ : Signature.{s, va, ua}} {Ω : Quiv.{vm, um}}
variable (I : Interpretation σ Ω)
variable {G : Quiv.{v₁, u₁}} {H : Quiv.{v₂, u₂}}
variable {S : DPGraph.{s, va, ua, v₁, u₁} σ}
variable {T : DPGraph.{s, va, ua, v₂, u₂} σ}
variable {U : DPGraph.{s, va, ua, v₃, u₃} σ}

/-- Interpret a formula by composing its binding with the candidate model. -/
def Satisfies (m : G ⥤q Ω) (φ : Formula σ G) : Prop :=
  φ.binding.comp m ∈ I.meaning φ.symbol

/-- Satisfaction commutes with translation along any graph map. This is an
equivalence about one formula, not reflection of whole-model satisfaction. -/
theorem satisfies_translate (φ : Formula σ G) (F : G ⥤q H) (m : H ⥤q Ω) :
    I.Satisfies m (φ.translate F) ↔ I.Satisfies (F.comp m) φ := by
  unfold Satisfies Formula.translate
  rw [Prefunctor.comp_assoc]

/-- A model satisfies every declared formula (B.5). -/
def IsModel (S : DPGraph.{s, va, ua, v₁, u₁} σ) (m : S.carrier ⥤q Ω) : Prop :=
  ∀ φ ∈ S.declarations, I.Satisfies m φ

/-- B.5 Theorem 3 in its generic form: a target model restricts to a source
model along a declaration-preserving DP morphism. The only hypotheses are the
fixed interpretation, the DP morphism and the target's model proof. -/
theorem isModel_reduct (F : Hom S T) (m : T.carrier ⥤q Ω) (hm : I.IsModel T m) :
    I.IsModel S (F.toPrefunctor.comp m) := by
  intro φ hφ
  exact (I.satisfies_translate φ F.toPrefunctor m).mp (hm _ (F.preserves hφ))

/-- Models retain the interpreting graph map as well as its satisfaction proof. -/
def Model (S : DPGraph.{s, va, ua, v₁, u₁} σ) :=
  {m : S.carrier ⥤q Ω // I.IsModel S m}

/-- Contravariant restriction by precomposition. -/
def reduct (F : Hom S T) (m : I.Model T) : I.Model S :=
  ⟨F.toPrefunctor.comp m.val, I.isModel_reduct F m.val m.property⟩

@[simp] theorem reduct_val (F : Hom S T) (m : I.Model T) :
    (I.reduct F m).val = F.toPrefunctor.comp m.val := rfl

@[simp] theorem reduct_id (m : I.Model S) : I.reduct (Hom.id S) m = m :=
  Subtype.ext (Prefunctor.id_comp m.val)

/-- Restricting along a composite first restricts along its second map. -/
theorem reduct_comp (F : Hom S T) (J : Hom T U) (m : I.Model U) :
    I.reduct (F.comp J) m = I.reduct F (I.reduct J m) :=
  Subtype.ext (Prefunctor.comp_assoc F.toPrefunctor J.toPrefunctor m.val)

end Interpretation
end DPGraph
