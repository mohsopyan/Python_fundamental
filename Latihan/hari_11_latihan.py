# Inisialisasi dafatar karyawan
karyawan = ["Moyan", "Budi", "Siti"]

# 1. Menambah data (Append)
karyawan.append("Agus")

# 2. Mengubah data
karyawan[1] = "Budi Santoso"

# 3. Menghapus data berdasarkan nilai
karyawan.remove("Siti")

# 4. Menghitung jumlah data
jumlah_karyawan = len(karyawan)

print(f"Data Terupdate: {karyawan}")
print(f"Total Karyawan: {jumlah_karyawan}")