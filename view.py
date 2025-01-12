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
