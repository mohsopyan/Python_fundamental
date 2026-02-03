#.title() agar input user selalu cocok ketika user input "ya", "YA", "Ya"
driver = input("Apakah Anda memiliki SIM? (Ya/Tidak)").title()

if driver == "Ya":
    print("Berapa umur Anda?")

    umur = int(input("Umur: "))
    if umur >= 17:
        print("Anda diizinkan mengemudi.")
    else:
        print("Umur tidak cukup, SIM anda invalid")
else:
    print("Silakan membuat SIM terlebih dulu")