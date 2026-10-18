module

public import FormalCD
public import Clafer.Shape.Diagram
public import Clafer.MCS.Metamodel
public import Clafer.Constraints.Typing
public import Clafer.Compile.Basic

/-!
# Structural 2014 Clafer

Resolved deep syntax, typed core constraints, a binder/context boundary and
individual Shapes over FormalCD and DPGraph, with the Figure 23 MCS structural
disciplines and structural Compile. Constraint meanings and gluing remain
separate increments; see docs/ARCHITECTURE.md. Acceptance examples are checked separately.
-/
