module

public import Clafer.Constraints.Typing
public import FormalCD.Telematics.VC

/-!
# Integer operands from navigation

SoSyM D.3–D.4 and Appendix F, p.34. This supplies the partial meaning of
`Expr.integerOf`, for the relational set result of navigation. It does not
interpret other expressions or use the special Figure 21 VC predicate.
The realization embeds all mathematical integers; no bit width is imposed.
-/

@[expose] public section
universe u w
namespace Clafer.Constraints
open CategoryTheory DPGraph.Predicates

abbrev IntegerRealization := FormalCD.Telematics.IntegerRealization

namespace IntegerRealization
variable {U : Type u} (R : IntegerRealization U)

/-- A successful result is exactly one realized integer object. -/
def Extracts (values : Set U) (n : Int) : Prop := values = {R.encode n}

/-- Object uniqueness and domain membership are separate runtime hypotheses. -/
def WellDefined (values : Set U) : Prop :=
  ∃ x, values = {x} ∧ x ∈ R.domain

theorem encode_decode {x : U} (h : x ∈ R.domain) : R.encode (R.decode x) = x := by
  obtain ⟨n, rfl⟩ := h
  rw [R.decode_encode]

theorem extracts_unique {values : Set U} {m n : Int}
    (hm : R.Extracts values m) (hn : R.Extracts values n) : m = n := by
  apply R.encode.injective
  exact Set.singleton_injective (hm.symm.trans hn)

theorem wellDefined_iff (values : Set U) :
    R.WellDefined values ↔ ∃ n, R.Extracts values n := by
  constructor
  · rintro ⟨x, hx, hd⟩
    exact ⟨R.decode x, hx.trans (congrArg (fun z : U => ({z} : Set U)) (R.encode_decode hd).symm)⟩
  · rintro ⟨n, hn⟩
    exact ⟨R.encode n, hn, ⟨n, rfl⟩⟩

/-- The only chosen witness is proved unique by `extracts_unique`.
Invalid collections return none; decode outside the integer domain is never used. -/
noncomputable def extract (values : Set U) : Option Int := by
  classical
  exact if h : ∃ n, R.Extracts values n then some (Classical.choose h) else none

theorem extract_eq_some_iff (values : Set U) (n : Int) :
    R.extract values = some n ↔ R.Extracts values n := by
  classical
  unfold extract
  split
  · rename_i h
    constructor
    · intro he
      cases Option.some.inj he
      exact Classical.choose_spec h
    · intro hn
      exact congrArg some (R.extracts_unique (Classical.choose_spec h) hn)
  · rename_i h
    constructor
    · intro he; cases he
    · intro hn; exact (h ⟨n, hn⟩).elim

theorem extract_none_iff (values : Set U) :
    R.extract values = none ↔ ¬ R.WellDefined values := by
  classical
  rw [R.wellDefined_iff]
  unfold extract
  split <;> simp_all

@[simp] theorem extract_encoded (n : Int) : R.extract {R.encode n} = some n :=
  (R.extract_eq_some_iff _ _).mpr rfl

@[simp] theorem extract_empty : R.extract ∅ = none := by
  apply (R.extract_none_iff _).mpr
  rintro ⟨x, hx, _⟩
  have : x ∈ (∅ : Set U) := hx.symm ▸ Set.mem_singleton x
  exact this

theorem extract_multiple {values : Set U} {x y : U}
    (hx : x ∈ values) (hy : y ∈ values) (hne : x ≠ y) : R.extract values = none := by
  apply (R.extract_none_iff _).mpr
  rintro ⟨z, rfl, _⟩
  exact hne ((Set.mem_singleton_iff.mp hx).trans (Set.mem_singleton_iff.mp hy).symm)

theorem extract_wrong_domain {x : U} (hx : x ∉ R.domain) : R.extract {x} = none := by
  apply (R.extract_none_iff _).mpr
  rintro ⟨y, he, hy⟩
  exact hx ((Set.singleton_injective he).symm ▸ hy)

/-- The domain is in correspondence with Int, not with a finite candidate list. -/
def objectEquiv : R.domain ≃ Int where
  toFun x := R.decode x.val
  invFun n := ⟨R.encode n, ⟨n, rfl⟩⟩
  left_inv x := Subtype.ext (R.encode_decode x.property)
  right_inv := R.decode_encode

end IntegerRealization

