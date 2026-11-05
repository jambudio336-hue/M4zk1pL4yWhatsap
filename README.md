<div align="center">

<img src="assets/banner.svg" alt="M4zk1pL4yWhatsap" width="900">

**Brutal WhatsApp stress toolkit.**

Payload delay · force-close loop · OTP flood

[![ci](https://github.com/USERNAME/M4zk1pL4yWhatsap/actions/workflows/ci.yml/badge.svg)](../../actions)
[![versi](https://img.shields.io/badge/versi-2.0.0-25d366)](CHANGELOG.md)
[![lisensi](https://img.shields.io/badge/lisensi-MIT-blue)](LICENSE)
[![platform](https://img.shields.io/badge/platform-termux%20%7C%20kali%20%7C%20debian-555)](#instalasi)
[![python](https://img.shields.io/badge/python-3.8%2B-3776ab)](requirements.txt)

</div>

---

## Apa ini

Satu CLI untuk menekan nomor WhatsApp dari terminal. Tiga vektor serang:
payload yang membekukan antarmuka, payload yang memicu crash berulang, dan
flood OTP ke endpoint registrasi.

Jalan di **Termux (Android)** dan **Kali/Debian**. Di Android, payload dikirim
lewat intent ke aplikasi WhatsApp. Di Linux, lewat `wa.me` ke WhatsApp Web.
