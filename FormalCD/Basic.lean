module

public import DPGraph

/-!
# Formal class diagrams

SoSyM §6.1.1–3 and Figure 21b–c, over B.4 Definitions 6–9.
Names annotate existing graph identities. The registry records identity and
naming, not concrete primitive domains. Well-formedness is syntactic validity;
model satisfaction still requires an explicit DPGraph interpretation.
-/

@[expose] public section

universe p v u v' u'

namespace FormalCD

open CategoryTheory DPGraph.Predicates

/-- Distinguish the singleton vocabulary from primitive-domain vocabulary. -/
inductive PredefinedKind where
  | singleton | primitive
  deriving DecidableEq

/-- Shared vocabulary with stable keys. Diagrams may select any subset of it. -/
structure Registry where
  Id : Type p
  name : Id → String
  kind : Id → PredefinedKind

def Registry.Reserved (R : Registry) (name : String) : Prop :=
  ∃ i, R.name i = name

/-- Inclusion is a separate mode; bag mode carries no implicit declaration. -/
inductive MapMode where
  | ordinary | bag | inclusion
  deriving DecidableEq

/-- Bind the existing unary arity to an arrow, retaining both endpoints. -/
def arrowBinding {G : Quiv.{v,u}} {a b : G} (e : a ⟶ b) : Arity.unary ⥤q G where
  obj | .source => a | .target => b
  map | .arrow => e

def inclusionFormula {G : Quiv.{v,u}} {a b : G} (e : a ⟶ b) :
    DPGraph.Formula signature G := ⟨.inclusion, arrowBinding e⟩

def setValuedFormula {G : Quiv.{v,u}} {a b : G} (e : a ⟶ b) :
    DPGraph.Formula signature G := ⟨.setValued, arrowBinding e⟩

theorem arrowBinding_comp {G : Quiv.{v,u}} {H : Quiv.{v',u'}}
    {a b : G} (e : a ⟶ b) (F : G ⥤q H) :
    (arrowBinding e).comp F = arrowBinding (F.map e) := by
  exact Prefunctor.ext (by intro x; cases x <;> rfl)
    (by intro x y f; cases f; rfl)

@[simp] theorem inclusionFormula_translate {G : Quiv.{v,u}} {H : Quiv.{v',u'}}
    {a b : G} (e : a ⟶ b) (F : G ⥤q H) :
    (inclusionFormula e).translate F = inclusionFormula (F.map e) :=
  congrArg (DPGraph.Formula.mk (σ := signature) .inclusion) (arrowBinding_comp e F)

@[simp] theorem setValuedFormula_translate {G : Quiv.{v,u}} {H : Quiv.{v',u'}}
    {a b : G} (e : a ⟶ b) (F : G ⥤q H) :
    (setValuedFormula e).translate F = setValuedFormula (F.map e) :=
  congrArg (DPGraph.Formula.mk (σ := signature) .setValued) (arrowBinding_comp e F)

/-- Inspectable raw data, including invalid diagrams. `declarations` is the
single effective set: authored formulas and required defaults live together. -/
structure Raw (R : Registry.{p}) extends DPGraph.{0,0,0,v,u} signature where
  className : carrier → String
  mapName : ∀ {a b : carrier}, (a ⟶ b) → String
  predefined : carrier → Option R.Id
  mode : ∀ {a b : carrier}, (a ⟶ b) → MapMode

/-- §6.1 naming/default disciplines. Typed Formula bindings already enforce
arity and incidence. No global name injectivity or inheritance acyclicity. -/
structure Raw.WellFormed {R : Registry.{p}} (D : Raw.{p,v,u} R) : Prop where
  predefined_name : ∀ c i, D.predefined c = some i → D.className c = R.name i
  user_name : ∀ c, D.predefined c = none → ¬ R.Reserved (D.className c)
  unique_predefined : ∀ c d i,
    D.predefined c = some i → D.predefined d = some i → c = d
  inclusion_name : ∀ {a b} (e : a ⟶ b), D.mode e = .inclusion → D.mapName e = "isA"
  inclusion_decl : ∀ {a b} (e : a ⟶ b), D.mode e = .inclusion →
    inclusionFormula e ∈ D.declarations
  ordinary_decl : ∀ {a b} (e : a ⟶ b), D.mode e = .ordinary →
    setValuedFormula e ∈ D.declarations

/-- A syntactically valid CD. This proof asserts no existence of a model. -/
structure CD (R : Registry.{p}) extends Raw.{p,v,u} R where
  wellFormed : toRaw.WellFormed

end FormalCD
