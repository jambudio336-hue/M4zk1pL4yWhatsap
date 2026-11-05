# Troubleshooting

## `termux-open-url` tidak ditemukan
`pkg install termux-api`, lalu pasang app **Termux:API** dari F-Droid.
Versi Play Store sudah tidak dirawat.

## Intent diblokir (MIUI / HyperOS / ColorOS)
Matikan "MIUI Optimization" di opsi developer, atau beri izin
"Display over other apps" untuk Termux. Fallback `am start` ada di adapter,
tapi sebagian ROM tetap memblokir.

## OTP flood semua balas `ERR` atau `invalid_token`
Skema registrasi WhatsApp berubah. Naikkan entri di list `VERS` pada
`lib/otp.py` ke versi WhatsApp yang sedang rilis, dan sesuaikan `User-Agent`.
Kalau `check` juga gagal total, berarti endpoint-nya yang pindah.

## `too_recent` terus-menerus
Normal, bukan error. Artinya nomor target sudah terkunci rate limit.
Itu justru tujuannya.

## Engine AUTO minta QR terus
Sesi ada di `lib/auth`. Pastikan folder itu tidak terhapus dan tidak masuk
`.gitignore` saat commit. Kalau `LOGGED OUT`, hapus `lib/auth` lalu login ulang.

## Pengiriman 90k char gagal di engine AUTO
Batas satu pesan WhatsApp 65.536 karakter. Pakai intensitas 4 (45k) untuk AUTO.
Mode INTENT aman sampai 90k karena lewat clipboard.

## Di Kali, link cuma tercetak di terminal
Tidak ada `xdg-open` atau tidak ada display server. `apt install xdg-utils`,
atau jalankan dengan `--no-open` dan salin URL-nya manual.
