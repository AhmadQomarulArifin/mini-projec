while True:
    print(" Selamat datang di indomaret Sultan ")
    Nama = (input("Masukkan Nama:"))
    kosong = (input(""))
    Nim = (input("Masukkan Nim:"))
    kosong = (input(""))
    print(f"Hai {Nama}, kamu berhasil login!\n")
    
    # Input harga barang dan jumlah pembelian
    harga_barang = float(input("Masukkan harga barang: Rp. "))
    print("")
    jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))

    # Menghitung total harga sebelum diskon
    total_harga = harga_barang * jumlah_pembelian

    # Menentukan apakah total harga lebih dari Rp. 250.000 dan memberikan diskon
    if total_harga > 250000:
        total_harga *= 0.75  # Memberikan diskon 25%
        print("Anda mendapatkan diskon 25%")
        print(f" uang yang anda keluarkan dari dompet anda yaitu sebesar: Rp. {total_harga:.2f}")
    else:
        print("maaf sekali anda kurang beruntung")
        print(f"uang yang anda keluarkan dari dompet anda yaitu sebesar: Rp. {total_harga:.2f}")
        

    # Menanyakan apakah ingin menghitung lagi atau keluar
    pilihan = input("Apakah ingin menghitung lagi? (ya/tidak): ").lower()
    if pilihan != "ya":
        print("Terima kasih telah berkunjung di indomaret sultan.")
        break
