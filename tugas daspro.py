
def login():
    print("=== Selamat datang di indomaret Sultan ===")
    nama = input(" NAMA:")
    nim =input(" NIM: ")
    print(f"Hai {nama}, kamu berhasil login!\n")

def hitung_total_harga() :

    try:
        harga_per_barang = float(input("Harga barang: Rp"))
        jumlah_barang = int(input("Jumlah barang yang dibeli:"))
    except ValueError:
        print("input salah, silahkan memasukkan angka.")
        return None
        
    total_harga = harga_per_barang * jumlah_barang

    if total_harga > 250000:
        diskon = 0.25
        total_harga_setelah_diskon = total_harga - (total_harga * 0.25)
        print(f"Total harga sebelum diskon: Rp {total_harga:.2f}")
        print(f"Anda mendapatkan diskon sebesar 25%!")
        print(f"Total harga setelah diskon: Rp {total_harga_setelah_diskon:.2f}")
    else:
        print(f"Total harga: Rp {total_harga:.2f}")
        print(f"Maaf sekali anda tidak mendapatkan diskon")

def main():
    login()
    while True:
        hitung_total_harga()

        pilihan = input("Apakah anda ingin menghitung total harga lagi? (y/n):")
        if pilihan != 'y':
            print("terima kasih telah mengunjungi toko kami !")
            break


main()