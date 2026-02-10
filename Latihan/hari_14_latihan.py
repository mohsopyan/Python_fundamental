ai_output = {
    "objek": "Mobil",
    "akurasi": 0.95,
    "warna": "Merah"
}
print(f"AI Mendeteksi {ai_output['objek']} dengan akurasi {ai_output['akurasi'] * 100}%")

ai_output["lokasi"] = (10, 50)
print(f"Data update: {ai_output}")