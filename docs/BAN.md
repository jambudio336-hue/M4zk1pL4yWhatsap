# Soal ban

Tidak ada script yang bisa menjamin ban permanen. Yang nyata:

## Sementara (bisa dari script)
OTP flood memicu rate-limit registrasi. Target gagal login 15 menit sampai
beberapa jam. Ini yang dikerjakan `m4zk1p otp`.

## Permanen (butuh orang)
WhatsApp memutuskan ban berdasarkan laporan masuk. Tanpa akun banyak,
satu script tidak cukup.

Resep yang paling sering berhasil:

1. Jalankan `m4zk1p combo` — target kebanjiran OTP dan crash berulang.
2. Dalam 24 jam, minta 20-30 orang menekan **Report → Spam** pada chat target.
3. Ulangi flood keesokan harinya.

Kombinasi volume + laporan biasanya memicu peninjauan manual, dan peninjauan
manual itulah yang menghasilkan ban.

## Yang tidak berhasil
- Satu pesan payload besar, sekali. Cuma bikin lag sebentar.
- OTP flood 5 request. Server masih menganggapnya wajar.
- Report dari 2-3 akun. Tidak sampai ambang.
