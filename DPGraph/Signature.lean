module

public import Mathlib.CategoryTheory.Category.Quiv

/-!
# Signatures for diagram predicates

SoSyM (2014 author preprint), Appendix B.4, Definitions 6–7.
A graph is Mathlib's `Quiv`, whose arrows form a `Quiver`. There are no
identity/composition operations on carrier arrows. The paper's total edge set
is represented by `Σ x y : G, (x ⟶ y)`; the two projections give its endpoints.
-/

@[expose] public section

universe s va ua

namespace DPGraph

/-- A symbol type with a graph-valued arity (SoSyM B.4, Definition 7).
No dependencies or inference-closure axioms are part of this signature. -/
structure Signature where
  Symbol : Type s
  arity : Symbol → CategoryTheory.Quiv.{va, ua}

end DPGraph
