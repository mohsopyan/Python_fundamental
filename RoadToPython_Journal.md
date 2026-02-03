# 🐍 My Python Journey: From Zero to Backend Engineer

Jurnal ini mendokumentasikan proses belajar Python saya mulai dari nol, fokus pada logika backend dan standarisasi kode.

## 📊 Ringkasan Belajar (Log)

| Hari | Topik Utama | Key Tools / Fungsi | Status |
| :--- | :--- | :--- | :--- |
| 1 | Setup & Output | `print()`, VS Code Interpreter | ✅ Berhasil |
| 2 | Variabel | `f-string`, Variable Naming | ✅ Berhasil |
| 3 | Tipe Data & Casting | `type()`, `int()`, `str()`, `bool` | ✅ Berhasil |
| 4 | Input & Operator | `input()`, `*`, `//`, `%` | ✅ Berhasil |
| 5 | String Manipulation | .upper(), .title(), len(), in | ✅ Selesai |
| 6 | Percabangan Logic | and, or, if-elif-else | ✅ Berhasil |
| 7 | Nested IF | if inside if (Logic levels) | ✅ Berhasil |

---

## 💡 Pelajaran Penting (Key Takeaways)

### 🔹 Fondasi & String
- **Interpreter:** Mesin "penerjemah" Python di VS Code (Set via `Ctrl+Shift+P`).
- **F-String:** Cara termudah menggabungkan teks dan variabel: `f"Halo {nama}"`.
- **String Methods:** - `.upper()` (Kapital semua), `.title()` (Besar di awal kata).
    - `len()` (Hitung panjang karakter), `in` (Cek keberadaan kata).

### 🔹 Penanganan Error & Logika
- **Casting:** Ingat bahwa `input()` selalu menghasilkan String. Gunakan `int()` untuk angka.
- **Math Operators:** `/` (Desimal), `//` (Bulat), `%` (Sisa bagi).
- **Logical Operators:** - `if-elif-else`: Mengambil keputusan berdasarkan kondisi.
    - `and`: Semua syarat harus benar.
    - `or`: Salah satu syarat benar sudah cukup.
- **Nested IF (Logika Bersarang)**
    - Digunakan untuk validasi bertahap.
    - Blok kode di dalam `if` kedua harus memiliki indentasi ekstra (2x Tab/4x Spasi).
    - Struktur: Mengecek kondisi luar dulu, baru masuk ke kondisi dalam.

### 🔹 Best Practices
- **Indentasi:** Spasi/Tab setelah tanda titik dua `:` pada `if` adalah wajib untuk menentukan blok kode.
- **Git Flow:** Selalu cek `git status` sebelum `add`, `commit`, dan `push`.

### 🔹 Masalah & Solusi
- **TypeError:** Muncul jika mencampur `str` dan `int`. Solusi: Ubah salah satu tipe datanya agar seragam.