/-- A semantic support binding preserves resolved identities and actual inheritance
inclusions. Only vertices explicitly marked integer receive this realization. -/
structure IntegerBinding (s : Support) (U : Type u) where
  realization : IntegerRealization U
  model : s.graph ⥤q semanticGraph.{u,w} U
  same_id : ∀ x y, s.classId x = s.classId y → model.obj x = model.obj y
  inclusion : ∀ e, (s.mapRef e).kind = .inclusion → Inclusion (model.map (s.arrow e))
  integer_domain : ∀ x, s.integer x = true → model.obj x = realization.domain

/-- Widening changes class membership evidence and preserves ambient objects. -/
theorem IntegerBinding.widen_subset {s U} (b : IntegerBinding.{u,w} s U)
    {x y} (h : Widen s x y) : Set.Subset (b.model.obj x) (b.model.obj y) := by
  induction h with
  | same he => exact (b.same_id _ _ he) ▸ Set.Subset.refl _
  | inclusion e he => exact inclusion_subset (b.inclusion e he)
  | trans _ _ h₁ h₂ => exact h₁.trans h₂

/-- A typed integer collection supplies the domain hypothesis, not uniqueness. -/
theorem IntegerBinding.singleton_defined {s U} (b : IntegerBinding.{u,w} s U)
    {v} (primitive : s.integer v = true) {x : U} (hx : (b.model.obj v : Set U) x) :
    b.realization.extract {x} = some (b.realization.decode x) := by
  apply (b.realization.extract_eq_some_iff _ _).mpr
  exact congrArg (fun z : U => ({z} : Set U)) (b.realization.encode_decode ((b.integer_domain v primitive) ▸ hx)).symm

/-- Relational image of ambient objects, retaining witnesses of traversed links.
Duplicate links to one object do not become distinct elements of a set. -/
def navigationImage {U : Type u} {A B : Set U}
    (q : DPGraph.Span.{u,u,max u w} A B) (values : Set U) : Set U :=
  {y | ∃ l, (q.source l).val ∈ values ∧ (q.target l).val = y}

@[simp] theorem navigationImage_empty {U : Type u} {A B : Set U}
    (q : DPGraph.Span.{u,u,max u w} A B) : navigationImage q ∅ = ∅ := by
  ext y
  simp [navigationImage]

theorem navigationImage_subset {U : Type u} {A B : Set U}
    (q : DPGraph.Span.{u,u,max u w} A B) (values : Set U) :
    navigationImage q values ⊆ B := by
  rintro y ⟨l, _, rfl⟩
  exact (q.target l).property

theorem navigationImage_singleton {U : Type u} {A B : Set U}
    (q : DPGraph.Span.{u,u,max u w} A B) (hs : SingleValued q) (l : q.Link) :
    navigationImage q {(q.source l).val} = {(q.target l).val} := by
  ext y
  constructor
  · rintro ⟨k, hk, rfl⟩
    have he : q.source k = q.source l := Subtype.ext (Set.mem_singleton_iff.mp hk)
    rw [hs he]
    exact Set.mem_singleton _
  · intro hy
    exact ⟨l, Set.mem_singleton _, (Set.mem_singleton_iff.mp hy).symm⟩

/-- 1..1 link multiplicity implies singleton object image, rather than assuming it. -/
theorem navigationImage_one {U : Type u} {A B : Set U}
    (q : DPGraph.Span.{u,u,max u w} A B)
    (hq : TargetMultiplicity Clafer.one q) (a : A) :
    ∃ b : B, navigationImage q {a.val} = {b.val} := by
  obtain ⟨ht, hs⟩ := FormalCD.Telematics.one_one_total_single q hq
  obtain ⟨l, hl⟩ := ht a
  exact ⟨q.target l, hl ▸ navigationImage_singleton q hs l⟩

/-- The ordinary functional reference discipline supplies the required 1..1. -/
theorem function_one {A B : Type u} (f : A → B) :
    TargetMultiplicity Clafer.one (DPGraph.Span.ofFunction f) := by
  change TargetMultiplicity ⟨1, .finite 1⟩ (DPGraph.Span.ofFunction f)
  intro a
  refine ⟨⟨⟨fun _ => ⟨a, rfl⟩, fun _ _ _ => Subsingleton.elim _ _⟩⟩,
    ⟨⟨fun _ => 0, ?_⟩⟩⟩
  intro x y _
  exact Subtype.ext (x.property.trans y.property.symm)

theorem navigationImage_function {U : Type u} {A B : Set U} (f : A → B) (a : A) :
    navigationImage.{u,0} (DPGraph.Span.ofFunction f) {a.val} = {(f a).val} :=
  navigationImage_singleton.{u,0} (DPGraph.Span.ofFunction f) Function.injective_id a

end Clafer.Constraints
