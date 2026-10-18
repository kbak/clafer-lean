module

public import FormalCD
public import Clafer.Shape.Diagram
public import Clafer.MCS.Metamodel
public import Clafer.MCS.Gluing.Origins
public import Clafer.Constraints.IntegerNavigation
public import Clafer.Compile.Basic
public import Clafer.Compile.GroupSemantics
public import Clafer.Compile.Realization
public import Clafer.Semantics.RealizationCompatibility
public import Clafer.Semantics.Abstracts
public import Clafer.Semantics.Reachability
public import Clafer.Verification.Representation
public import Clafer.Verification.ProtocolProofs

/-!
# Structural 2014 Clafer

Resolved deep syntax, typed core constraints, a binder/context boundary and
individual Shapes over FormalCD and DPGraph, with the Figure 23 MCS structural
disciplines, structural Compile, resolved-referent gluing and verified finite
structural satisfaction for the guarded effective core. Integer extraction and
selected Appendix F navigation have partial meanings; a full constraint interpreter
remains a separate increment; see docs/ARCHITECTURE.md. Acceptance examples are
checked separately.
-/
