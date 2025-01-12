class Celana:
    def __init__(self, nama, ukuran, harga, jumlah):
        self.nama = nama
        self.ukuran = ukuran
        self.harga = harga
        self.jumlah = jumlah

    def get_info(self):
        return {
            'Nama': self.nama,
            'Ukuran': self.ukuran,
            'Harga': self.harga,
            'Jumlah': self.jumlah,
            'Total Penjualan': self.harga * self.jumlah
        }


class View:
    @staticmethod
    def display_penjualan(celana_list):
        print("\nDaftar Penjualan Celana:")
        print("{:<20} {:<10} {:<10} {:<10} {:<15}".format("Nama", "Ukuran", "Harga", "Jumlah", "Total"))
        print("-" * 70)
        for celana in celana_list:
            info = celana.get_info()
            print("{:<20} {:<10} {:<10} {:<10} {:<15}".format(info['Nama'], info['Ukuran'], info['Harga'], info['Jumlah'], info['Total Penjualan']))
        print("-" * 70)


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


if __name__ == "__main__":
    proses = Proses()
    proses.input_celana()
    proses.show_penjualan()
