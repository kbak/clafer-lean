module

public import Mathlib.Data.Fintype.Basic
public import Mathlib.Data.Fintype.EquivFin

/-!
# Resolved constraint boundary

SoSyM §6.2.2, Figure 22 (p.20), Appendix D.2 (p.31).
This is the input seam for #21, not an expression language or a name resolver.
Lists index occurrences: repeated declaration references are retained.
-/

@[expose] public section
namespace Clafer

structure DeclId where
  value : Nat
  deriving DecidableEq, Repr

structure BinderId where
  value : Nat
  deriving DecidableEq, Repr

/-- The binding's domain is already resolved; names remain display metadata. -/
structure Binder where
  id : BinderId
  name : String
  domainOccurrences : List DeclId
  deriving DecidableEq, Repr

/-- An opaque constraint occurrence with the enclosing declaration and scope bag.
The expression implementation may attach a body to `id` without a dependency
from this module to that implementation. Binder order is outermost first. -/
structure ConstraintBoundary where
  id : Nat
  context : DeclId
  scopeOccurrences : List DeclId
  binders : List Binder := []
  deriving DecidableEq, Repr

abbrev ConstraintBoundary.Occurrence (c : ConstraintBoundary) :=
  Fin c.scopeOccurrences.length

def ConstraintBoundary.referenced (c : ConstraintBoundary) (i : c.Occurrence) : DeclId :=
  c.scopeOccurrences[i]

/-- Resolution validity only; typing and binder semantics belong to #21. -/
def ConstraintBoundary.Resolved (c : ConstraintBoundary) (known : DeclId → Prop) : Prop :=
  known c.context ∧ (∀ i ∈ c.scopeOccurrences, known i) ∧
    (c.binders.map Binder.id).Nodup ∧
    ∀ b ∈ c.binders, ∀ i ∈ b.domainOccurrences, known i

theorem ConstraintBoundary.occurrences_finite (c : ConstraintBoundary) :
    Finite c.Occurrence := inferInstance

end Clafer
