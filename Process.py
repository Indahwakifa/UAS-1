from DATA.celana import Celana
from PROCESS.Process import Proses
from VIEW.view import View

class Proses:
    def __init__(self):
        self.celana_list = []

    def input_celana(self):
        while True:
            try:
                nama = input("Masukkan nama celana: ")
                ukuran = input("Masukkan ukuran celana (S/M/L/XL): ")
                harga = float(input("Masukkan harga celana: "))
                jumlah = int(input("Masukkan jumlah yang terjual: "))

                if harga < 0 or jumlah < 0:
                    raise ValueError("Harga dan jumlah harus lebih besar atau sama dengan nol.")
                
                celana = Celana(nama, ukuran, harga, jumlah)
                self.celana_list.append(celana)
                print(f"Penjualan '{nama}' berhasil ditambahkan.")

                another = input("Apakah Anda ingin menambah penjualan lagi? (y/n): ")
                if another.lower() != 'y':
                    break
            except ValueError as e:
                print(f"Input tidak valid: {e}")

    def show_penjualan(self):
        if self.celana_list:
            View.display_penjualan(self.celana_list)
        else:
            print("Tidak ada data penjualan yang terdaftar.")
