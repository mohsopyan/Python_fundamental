total_price = int(input("Masukan total belanja anda: "))
member_card = input("Apakah anda memiliki kartu member?")

if total_price >= 100000 and member_card == "ya":
    print("Anda mendapat discount 20%")
elif total_price >= 100000 and member_card == "tidak":
    print("Anda medapat discount 5%")
else:
    print("Terimakasih sudah berbelanja")