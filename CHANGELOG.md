# Changelog

Format mengikuti [Keep a Changelog](https://keepachangelog.com/id/1.1.0/).
Versi mengikuti [SemVer](https://semver.org/lang/id/).

## [2.0.0] — 2026-11-05

### Brutal
- **OTP flood engine baru.** Multi-thread sampai 64 worker, rotasi Android-ID,
  MCC/MNC 14 negara, dan versi WhatsApp acak di setiap request. Server tidak
  bisa mengingat nomor target sudah pernah meminta OTP.
- **Mode `burn`.** Jeda dirapatkan ke 0.2s selama server membalas sukses.
  Otomatis membaca `retry_after` dan menurunkan ritme saat kena limit.
- **Metode `both`.** SMS dan voice call bergantian acak. Voice memicu dering,
  jauh lebih mengganggu daripada notifikasi.
- **Mode COMBO.** OTP flood berjalan di background sambil payload force-close
  dilontarkan. Target panik, buka WhatsApp, langsung disambut Zalgo 45k.
- **Banner brutal.** Binary rain, logo WhatsApp, wordmark blok, indikator platform.

### Ditambahkan
- Dukungan Kali Linux dan Debian: adapter `lib/platform.sh` memilih
  `termux-open-url` atau `xdg-open`, `termux-clipboard-set` atau `wl-copy`/`xclip`.
- Mode `--no-open` untuk lingkungan headless / SSH.
- Subcommand CLI penuh: `delay`, `crash`, `otp`, `combo`, `check`.
- `install.sh` dan `uninstall.sh` dengan deteksi platform otomatis.
- Workflow CI: shellcheck, py_compile, node --check.

### Diubah
- Payload builder dipisah ke `lib/payload.py`, 6 varian termasuk `combo`.
- Penanganan SIGINT pada OTP flood: thread diberi kesempatan selesai, statistik
  akhir tetap dicetak.
- Intensitas 5 (90k) diperingatkan untuk engine AUTO karena batas 65.536 char.

### Diperbaiki
- Normalisasi nomor tidak lagi merusak input berawalan `+`.
- Payload >7.500 char otomatis lewat clipboard, tidak lagi terpotong URL.
- Fallback `am start` untuk ROM yang memblokir intent Termux.

## [1.0.0] — 2026-11-04

### Ditambahkan
- Rilis pertama. Bug delay (Hangul filler, zero-width space, long line),
  bug force close (Zalgo, RTL override), OTP flood dasar, engine intent dan Baileys.
