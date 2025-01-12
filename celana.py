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
