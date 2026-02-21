import json

def simpan_data(list_user, filename="database.json"):
    try:
        data_to_save = []
        for u in list_user:
            data_to_save.append(u.__dict__)

        with open(filename, "w") as file:
            json.dump(data_to_save, file, indent=4)
        print(f"✅ Data berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"❌ Gagal menyimpan data: {e}")

def muat_data(filename="database.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Peringatan: File database tidak ditemukan.")
        return []

def sapa_user(nama:str):
    return f"Halo {nama}, Selamat datang di sistem backend"

def hitung_pajak(harga: int):
    try:
        return harga * 0.1
    except TypeError:
        return "Error: Harga harus berupa angka (int/float)!"

def cek_akses(level: int):
    try:
        if level > 5:
            return True
        else:
            return False
    except (TypeError, Exception):
        print("Log: Input level tidak valid!")
        return False
    finally:
        print("Pengecekan selesai.")
    
def daftar_user(username:str, email:str):
    hasil = {
        "nama": username,
        "email": email
    }
    return hasil