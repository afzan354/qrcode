import os
import pandas as pd
import qrcode
from PIL import Image
from colorama import Fore, Style, init

# Inisialisasi Colorama
init()

# Tampilan ASCII dengan warna
def print_ascii_art():
    ascii_art = f"""
  {Fore.GREEN}___  ____     ____ ___  ____  _____
 / _ \|  _ \   / ___/ _ \|  _ \| ____|
| | | | |_) | | |  | | | | | | |  _|
| |_| |  _ <  | |__| |_| | |_| | |___
 \__\_\_| \_\  \____\___/|____/|_____|{Style.RESET_ALL}"""
    print(ascii_art)
    print(f"\n{Fore.MAGENTA}Powered By Afzan & Chat GPT{Style.RESET_ALL}")

# Proses pembuatan QR code
def generate_qr_code(excel_file, logo_file, folder_name):
    # Membuat folder jika belum ada
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Membaca file Excel
    try:
        data = pd.read_excel(excel_file, header=None)
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        return

    # Membuka logo
    try:
        logo = Image.open(logo_file)
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        return

    # Membuat QR code dari kolom nomor pokok (kolom B - indeks 1)
    for index, row in data.iterrows():
        nomor_pokok = str(row[1])  # Mengakses kolom B (indeks 1)
        nama_file_qr = os.path.join(folder_name, f'qr_{row[0]}.png')  # Nama file QR code

        # Membuat QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # Menggunakan error correction lebih tinggi
            box_size=10,
            border=4,
        )
        qr.add_data(nomor_pokok)
        qr.make(fit=True)

        # Membuat gambar QR code
        img_qr = qr.make_image(fill='black', back_color='white').convert('RGB')

        # Mengatur ukuran logo agar proporsional dengan QR code
        logo_size = int(img_qr.size[0] * 0.25)  # 25% dari ukuran QR code
        logo_resized = logo.resize((logo_size, logo_size), Image.LANCZOS)

        # Menempatkan logo di tengah QR code
        pos = ((img_qr.size[0] - logo_size) // 2, (img_qr.size[1] - logo_size) // 2)

        # Menempatkan logo pada QR code
        if logo_resized.mode in ('RGBA', 'LA'):
            logo_transparency = logo_resized.split()[-1]  # Mengambil channel transparansi (A)
            img_qr.paste(logo_resized, pos, mask=logo_transparency)  # Menggunakan transparansi logo
        else:
            img_qr.paste(logo_resized, pos)  # Jika tidak ada transparansi, langsung paste

        # Menyimpan gambar QR code dengan logo
        img_qr.save(nama_file_qr)
        print(f"{Fore.GREEN}{row[0]} => {row[1]} sukses{Style.RESET_ALL}")

    print(f"\n{Fore.GREEN}QR Code Generator telah selesai{Style.RESET_ALL}")

# Fungsi utama
def main():
    while True:
        print_ascii_art()

        # Input nama file Excel
        excel_file = input("\nNama file Excel: ")
        # Input nama file logo
        logo_file = input("Nama file logo: ")
        # Input nama folder untuk menyimpan gambar
        folder_name = input("Nama folder: ")

        # Jalankan proses pembuatan QR code
        generate_qr_code(excel_file, logo_file, folder_name)

        # Menunggu konfirmasi untuk kembali ke menu home
        choice = input(f"{Fore.YELLOW}Tekan 0 untuk kembali ke halaman home atau 1 untuk keluar: {Style.RESET_ALL}")
        if choice != '0':
            break

if __name__ == "__main__":
    main()
