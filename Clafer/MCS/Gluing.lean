module

public import Clafer.MCS.Laws
public import FormalCD.Morphism

/-!
# Gluing resolved MCS roles

SoSyM §6.2.5 and Appendix B.4 Definition 10, with the approved Q4 rule:
class/map roles identify exactly at equal resolved referents. Incidence and
metadata must be constant on those fibers. Names never generate identifications.
The declaration set is the exact translated image, without adding defaults.
-/

@[expose] public section
namespace Clafer.MCS.Gluing
open CategoryTheory

variable {C V : Type} {f : Family C} (r : Roles C V f) (l : Labels (V := V) f)

/-- The incidence obligation precedes construction of the graph map. -/
structure Incidence : Prop where
  source : ∀ m n, l.mapReferent m = l.mapReferent n →
    l.classReferent (r.source m) = l.classReferent (r.source n)
  target : ∀ m n, l.mapReferent m = l.mapReferent n →
    l.classReferent (r.target m) = l.classReferent (r.target n)

abbrev Class := {x // x ∈ Set.range l.classReferent}
abbrev Map := {x // x ∈ Set.range l.mapReferent}

def classLabel (v : V) : Class l := ⟨l.classReferent v, ⟨v, rfl⟩⟩
def mapLabel (m : f.MapId) : Map l := ⟨l.mapReferent m, ⟨m, rfl⟩⟩

@[simp] theorem classLabel_eq_iff (v w : V) :
    classLabel l v = classLabel l w ↔ l.classReferent v = l.classReferent w :=
  Subtype.ext_iff

@[simp] theorem mapLabel_eq_iff (m n : f.MapId) :
    mapLabel l m = mapLabel l n ↔ l.mapReferent m = l.mapReferent n :=
  Subtype.ext_iff

noncomputable def classRepresentative (v : Class l) : V := v.property.choose
noncomputable def mapRepresentative (m : Map l) : f.MapId := m.property.choose

theorem classRepresentative_spec (v : Class l) :
    l.classReferent (classRepresentative l v) = v.val := v.property.choose_spec
theorem mapRepresentative_spec (m : Map l) :
    l.mapReferent (mapRepresentative l m) = m.val := m.property.choose_spec

noncomputable def source (m : Map l) : Class l :=
  classLabel l (r.source (mapRepresentative l m))
noncomputable def target (m : Map l) : Class l :=
  classLabel l (r.target (mapRepresentative l m))

variable {r l}

theorem source_label (h : Incidence r l) (m : f.MapId) :
    source r l (mapLabel l m) = classLabel l (r.source m) :=
  Subtype.ext (h.source _ _ (mapRepresentative_spec l (mapLabel l m)))
theorem target_label (h : Incidence r l) (m : f.MapId) :
    target r l (mapLabel l m) = classLabel l (r.target m) :=
  Subtype.ext (h.target _ _ (mapRepresentative_spec l (mapLabel l m)))

variable (r l)

abbrev Arrow (a b : Class l) := {m : Map l // source r l m = a ∧ target r l m = b}
noncomputable def graph : Quiv := @Quiv.of (Class l) ⟨Arrow r l⟩

/-- Endpoint equations are checked before any formula is transported. -/
noncomputable def label (h : Incidence r l) : r.graph ⥤q graph r l where
  obj := classLabel l
  map e := ⟨mapLabel l e.val,
    (source_label h e.val).trans (congrArg (classLabel l) e.property.1),
    (target_label h e.val).trans (congrArg (classLabel l) e.property.2)⟩

def roleArrow (m : f.MapId) : r.Arrow (r.source m) (r.target m) := ⟨m, rfl, rfl⟩

noncomputable def labeledArrow (h : Incidence r l) (m : f.MapId) :
    FormalCD.Metamodel.ArrowData (graph r l) :=
  ⟨classLabel l (r.source m), classLabel l (r.target m), (label r l h).map (roleArrow r m)⟩

theorem arrowData_ext (x y : FormalCD.Metamodel.ArrowData (graph r l))
    (h : x.2.2.val = y.2.2.val) : x = y := by
  rcases x with ⟨a, b, m, hs, ht⟩
  rcases y with ⟨a', b', m', hs', ht'⟩
  change m = m' at h
  subst m'
  cases hs; cases ht; cases hs'; cases ht'
  rfl

/-- Includes endpoint equality, even when the original roles have different endpoints. -/
theorem labeledArrow_eq_iff (h : Incidence r l) (m n : f.MapId) :
    labeledArrow r l h m = labeledArrow r l h n ↔ l.mapReferent m = l.mapReferent n := by
  constructor
  · exact fun he => congrArg (fun a => a.2.2.val.val) he
  · exact fun he => arrowData_ext r l _ _ (Subtype.ext he)

theorem label_obj_surjective (h : Incidence r l) : Function.Surjective (label r l h).obj := by
  rintro ⟨v, w, rfl⟩
  exact ⟨w, rfl⟩

variable {σ : DPGraph.Signature.{0,0,0}}

/-- Full bindings, including isolated vertices and repeated arrows, postcompose unchanged. -/
noncomputable def diagram (h : Incidence r l) (d : Formulas r σ) : DPGraph σ :=
  ⟨graph r l, Set.range (fun i => (d.formula i).translate (label r l h))⟩

theorem declared_iff (h : Incidence r l) (d : Formulas r σ) (φ) :
    φ ∈ (diagram r l h d).declarations ↔
      ∃ i, (d.formula i).translate (label r l h) = φ := Iff.rfl

noncomputable def labelHom (h : Incidence r l) (d : Formulas r σ) :
    DPGraph.Hom d.diagram (diagram r l h d) where
  toPrefunctor := label r l h
  preserves := by rintro φ ⟨i, rfl⟩; exact ⟨i, rfl⟩

theorem translated_vertex (h : Incidence r l) (φ : DPGraph.Formula σ r.graph)
    (v : σ.arity φ.symbol) :
    (φ.translate (label r l h)).binding.obj v = classLabel l (φ.binding.obj v) := rfl

theorem translated_arrow (h : Incidence r l) (φ : DPGraph.Formula σ r.graph)
    {a b : σ.arity φ.symbol} (e : a ⟶ b) :
    (φ.translate (label r l h)).binding.map e = (label r l h).map (φ.binding.map e) := rfl

variable {R : FormalCD.Registry.{0}} (p : V → Option R.Id)

/-- Invalid inputs have no proof of this proposition; conflicts are never repaired.
Registry kinds follow registry identity, so equal annotations also preserve kinds. -/
structure Compatible : Prop extends Incidence r l where
  class_name : ∀ v w, l.classReferent v = l.classReferent w → l.className v = l.className w
  map_name : ∀ m n, l.mapReferent m = l.mapReferent n → l.mapName m = l.mapName n
  predefined : ∀ v w, l.classReferent v = l.classReferent w → p v = p w
  mode : ∀ m n, l.mapReferent m = l.mapReferent n → m.mode = n.mode

variable {W : FormalCD.Vocabulary.{0,0,0}}

noncomputable def raw (h : Compatible r l p) (d : Formulas r W.signature) :
    FormalCD.RawOver W R where
  toDPGraph := diagram r l h.toIncidence d
  className v := l.className (classRepresentative l v)
  mapName e := l.mapName (mapRepresentative l e.val)
  predefined v := p (classRepresentative l v)
  mode e := (mapRepresentative l e.val).mode

variable {r l p}

@[simp] theorem className_label (h : Compatible r l p) (d : Formulas r W.signature) (v : V) :
    (raw r l p h d).className (classLabel l v) = l.className v :=
  h.class_name _ _ (classRepresentative_spec l (classLabel l v))

@[simp] theorem mapName_label (h : Compatible r l p) (d : Formulas r W.signature)
    {a b : r.graph} (e : a ⟶ b) :
    (raw r l p h d).mapName ((label r l h.toIncidence).map e) = l.mapName e.val :=
  h.map_name _ _ (mapRepresentative_spec l (mapLabel l e.val))

@[simp] theorem predefined_label (h : Compatible r l p) (d : Formulas r W.signature) (v : V) :
    (raw r l p h d).predefined (classLabel l v) = p v :=
  h.predefined _ _ (classRepresentative_spec l (classLabel l v))

theorem kind_label (h : Compatible r l p) (d : Formulas r W.signature) (v : V) :
    ((raw r l p h d).predefined (classLabel l v)).map R.kind = (p v).map R.kind := by
  rw [predefined_label]

@[simp] theorem mode_label (h : Compatible r l p) (d : Formulas r W.signature)
    {a b : r.graph} (e : a ⟶ b) :
    (raw r l p h d).mode ((label r l h.toIncidence).map e) = e.val.mode :=
  h.mode _ _ (mapRepresentative_spec l (mapLabel l e.val))

variable (r l p)

/-- Naming assumptions on the input, independently of declaration preservation.
Predefined uniqueness is required at referent identity, not at role identity. -/
structure Naming : Prop where
  predefined_name : ∀ v i, p v = some i → l.className v = R.name i
  user_name : ∀ v, p v = none → ¬R.Reserved (l.className v)
  unique_predefined : ∀ v w i, p v = some i → p w = some i →
    l.classReferent v = l.classReferent w
  inclusion_name : ∀ m, m.mode = .inclusion → l.mapName m = "isA"

/-- Effective defaults must already be in the source bank. Bag maps have no
obligation here. MCS.Valid by itself does not imply this property. -/
structure Defaults (d : Formulas r W.signature) : Prop where
  inclusion : ∀ m, m.mode = .inclusion →
    W.embed (FormalCD.inclusionFormula (G := r.graph) (roleArrow r m)) ∈ d.diagram.declarations
  ordinary : ∀ m, m.mode = .ordinary →
    W.embed (FormalCD.setValuedFormula (G := r.graph) (roleArrow r m)) ∈ d.diagram.declarations

variable {r l p}

theorem raw_wellFormed (h : Compatible r l p) (d : Formulas r W.signature)
    (hn : Naming l p) (hd : Defaults r d) : (raw r l p h d).WellFormed where
  predefined_name v i hi := hn.predefined_name _ i hi
  user_name v hv := hn.user_name _ hv
  unique_predefined v w i hv hw := by
    apply Subtype.ext
    have he := hn.unique_predefined _ _ i hv hw
    exact (classRepresentative_spec l v).symm.trans (he.trans (classRepresentative_spec l w))
  inclusion_name e he := hn.inclusion_name _ he
  inclusion_decl := by
    intro a b e he
    rcases e with ⟨m, rfl, rfl⟩
    have hp := (labelHom r l h.toIncidence d).preserves (hd.inclusion (mapRepresentative l m) he)
    have hf := (W.embed_translate
      (FormalCD.inclusionFormula (G := r.graph) (roleArrow r (mapRepresentative l m)))
      (label r l h.toIncidence)).symm.trans
      (congrArg W.embed (FormalCD.inclusionFormula_translate
        (G := r.graph) (roleArrow r (mapRepresentative l m)) (label r l h.toIncidence)))
    have hp' := hf ▸ hp
    have hm : (label r l h.toIncidence).map (roleArrow r (mapRepresentative l m)) =
        (⟨m, rfl, rfl⟩ : Arrow r l (source r l m) (target r l m)) :=
      Subtype.ext (Subtype.ext (mapRepresentative_spec l m))
    exact (congrArg (fun e => W.embed (FormalCD.inclusionFormula e) ∈
      (diagram r l h.toIncidence d).declarations) hm).mp hp'
  ordinary_decl := by
    intro a b e he
    rcases e with ⟨m, rfl, rfl⟩
    have hp := (labelHom r l h.toIncidence d).preserves (hd.ordinary (mapRepresentative l m) he)
    have hf := (W.embed_translate
      (FormalCD.setValuedFormula (G := r.graph) (roleArrow r (mapRepresentative l m)))
      (label r l h.toIncidence)).symm.trans
      (congrArg W.embed (FormalCD.setValuedFormula_translate
        (G := r.graph) (roleArrow r (mapRepresentative l m)) (label r l h.toIncidence)))
    have hp' := hf ▸ hp
    have hm : (label r l h.toIncidence).map (roleArrow r (mapRepresentative l m)) =
        (⟨m, rfl, rfl⟩ : Arrow r l (source r l m) (target r l m)) :=
      Subtype.ext (Subtype.ext (mapRepresentative_spec l m))
    exact (congrArg (fun e => W.embed (FormalCD.setValuedFormula e) ∈
      (diagram r l h.toIncidence d).declarations) hm).mp hp'

noncomputable def cd (h : Compatible r l p) (d : Formulas r W.signature)
    (hn : Naming l p) (hd : Defaults r d) : FormalCD.CDOver W R :=
  ⟨raw r l p h d, raw_wellFormed h d hn hd⟩

end Clafer.MCS.Gluing
