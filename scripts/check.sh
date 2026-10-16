#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

# IntentMade supplies this trusted profile to provision the pinned Lean toolchain.
if [[ -n "${FACTORY_TESTS:-}" && -f "$FACTORY_TESTS/lean-env.sh" ]]; then
  source "$FACTORY_TESTS/lean-env.sh"
fi

# [impl->req~lean-validation~1]
# [itest->req~lean-validation~1]
lake build
lake env leanchecker ClaferLean

PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
