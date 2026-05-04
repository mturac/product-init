#!/usr/bin/env bash
# product-init install script
# Usage: bash install.sh [--openclaw] [--codex] [--all]
set -euo pipefail

SKILL_SRC="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_SKILL="$HOME/.claude/skills/product-init"
OPENCLAW_SKILL="$HOME/.openclaw/skills/product-init"

install_venv() {
  if [ ! -f "$SKILL_SRC/.venv/bin/python" ]; then
    echo "→ Creating venv..."
    python3 -m venv "$SKILL_SRC/.venv"
    "$SKILL_SRC/.venv/bin/pip" install -q -r "$SKILL_SRC/scripts/requirements.txt"
    echo "  venv ready at $SKILL_SRC/.venv"
  else
    echo "  venv already exists, skipping"
  fi
}

install_claude() {
  if [ "$SKILL_SRC" != "$CLAUDE_SKILL" ]; then
    mkdir -p "$(dirname "$CLAUDE_SKILL")"
    ln -sf "$SKILL_SRC" "$CLAUDE_SKILL"
    echo "→ Linked to $CLAUDE_SKILL"
  else
    echo "  Already installed at Claude Code skill dir"
  fi
}

install_openclaw() {
  if [ -d "$HOME/.openclaw" ]; then
    mkdir -p "$HOME/.openclaw/skills"
    ln -sf "$SKILL_SRC" "$OPENCLAW_SKILL"
    echo "→ Linked to $OPENCLAW_SKILL"
  else
    echo "  ~/.openclaw not found — skipping OpenClaw install"
  fi
}

print_usage() {
  echo "Usage: bash install.sh [--openclaw] [--codex] [--all]"
  echo "  --openclaw   Link skill into ~/.openclaw/skills/"
  echo "  --codex      Print Codex env var setup (no files to install)"
  echo "  --all        Install everywhere"
  echo "  (no args)    Install venv + Claude Code link only"
}

DO_OPENCLAW=false
DO_CODEX=false

for arg in "$@"; do
  case $arg in
    --openclaw) DO_OPENCLAW=true ;;
    --codex)    DO_CODEX=true ;;
    --all)      DO_OPENCLAW=true; DO_CODEX=true ;;
    --help|-h)  print_usage; exit 0 ;;
  esac
done

install_venv
install_claude

if $DO_OPENCLAW; then
  install_openclaw
fi

if $DO_CODEX; then
  echo "→ Codex: set this in your shell profile:"
  echo "  export PRODUCT_INIT_SKILL_DIR=\"$SKILL_SRC\""
fi

echo ""
echo "product-init installed. Verify with:"
echo "  $SKILL_SRC/.venv/bin/python $SKILL_SRC/scripts/orchestrator.py --help"
