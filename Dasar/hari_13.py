# Membuat Tuple (Backend Config)
config_server = ("192.168.1.1", 8080, "admin")

# Mengakses data (sama dengan list)
print(f"IP Addres: {config_server[0]}")
print(f"Port: {config_server[1]}")

# Percobaan mengubah data (Akan Error!)
# config_server[1] = 9090 -> Jika baris ini diaktifkan, program akan crash