Berikut adalah penjelasan rinci tentang kode Python yang Anda berikan, yang merupakan implementasi sistem pelacakan penjualan celana. Kode ini dibagi menjadi beberapa kelas, masing-masing dengan tanggung jawab tertentu.

## 1. Kelas Celana

### Deskripsi
Kelas Celana digunakan untuk merepresentasikan sebuah item celana yang memiliki beberapa atribut:

- *Nama*: Nama dari celana.
- *Ukuran*: Ukuran celana (misalnya S, M, L, XL).
- *Harga*: Harga per unit celana.
- *Jumlah*: Jumlah celana yang terjual.

### Metode
- *__init__*: Konstruktor yang menginisialisasi atribut kelas.
- *get_info*: Mengembalikan informasi tentang celana dalam bentuk dictionary, termasuk total penjualan yang dihitung dengan mengalikan harga dengan jumlah.

python
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


## 2. Kelas View

### Deskripsi
Kelas View bertanggung jawab untuk menampilkan informasi penjualan. Kelas ini menggunakan metode statis sehingga tidak perlu membuat instance dari kelas ini untuk menggunakannya.

### Metode
- *display_penjualan*: Menerima daftar objek Celana dan mencetak informasi penjualan dalam format tabel. Ini mencetak nama, ukuran, harga, jumlah, dan total penjualan untuk setiap item celana.

python
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


## 3. Kelas Proses

### Deskripsi
Kelas Proses menangani logika bisnis untuk mengelola daftar penjualan celana. Kelas ini memiliki metode untuk memasukkan data penjualan dan menampilkan daftar penjualan.

### Atribut
- *celana_list*: Daftar untuk menyimpan objek Celana.

### Metode
- *input_celana*: Mengambil input dari pengguna untuk menambahkan celana baru ke dalam daftar. Ini menggunakan loop untuk terus meminta input hingga pengguna memilih untuk berhenti. Metode ini juga menangani validasi input.
- *show_penjualan*: Menampilkan daftar penjualan jika ada data yang terdaftar; jika tidak ada, akan memberi tahu pengguna bahwa tidak ada data.

python
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


## 4. Bagian Utama (if __name__ == "__main__":)

Bagian ini adalah titik awal eksekusi program. Di sini, instance dari kelas Proses dibuat dan metode untuk memasukkan dan menampilkan penjualan dipanggil.

python
if __name__ == "__main__":
    proses = Proses()
    proses.input_celana()
    proses.show_penjualan()


### Penjelasan Akhir

Program ini secara keseluruhan berfungsi sebagai alat sederhana untuk mencatat dan menampilkan informasi tentang penjualan celana. Pengguna dapat memasukkan data penjualan melalui input konsol dan melihat ringkasan penjualannya dalam format tabel setelah selesai memasukkan data. Validasi input juga ditangani untuk memastikan bahwa harga dan jumlah tidak negatif. 

Sistem ini dapat diperluas lebih lanjut dengan menambahkan fitur seperti penyimpanan data yang sudah ada, atau laporan analisis penjualan berdasarkan waktu atau kategori produk.
