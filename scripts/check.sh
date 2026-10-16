#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

# IntentMade supplies this trusted profile to provision the pinned Lean toolchain.
if [[ -n "${FACTORY_TESTS:-}" && -f "$FACTORY_TESTS/lean-env.sh" ]]; then
  source "$FACTORY_TESTS/lean-env.sh"
fi

# [impl->req~lean-validation~1]
# [itest->req~lean-validation~1]
# Dependency provisioning is optional; the build and kernel checks always run.
if ! lake exe cache get Mathlib.CategoryTheory.Category.Quiv Mathlib.Data.Fintype.Basic; then
  echo 'Mathlib cache unavailable; building the pinned dependencies from source.' >&2
fi
lake build
lake env leanchecker ClaferLean
lake env lean -DwarningAsError=true tests/axiom_audit.lean

PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
