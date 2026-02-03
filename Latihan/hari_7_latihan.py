username = input("Masukan username: ")

if username == "admin":
    print("Halo, Admin")

    password = int(input("password: "))

    if password == 12345:
        print("Akses Diberikan. Selamat Datang Admin!")
    else:
        print("Password Salah")
else:
    print("User tidak ditemukan!")