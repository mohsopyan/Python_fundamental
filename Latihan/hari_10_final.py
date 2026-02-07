while True:
    print("\n--- Sistem Gudang ---")
    pilihan = input("1. Tambah\n2. Keluar\nPilih: ")

    if pilihan == "1":
        nama = input("Nama Barang: ")
        stok = input("Jumlah: ")
        print(f"Berhasil: {nama} sejumlah {stok} ditambahkan.")
    elif pilihan == "2":
        print("Sistem dimatikan...")
        break
    else:
        print("pilihan tidak valid")