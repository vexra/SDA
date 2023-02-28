cmd = "Y"

while cmd == "Y":
    print("\nKalkulator Duo")
    print("Pilih menu 1 sd 4:")
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Pengurangan")
    print("4. Pembagian\n")

    menu = int(input("masukan menu: "))
    bilangan1 = int(input("masukan bilangan pertama: "))
    bilangan2 = int(input("masukan bilangan kedua: "))

    if menu == 1:
        print("Hasil dari {} + {} = {}".format(bilangan1, bilangan2, bilangan1+bilangan2))
    elif menu == 2:
        print("Hasil dari {} kali {} = {}".format(bilangan1, bilangan2, bilangan1*bilangan2))
    elif menu == 3:
        print("Hasil dari {} - {} = {}".format(bilangan1, bilangan2, bilangan1-bilangan2))
    elif menu == 4:
        print("Hasil dari {} bagi {} = {}".format(bilangan1, bilangan2, bilangan1/bilangan2))
    else:
        print("Menu not found. Program Exit")
        break

    cmd = input("\nPress Y to continue. or N to exit ")

    

