# Simple Backend Logic System

Proyek ini adalah implementasi sistem backend sederhana menggunakan Python Modules dan Packages.

## Fitur Utama
- **Object-Oriented User Model**: Menggunakan Class `User` untuk standarisasi data entitas.
- **Reliability & Safety**: Proteksi `try...except` di dalam constructor Class untuk menjamin integritas data.
- **Access Control**: Logika pengecekan akses yang tertanam (encapsulated) dalam objek User.
- **Modular Structure**: Pemisahan antara logika pendukung (`tools.py`) dan cetakan data (`models.py`).

## Struktur Proyek
- `main.py`: Entry point aplikasi.
- `utils/`: 
    - `models.py`: Berisi blueprint/class (User, dll).
    - `tools.py`: Berisi fungsi utility dan helper.

## Cara Menjalankan
```bash
python main.py
```
