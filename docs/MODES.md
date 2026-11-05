# Mode

## delay
Payload karakter tak terlihat: Hangul filler `U+3164`, zero-width space `U+200B`,
atau string alfanumerik tanpa spasi. WhatsApp dipaksa mengukur dan membungkus
puluhan ribu karakter yang tidak punya titik patah. UI thread kejebak.
Di perangkat 3-4 GB RAM: freeze 5-20 detik, kadang ANR.

Efektif bila dikirim berulang (10-30 pesan), bukan sekali.

## crash
Zalgo — sampai ~1300 combining mark `U+0300`–`U+036F` per huruf. Setiap kali
target membuka chat, rasterizer harus menggambar ribuan mark per glyph.
Alokasi memori render meledak, proses di-kill sistem, target membuka lagi,
payload masih ada di layar, mati lagi. Itu loop-nya.

Kirim 5-10 varian berbeda. Satu varian saja biasanya cuma bikin patah-patah.

## crash2
Override RTL `U+202E`/`U+202C` berulang. Memaksa reflow bidirectional terus
menerus. Lebih ringan dari Zalgo, tapi menjengkelkan di teks panjang.

## otp
Menyerang `v.whatsapp.net/v2/code`, endpoint registrasi. Setiap request memakai
identitas perangkat baru sehingga server menganggapnya perangkat lain dan
mengirim OTP lagi.

Hasil: target kebanjiran SMS/kontak suara, nomor kena rate-limit, OTP asli
nyangkut, gagal login 15 menit sampai beberapa jam.

## combo
OTP flood di background + payload crash di foreground. Kombinasi paling
maksimal yang bisa dicapai tanpa botnet akun.
