module

import DPGraph
public meta import Lean.Elab.Command

/-! Public foundation smoke test: no upper layer or examples are imported. -/
#check DPGraph
#check DPGraph.Signature
#check DPGraph.Formula
#check DPGraph.Formula.translate
#check DPGraph.Formula.translate_id
#check DPGraph.Formula.translate_comp
#check DPGraph.Hom
#check DPGraph.Hom.ext
#check DPGraph.Hom.ext_of_obj_map
#check DPGraph.Hom.comp_preserves
#check DPGraph.Hom.id_comp
#check DPGraph.Hom.comp_id
#check DPGraph.Hom.comp_assoc

open Lean in
run_cmd do
  let env ← getEnv
  for name in env.header.moduleNames do
    if (`FormalCD).isPrefixOf name || (`Clafer).isPrefixOf name ||
        (`DPGraph.Examples).isPrefixOf name then
      throwError "independent DPGraph entrypoint imported {name}"
