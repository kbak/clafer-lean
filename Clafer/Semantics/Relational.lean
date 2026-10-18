module

public import Clafer.Semantics.Interpretation
public import Mathlib.Tactic.FinCases

/-!
# Representation lemmas for ordinary maps and occurrence counts

SoSyM B.1 Definitions 1–5, B.2.1 (Q1), Table 3/A.1. The exact-one
predicate is totality and single-valuedness of links, not endpoint reduction.
-/

@[expose] public section
namespace Clafer.Semantics
open DPGraph DPGraph.Predicates

universe u

theorem inRange_one_iff (A : Type u) :
    InRange Clafer.one A ↔ Nonempty A ∧ Subsingleton A := by
  unfold InRange Clafer.one
  constructor
  · rintro ⟨⟨lo⟩, ⟨hi⟩⟩
    exact ⟨⟨lo 0⟩, ⟨fun a b => hi.injective (Subsingleton.elim _ _)⟩⟩
  · rintro ⟨⟨a⟩, hs⟩
    exact ⟨⟨⟨fun _ => a, fun _ _ _ => Subsingleton.elim _ _⟩⟩,
      ⟨⟨fun _ => 0, fun x y _ => @Subsingleton.elim _ hs x y⟩⟩⟩

theorem one_iff_total_single {A B : Type} (q : Span A B) :
    TargetMultiplicity Clafer.one q ↔ Total q ∧ SingleValued q := by
  simp only [TargetMultiplicity, inRange_one_iff, total_fibers, singleValued_fibers,
    forall_and]

