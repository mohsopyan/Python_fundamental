nilai_akademik = int(input("Masukan nilai akademik: "))

if nilai_akademik >=80:
    print("Nilai akademik cukup, Mengecek status ekonomi...")

    status_ekonomi = input("Apakah keluarga penerima bantuan? (ya/tidak): ")

    if status_ekonomi == "ya":
        print("Selamat! Anda berhak menerima Beasiswa Penuh")
    else:
        print("Maaf, beasiswa ini hanya untuk keluarga penerima bantuan.")
else:
    print("Maaf, nilai akademik Anda belum memenuhi syarat beasiswa.")