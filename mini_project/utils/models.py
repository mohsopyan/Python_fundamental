class User:
    def __init__(self, nama: str, email: str, level: int):
        self.nama = nama
        self.email = email

        try:
            self.level = int(level)
        except ValueError:
            self.level = 0
            print(f"Peringatan: Level untuk {nama} tidak valid, diset ke 0")
            
    def sapa(self):
        return f"Halo, saya {self.nama}, Email saya {self.email}."
    
    def cek_status_akses(self):
        if self.level > 5:
            return f"User {self.nama} memilik akses EXPERT."
        else:
            return f"User {self.nama} hanya memiliki akses STANDARD."