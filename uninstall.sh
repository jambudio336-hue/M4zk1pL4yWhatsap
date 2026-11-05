#!/usr/bin/env bash
set -uo pipefail
D="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. lib/platform.sh
if [ "$MZK_PLATFORM" = "termux" ]; then T="$PREFIX/bin"; else T="/usr/local/bin"; fi
rm -f "$T/m4zk1p"
rm -rf "$D/node_modules" "$D/lib/auth" "$D/lib/p.tmp"
echo "[+] binary dilepas. sumber tetap di $D"