theorem relation_one_iff {A B : Type} (R : A → B → Prop) :
    TargetMultiplicity Clafer.one (Span.ofRelation R) ↔ ∀ a, ∃! b, R a b := by
  rw [one_iff_total_single]
  constructor
  · rintro ⟨ht, hs⟩ a
    obtain ⟨⟨⟨a', b⟩, hr⟩, he⟩ := ht a
    change a' = a at he
    subst a'
    refine ⟨b, hr, ?_⟩
    intro b' hb'
    have he := hs (a₁ := ⟨(a, b'), hb'⟩) (a₂ := ⟨(a, b), hr⟩) rfl
    exact congrArg (fun l => l.val.2) he
  · intro h
    constructor
    · intro a
      obtain ⟨b, hb, _⟩ := h a
      exact ⟨⟨(a, b), hb⟩, rfl⟩
    · rintro ⟨⟨a, b⟩, hb⟩ ⟨⟨a', b'⟩, hb'⟩ he
      change a = a' at he
      subst a'
      exact Subtype.ext (Prod.ext rfl ((h a).unique hb hb'))

theorem setValued_one_iff {A B : Type} (q : Span A B) (hq : SetValued q) :
    TargetMultiplicity Clafer.one q ↔ ∀ a, ∃! b, q.red a b :=
  (targetMultiplicity_iff _ (q.relationIso hq)).trans (relation_one_iff _)

theorem unique_subtype_iff {U : Type} (B : Set U) (P : U → Prop)
    (typed : ∀ b, P b → b ∈ B) : (∃! b : B, P b.val) ↔ ∃! b, P b := by
  constructor
  · rintro ⟨b, hb, hu⟩
    exact ⟨b.val, hb, fun c hc => congrArg Subtype.val (hu ⟨c, typed c hc⟩ hc)⟩
  · rintro ⟨b, hb, hu⟩
    exact ⟨⟨b, typed b hb⟩, hb, fun c hc => Subtype.ext (hu c.val hc)⟩

theorem identity_inclusion_iff {U : Type} (A B : Set U) :
    Inclusion (Span.ofRelation (fun (a : A) (b : B) => a.val = b.val)) ↔ A ⊆ B := by
  constructor
  · exact inclusion_subset
  · intro h
    refine ⟨⟨?_, ?_⟩, ?_⟩
    · rintro ⟨⟨a, b⟩, hab⟩ ⟨⟨a', b'⟩, hab'⟩ he
      change a = a' at he
      subst a'
      exact Subtype.ext (Prod.ext rfl (Subtype.ext (hab.symm.trans hab')))
    · intro a
      exact ⟨⟨(a, ⟨a.val, h a.property⟩), rfl⟩, rfl⟩
    · intro l
      exact l.property.symm

/-- With one dereference link per head, composable target links and head
links have exactly the same multiplicity, including repeated target values. -/
noncomputable def compositeFiber {A B C : Type} (q : Span A B) (r : Span B C)
    (ht : Total r) (hs : SingleValued r) (a : A) :
    (q.comp r).toFamily.Index a ≃ q.toFamily.Index a :=
  Equiv.ofBijective (fun l => ⟨l.val.val.1, l.property⟩)
    ⟨by
      intro l k he
      apply Subtype.ext
      apply Subtype.ext
      apply Prod.ext
      · exact congrArg Subtype.val he
      · apply hs
        exact l.val.property.symm.trans
          ((congrArg q.target (congrArg Subtype.val he)).trans k.val.property), by
      intro l
      obtain ⟨r', hr⟩ := ht (q.target l.val)
      exact ⟨⟨⟨(l.val, r'), hr.symm⟩, l.property⟩, rfl⟩⟩

theorem composite_multiplicity {A B C : Type} (q : Span A B) (r : Span B C)
    (ht : Total r) (hs : SingleValued r) (range : Range) :
    TargetMultiplicity range (q.comp r) ↔ TargetMultiplicity range q :=
  forall_congr' (fun a => inRange_iff range (compositeFiber q r ht hs a))

def pairSpans {A B C : Type} (q : Span A B) (r : Span A C) :
    (i : Fin 2) → Span A (Fin.cases B (fun _ => C) i) :=
  Fin.cases q (fun _ => r)

theorem two_key_iff {A : Type} {B : Fin 2 → Type} (q : ∀ i, Span A (B i))
    (ht : ∀ i, Total (q i)) (hs : ∀ i, SingleValued (q i)) :
    Key q ↔ ∀ a a' (b : B 0) (c : B 1),
      (q 0).red a b → (q 1).red a c →
      (q 0).red a' b → (q 1).red a' c → a = a' := by
  rw [key_total_singleValued_iff _ ht hs]
  constructor
  · intro h a a' b c hq hr hq' hr'
    apply h
    funext i
    fin_cases i
    · exact ((red_iff_targetValue_eq (q 0) (ht 0) (hs 0) a b).mp hq).trans
        ((red_iff_targetValue_eq (q 0) (ht 0) (hs 0) a' b).mp hq').symm
    · exact ((red_iff_targetValue_eq (q 1) (ht 1) (hs 1) a c).mp hr).trans
        ((red_iff_targetValue_eq (q 1) (ht 1) (hs 1) a' c).mp hr').symm
  · intro h a a' he
    exact h a a' (targetValue (q 0) (ht 0) (hs 0) a)
      (targetValue (q 1) (ht 1) (hs 1) a)
      ((red_iff_targetValue_eq _ _ _ _ _).mpr rfl)
      ((red_iff_targetValue_eq _ _ _ _ _).mpr rfl)
      ((red_iff_targetValue_eq _ _ _ _ _).mpr (congrFun he 0).symm)
      ((red_iff_targetValue_eq _ _ _ _ _).mpr (congrFun he 1).symm)

theorem pair_key_iff {A B C : Type} (q : Span A B) (r : Span A C)
    (qt : Total q) (qs : SingleValued q) (rt : Total r) (rs : SingleValued r) :
    Key (pairSpans q r) ↔
      ∀ a a' b c, q.red a b → r.red a c → q.red a' b → r.red a' c → a = a' := by
  have ht : ∀ i, Total (pairSpans q r i) := by intro i; fin_cases i <;> assumption
  have hs : ∀ i, SingleValued (pairSpans q r i) := by intro i; fin_cases i <;> assumption
  rw [key_total_singleValued_iff _ ht hs]
  constructor
  · intro h a a' b c hq hr hq' hr'
    apply h
    funext i
    fin_cases i
    · exact ((red_iff_targetValue_eq q qt qs a b).mp hq).trans
        ((red_iff_targetValue_eq q qt qs a' b).mp hq').symm
    · exact ((red_iff_targetValue_eq r rt rs a c).mp hr).trans
        ((red_iff_targetValue_eq r rt rs a' c).mp hr').symm
  · intro h a a' he
    exact h a a' (targetValue q qt qs a) (targetValue r rt rs a)
      ((red_iff_targetValue_eq q qt qs _ _).mpr rfl)
      ((red_iff_targetValue_eq r rt rs _ _).mpr rfl)
      ((red_iff_targetValue_eq q qt qs _ _).mpr (congrFun he 0).symm)
      ((red_iff_targetValue_eq r rt rs _ _).mpr (congrFun he 1).symm)

namespace Configuration
variable {n : Nat} {U : Type} (m : EffectiveCore n) (s : Configuration (Fin n) U)

theorem parent_one_iff (typed : s.Typed m) (d p : Fin n)
    (hp : m.family.parent d = some p) :
    TargetMultiplicity Clafer.one (s.headMap m d).inverse ↔
      ∀ x, (x ∈ s.head d) → ∃! y, s.contains d y x := by
  rw [setValued_one_iff _ ((setValued_inverse _).mpr (s.headMap_setValued m d))]
  simp only [Span.red_inverse, headMap, Span.red_ofRelation]
  constructor
  · intro h x hx
    exact (unique_subtype_iff _ _ (fun y hy => by
      obtain ⟨_, c, hc, hcy⟩ := typed.1 d y x hy
      have he := hc.symm.trans hp
      cases he
      simpa [hp] using hcy)).mp (h ⟨x, hx⟩)
  · intro h x
    apply (unique_subtype_iff (s.head ((m.family.parent d).getD d))
      (fun y => s.contains d y x.val) (fun y hy => by
      obtain ⟨_, c, hc, hcy⟩ := typed.1 d y x.val hy
      have he := hc.symm.trans hp
      cases he
      simpa [hp] using hcy)).mpr
    exact h x.val x.property

theorem deref_one_iff (typed : s.Typed m) (d t : Fin n)
    (ht : (m.family.reference d).target = some t) :
    TargetMultiplicity Clafer.one (s.derefMap m d) ↔
      ∀ x, (x ∈ s.head d) → ∃! y, s.deref d x y := by
  unfold derefMap
  rw [relation_one_iff]
  constructor
  · intro h x hx
    exact (unique_subtype_iff _ _ (fun y hy => by
      obtain ⟨_, c, hc, hcy⟩ := typed.2 d x y hy
      have he := hc.symm.trans ht
      cases he
      simpa [ht] using hcy)).mp (h ⟨x, hx⟩)
  · intro h x
    apply (unique_subtype_iff (s.head ((m.family.reference d).target.getD d))
      (fun y => s.deref d x.val y) (fun y hy => by
      obtain ⟨_, c, hc, hcy⟩ := typed.2 d x.val y hy
      have he := hc.symm.trans ht
      cases he
      simpa [ht] using hcy)).mpr
    exact h x.val x.property

end Configuration

end Clafer.Semantics
