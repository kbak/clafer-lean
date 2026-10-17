#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ $# != 0 && !( $# == 1 && "$1" == --preflight ) ]]; then
  echo 'Usage: bash scripts/check.sh [--preflight]' >&2
  exit 2
fi

run_step() {
  local label=$1 started=$SECONDS status=0
  shift
  printf '\n[check] %s: starting\n' "$label"
  "$@" || status=$?
  printf '[check] %s: exit %s, %ss\n' "$label" "$status" "$((SECONDS - started))"
  return "$status"
}

# [impl->req~lean-validation~1]
# [itest->req~lean-validation~1]
export PYTHONDONTWRITEBYTECODE=1
validation_dir=.lake/validation
# Catch source/inventory mistakes before installing Lean or preparing dependencies.
run_step 'Module inventory' python3 scripts/project_modules.py --output-dir "$validation_dir"
run_step 'Module regressions' python3 -m unittest discover -s tests -p test_project_modules.py -v

if [[ "${1:-}" == --preflight ]]; then
  exit 0
fi

# IntentMade supplies this trusted profile to provision the pinned Lean toolchain.
if [[ -n "${FACTORY_TESTS:-}" && -f "$FACTORY_TESTS/lean-env.sh" ]]; then
  printf '\n[check] Lean toolchain: starting\n'
  started=$SECONDS
  source "$FACTORY_TESTS/lean-env.sh"
  printf '[check] Lean toolchain: exit 0, %ss\n' "$((SECONDS - started))"
fi

# Dependency provisioning is optional; the build and kernel checks always run.
if ! run_step 'Mathlib cache' lake exe cache get Mathlib.CategoryTheory.Category.Quiv \
    Mathlib.Data.Fintype.Basic Mathlib.CategoryTheory.Limits.Shapes.Pullback.PullbackCone; then
  echo 'Mathlib cache unavailable; building the pinned dependencies from source.' >&2
fi
# Use the discovered inventory at every stage, including modules not reachable
# from an entrypoint (notably examples and future internal helpers).
mapfile -t modules < "$validation_dir/modules.txt"
run_step 'Library and module build' lake build DPGraph FormalCD Clafer "${modules[@]/#/+}"
# Run the audit and regression gates before the more expensive kernel replay.
# An invalid candidate should fail before rechecking all compiled project proofs.
run_step 'Axiom audit' lake env lean -DwarningAsError=true "$validation_dir/axiom_audit.lean"
while IFS= read -r source; do
  run_step "Lean test $source" lake env lean -DwarningAsError=true "$source"
done < "$validation_dir/tests.txt"

run_step 'Python tests (including Lean audit fixtures)' lake env python3 -m unittest discover -s tests -v

# leanchecker recursively enumerates each public root, including unimported
# helpers/examples. Avoid rescanning every dependency directory for each leaf.
run_step 'Kernel checks (all discovered modules)' \
  env LEAN_NUM_THREADS="${LEAN_NUM_THREADS:-4}" \
  lake env leanchecker --verbose DPGraph FormalCD Clafer
