# 🛡️ OpenPort Scanner v1.0
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**OpenPort Scanner** adalah tools sederhana berbasis Python untuk memindai port yang terbuka pada alamat IP atau domain tertentu. Dilengkapi dengan fitur peringatan keamanan dan auto-push ke GitHub.

---

## 🚀 Fitur Utama
* **Fast Scanning**: Menggunakan library `socket` dengan optimasi timeout.
* **Security Alert**: Memberikan peringatan otomatis untuk port rawan (seperti Port 80, 443, dan 21).
* **Auto Logging**: Hasil scan otomatis disimpan ke dalam file `hasil_scan.txt`.
* **Auto GitHub Commit**: Mengunggah hasil pemindaian secara otomatis ke repository GitHub Anda.

## 🛠️ Cara Instalasi

1. **Clone repository ini:**
   ```bash
   git clone [https://github.com/arill2/open_portScanner.git](https://github.com/arill2/open_portScanner.git)
   cd open_portScanner
