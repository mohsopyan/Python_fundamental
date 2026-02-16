from utils import tools as t, formatter as f

print(t.sapa_user("Moyan"))
print(f"Pajak Anda: {t.hitung_pajak(100000)}")

user_level = 10

if t.cek_akses(user_level):
    print("Akses Diberikan ke Dashboard Expert")
else:
    print("Akses di Tolak")

profil = t.daftar_user("Moyan", "moyan@example.com")
print(profil["nama"])

print(f.cetak_header("Backend & AI Specialist"))