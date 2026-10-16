#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

# IntentMade supplies this trusted profile to provision the pinned Lean toolchain.
if [[ -n "${FACTORY_TESTS:-}" && -f "$FACTORY_TESTS/lean-env.sh" ]]; then
  source "$FACTORY_TESTS/lean-env.sh"
fi

# [impl->req~lean-validation~1]
# [itest->req~lean-validation~1]
export PYTHONDONTWRITEBYTECODE=1
validation_dir=.lake/validation
python3 scripts/project_modules.py --output-dir "$validation_dir"
# Dependency provisioning is optional; the build and kernel checks always run.
if ! lake exe cache get Mathlib.CategoryTheory.Category.Quiv Mathlib.Data.Fintype.Basic; then
  echo 'Mathlib cache unavailable; building the pinned dependencies from source.' >&2
fi
lake build
# Use the discovered inventory at every stage, including modules not reachable
# from an entrypoint (notably examples and future internal helpers).
while IFS= read -r module; do
  lake build "+$module"
  lake env leanchecker "$module"
done < "$validation_dir/modules.txt"
lake env lean -DwarningAsError=true "$validation_dir/axiom_audit.lean"
while IFS= read -r source; do
  lake env lean -DwarningAsError=true "$source"
done < "$validation_dir/tests.txt"

lake env python3 -m unittest discover -s tests -v
