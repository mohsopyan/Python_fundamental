# 1. Contoh *args (Menampung banyak nilai sekaligus)
def cetak_daftar_sensor(*sensor: str):
    print(f"Tipe data args: {type(sensor)}")
    for item in sensor:
        print(f"Aktifkan Sensor: {item}")

# 2. Contoh **kwargs (Menampung banyak label/konfigurasi)
def konfigurasi_ai(**setting):
    print(f"Tipe data kwargs: {type(setting)}")
    for key, value in setting.items():
        print(f"Setting {key} diatur ke: {value}")

# --- Eksekusi ---
print("--- TEST ARGS ---")
cetak_daftar_sensor("Kamera Depan", "Lidar", "Ultrasonik")

print("\n--- TEST KWARGS ---")
konfigurasi_ai(model="YOLOv8", threshold=0.5, device="GPU")