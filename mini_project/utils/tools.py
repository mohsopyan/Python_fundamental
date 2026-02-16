def sapa_user(nama:str):
    return f"Halo {nama}, Selamat datang di sistem backend"

def hitung_pajak(harga: int):
    return harga * 0.1

def cek_akses(level: int):
    if level > 5:
        return True
    else:
        return False
    
def daftar_user(username:str, email:str):
    hasil = {
        "nama": username,
        "email": email
    }
    return hasil