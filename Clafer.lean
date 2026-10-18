module

public import FormalCD
public import Clafer.Shape.Diagram
public import Clafer.MCS.Metamodel
public import Clafer.MCS.Gluing.Origins
public import Clafer.Constraints.IntegerNavigation
public import Clafer.Compile.Basic

/-!
# Structural 2014 Clafer

Resolved deep syntax, typed core constraints, a binder/context boundary and
individual Shapes over FormalCD and DPGraph, with the Figure 23 MCS structural
disciplines, structural Compile and resolved-referent gluing. Integer extraction
and selected Appendix F navigation have partial meanings; a full constraint
interpreter remains a separate increment; see docs/ARCHITECTURE.md. Acceptance
examples are checked separately.
-/
