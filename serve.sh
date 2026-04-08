#!/usr/bin/env bash
# serve.sh — Build and launch Hugo dev server
set -euo pipefail
cd "$(dirname "$0")"
python3 build.py
cd site
exec hugo server --minify --baseURL http://localhost:1313/ --port 1313
