def proses_gambar(nama_file:str, format_output:str ="png"):
    return f"Memproses file {nama_file} ke format {format_output}"

print(proses_gambar("profil_user"))  
print(proses_gambar("data_ai", "jpeg"))

def kirim_notifikasi(pesan:str, metode:str = "Email", prioritas:str = "Normal"):
    return f"Mengirim pesan {pesan} via {metode} dengan prioritas {prioritas}"

print(kirim_notifikasi("server down", "sms"))