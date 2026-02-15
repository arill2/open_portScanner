print("""WELCOME TO OPENPORT SCRIPT SCANNER BY MUH SYAHRIR HAMDANI""")

import socket

# 1. menentukan target IP 
TARGET_IP = input('masukkan target IP/DOMAIN:')
print(f'memulai scanning pada {TARGET_IP}')
print("-" * 30)
print("ini akan memindai port 1-100, agak lama sabar aja....")

# 2. melalukan looping untuk rentang port yang akan di scan
for port in range(1, 444):
    # membuat socket baru di setiap percobaan scan
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Durasi tunggu (semakin kecil semakin cepat, tapi kurang akurat)


    # mencoba koneksi
    result = s.connect_ex((TARGET_IP, port))

    if result == 0:
        print(f'[+]Port {port} terbuka')
    if {port} == 80 or port == 443:
        print(f'[!] Port {port} terbuka, ada kemungkinan di DDOS cek lebih lanjut!!')
    # menutup socket setelah digunakan
    s.close()

print("-" * 30)
print('scanning selesai')