#!/usr/bin/env zsh
set -euo pipefail

"$(dirname "$0")/scripts/refresh_paper_index.sh"
python3 "$(dirname "$0")/scripts/distill_topconf_patterns.py"
python3 "$(dirname "$0")/scripts/distill_fulltext_semantics.py"

echo "knowledge rebuild complete (metadata + fulltext)"
