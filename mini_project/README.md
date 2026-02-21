# Simple Backend Logic System 🚀

Proyek ini adalah implementasi sistem backend sederhana menggunakan Python Modules dan Packages.

## Fitur Utama

### 1. Advanced OOP Architecture
- **Base Class `User`**: Standarisasi entitas user dengan enkapsulasi data.
- **Inheritance (Pewarisan)**: Class `Admin` yang mewarisi sifat `User` namun memiliki kapabilitas khusus.
- **Method Overriding**: Personalisasi perilaku fungsi berdasarkan peran user (User vs Admin).

### 2. Reliability & Integrity
- **Automated Validation**: Constructor class dilengkapi dengan `try..except` untuk menjamin tipe data `level` selalu valid (Integer).
- **Graceful Error Handling**: Sistem tetap berjalan (tidak crash) meskipun menerima input yang tidak terduga.

### 3. Modular System
- Struktur folder yang rapi memisahkan antara logika utilitas (`tools.py`) dan blueprint data (`models.py`).

## 📁 Struktur Proyek
- `main.py`: Entry point aplikasi.
- `utils/`: 
    - `models.py`: Berisi blueprint/class (`User` dan `Admin`).
    - `tools.py`: Berisi fungsi utility dan helper.

## Cara Menjalankan
```bash
python main.py
```
