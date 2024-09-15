QR Code Generator dengan Logo
Ini adalah alat untuk menghasilkan QR Code dari data yang diambil dari file Excel, dengan opsi untuk menambahkan logo di tengah QR Code. Alat ini juga memberikan tampilan antarmuka terminal dengan warna untuk informasi dan status.

Syarat Menjalankan
Python: Pastikan Python 3.6 atau versi lebih baru terinstal di sistem Anda.

Pustaka Python: Anda perlu menginstal beberapa pustaka Python. Daftar pustaka yang diperlukan:

pandas: Untuk membaca file Excel.
qrcode: Untuk menghasilkan QR Code.
Pillow: Untuk manipulasi gambar, termasuk menambahkan logo pada QR Code.
colorama: Untuk pewarnaan teks di terminal.
File Excel: File Excel dengan data yang akan diubah menjadi QR Code. File ini harus memiliki dua kolom:

Kolom A: Nama
Kolom B: Nomor pokok (data yang akan dimasukkan ke dalam QR Code)
File Logo: Gambar logo dalam format .png atau .jpg yang akan ditambahkan ke tengah QR Code.

Folder Output: Tempat di mana gambar QR Code akan disimpan.

Use:
pip install pandas qrcode[pil] Pillow colorama


python qr4.py
