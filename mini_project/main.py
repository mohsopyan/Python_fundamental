from utils import tools as t, formatter as f
from utils.models import User, Admin

from utils.tools import simpan_data, muat_data

data_mentah = muat_data()

user_objects = []

for item in data_mentah:
    if 'kode_akses' in item:
        obj = Admin(item['nama'], item['email'], item['level'], item['kode_akses'])
    else:
        obj = User(item['nama'], item['email'], item['level'])

    user_objects.append(obj)

for user in user_objects:
    print(user.sapa())

    if isinstance(user, Admin):
        print(user.hapus_data())

    print("-" * 30)

#print(t.sapa_user("Moyan"))

# pajak = 100000
#print(f"Pajak Anda: {t.hitung_pajak(pajak)}")
#print("Sistem tetap berjalan dengan aman...")

# user_level = "Expert"
# if t.cek_akses(user_level):
#     print("Akses Diberikan ke Dashboard Expert")
# else:
#     print("Akses di Tolak")

# profil = t.daftar_user("Moyan", "moyan@example.com")
#print(profil["nama"])

#print(f.cetak_header("Backend & AI Specialist"))

# user1 = User("Moyan", "moyan@example.com", 10)
# user2 = User("Budi", "budi@test.com", 5)
# user3 = User("Siti", "siti@test.com", 3)
# user4 = User("Robby", "robby@test", "sangat tinggi")

# print(user1.cek_status_akses())
# print(user2.sapa())
# print(user3.cek_status_akses())
# print(user4.cek_status_akses())

# admin1 = Admin("Moyan Expert", "admin@moyan.com", 10, "SECRET_99")

# print(admin1.sapa())
# print(admin1.hapus_data())

#semua_user = [user1, user2, admin1]
#print(simpan_data(semua_user))

