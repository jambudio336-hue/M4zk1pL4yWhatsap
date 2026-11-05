#!/usr/bin/env bash
set -euo pipefail
D="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$D"
. lib/platform.sh

echo "[*] platform terdeteksi: $MZK_PLATFORM"

case "$MZK_PLATFORM" in
  termux)
    pkg update -y >/dev/null 2>&1 || true
    pkg install -y python nodejs-lts termux-api openssl libffi >/dev/null
    TARGET="$PREFIX/bin" ;;
  linux)
    SUDO=""; [ "$(id -u)" -ne 0 ] && SUDO="sudo"
    $SUDO apt-get update -qq
    $SUDO apt-get install -y python3 nodejs npm xdg-utils xclip >/dev/null
    TARGET="/usr/local/bin" ;;
esac

python3 -c 'import sys; assert sys.version_info >= (3,8)' \
  || { echo "butuh Python >= 3.8"; exit 1; }

chmod +x bin/m4zk1p lib/payload.py lib/otp.py lib/auto.js

echo "[*] memasang dependensi Node (Baileys)..."
npm install --silent --no-audit --no-fund

echo "[*] menautkan binary ke $TARGET/m4zk1p"
if [ "$MZK_PLATFORM" = "linux" ] && [ "$(id -u)" -ne 0 ]; then
  sudo ln -sf "$D/bin/m4zk1p" "$TARGET/m4zk1p"
else
  ln -sf "$D/bin/m4zk1p" "$TARGET/m4zk1p"
fi

echo "[+] selesai. jalankan: m4zk1p --menu"
[ "$MZK_PLATFORM" = "termux" ] && \
  echo "[!] pastikan app Termux:API sudah terpasang dari F-Droid"
