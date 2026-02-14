def buat_profil(nama:str, *hobi:str, **info_tambahan):
    print(f"Nama: {nama}")
    for item in hobi:
        print(f"Hobi: {item}")
    for key, value in info_tambahan.items():
        print(f"info {key} adalah {value}")

print("Profil")
buat_profil("Moyan", "Coding", "Gaming", kota="Jakarta", role="Backend")

def hitung_stok(nama_barang:str, *jumlah:int):
    total = sum(jumlah)
    return f"Total stok {nama_barang} adalah {total}"

result = hitung_stok("Galvanis", 4, 10, 15)
print(result)