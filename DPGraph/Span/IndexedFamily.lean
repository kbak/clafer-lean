module

public import DPGraph.Span.Basic

/-!
# Indexed mappings and spans

SoSyM B.1, Definitions 1–5 and Theorem 1. A family-to-span head has universe
`max u w`; returning to a family retains that join. Equivalences may cross
universes, so no resizing is needed.
-/

@[expose] public section

universe u v w w'

namespace DPGraph

structure IndexedFamily (A : Type u) (B : Type v) where
  Index : A → Type w
  eval : ∀ a, Index a → B

namespace IndexedFamily

variable {A : Type u} {B : Type v}

structure Equivalence (f : IndexedFamily.{u, v, w} A B)
    (g : IndexedFamily.{u, v, w'} A B) where
  equiv : ∀ a, f.Index a ≃ g.Index a
  eval_eq : ∀ a i, g.eval a (equiv a i) = f.eval a i

def Equivalence.refl (f : IndexedFamily.{u, v, w} A B) : Equivalence f f where
  equiv _ := Equiv.refl _
  eval_eq _ _ := rfl

def Equivalence.symm {f : IndexedFamily.{u, v, w} A B}
    {g : IndexedFamily.{u, v, w'} A B} (e : Equivalence f g) : Equivalence g f where
  equiv a := (e.equiv a).symm
  eval_eq a i := by simpa using (e.eval_eq a ((e.equiv a).symm i)).symm

def toSpan (f : IndexedFamily.{u, v, w} A B) : Span.{u, v, max u w} A B where
  Link := Σ a, f.Index a
  source := Sigma.fst
  target p := f.eval p.1 p.2

def red (f : IndexedFamily.{u, v, w} A B) (a : A) (b : B) : Prop :=
  ∃ i, f.eval a i = b

end IndexedFamily

namespace Span

variable {A : Type u} {B : Type v}

def toFamily (q : Span.{u, v, w} A B) : IndexedFamily.{u, v, w} A B where
  Index a := { l : q.Link // q.source l = a }
  eval _ l := q.target l.1

/-- The span roundtrip is a head equivalence, with head universe `max u w`. -/
def familySpanIso (q : Span.{u, v, w} A B) : Iso q.toFamily.toSpan q where
  equiv :=
    { toFun := fun p => p.2.1
      invFun := fun l => ⟨q.source l, ⟨l, rfl⟩⟩
      left_inv := by rintro ⟨a, l, h⟩; cases h; rfl
      right_inv := fun _ => rfl }
  source_eq p := p.2.2
  target_eq _ := rfl

/-- B.1 Theorem 1: the family of source fibers has exactly the reduced members. -/
theorem red_toFamily (q : Span.{u, v, w} A B) : q.toFamily.red = q.red := by
  funext a b
  apply propext
  constructor
  · rintro ⟨⟨l, hs⟩, ht⟩
    exact ⟨l, hs, ht⟩
  · rintro ⟨l, hs, ht⟩
    exact ⟨⟨l, hs⟩, ht⟩

end Span

namespace IndexedFamily

variable {A : Type u} {B : Type v}

/-- The family roundtrip allows index universes `max u w` and `w`. -/
def spanFamilyEquivalence (f : IndexedFamily.{u, v, w} A B) :
    Equivalence f.toSpan.toFamily f where
  equiv a :=
    { toFun := fun p => p.2 ▸ p.1.2
      invFun := fun i => ⟨⟨a, i⟩, rfl⟩
      left_inv := by rintro ⟨⟨a', i⟩, h⟩; cases h; rfl
      right_inv := fun _ => rfl }
  eval_eq := by rintro a ⟨⟨a', i⟩, h⟩; cases h; rfl

/-- B.1 Theorem 1 in the other direction, stated as endpoint-membership equality. -/
theorem red_toSpan (f : IndexedFamily.{u, v, w} A B) : f.toSpan.red = f.red := by
  funext a b
  apply propext
  constructor
  · rintro ⟨⟨a', i⟩, hs, ht⟩
    cases hs
    exact ⟨i, ht⟩
  · rintro ⟨i, hi⟩
    exact ⟨⟨a, i⟩, rfl, hi⟩

end IndexedFamily
end DPGraph
