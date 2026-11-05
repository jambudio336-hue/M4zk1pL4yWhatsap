# shellcheck shell=bash
# Adapter lintas platform. Termux (Android) vs Linux desktop (Kali/Debian).
# Tidak ada yang dieksekusi saat sourcing.

if [ -n "${TERMUX_VERSION:-}" ] || [ -d /data/data/com.termux ]; then
  MZK_PLATFORM="termux"
else
  MZK_PLATFORM="linux"
fi
export MZK_PLATFORM

mzk_open_url(){
  local url="$1"
  if [ "${MZK_NOOPEN:-0}" = "1" ]; then printf '%s\n' "$url"; return 0; fi
  case "$MZK_PLATFORM" in
    termux)
      if command -v termux-open-url >/dev/null 2>&1; then
        termux-open-url "$url" 2>/dev/null; return 0
      fi
      am start -a android.intent.action.VIEW -d "$url" >/dev/null 2>&1 && return 0
      printf '%s\n' "$url"; return 1 ;;
    linux)
      if command -v xdg-open >/dev/null 2>&1; then
        xdg-open "$url" >/dev/null 2>&1 & return 0
      fi
      printf '%s\n' "$url"; return 1 ;;
  esac
}

mzk_set_clip(){
  case "$MZK_PLATFORM" in
    termux)
      command -v termux-clipboard-set >/dev/null 2>&1 && termux-clipboard-set && return 0 ;;
    linux)
      command -v wl-copy >/dev/null 2>&1 && wl-copy 2>/dev/null && return 0
      command -v xclip  >/dev/null 2>&1 && xclip -selection clipboard 2>/dev/null && return 0
      command -v xsel  >/dev/null 2>&1 && xsel -ib 2>/dev/null && return 0 ;;
  esac
  return 1
}

mzk_deps_hint(){
  case "$MZK_PLATFORM" in
    termux) echo "pkg install -y python nodejs-lts termux-api" ;;
    linux)  echo "sudo apt install -y python3 nodejs npm xdg-utils xclip" ;;
  esac
}
