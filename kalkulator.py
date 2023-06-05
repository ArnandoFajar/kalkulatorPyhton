def tambah(angka1, angka2):
    return angka1 + angka2


def kurang(angka1, angka2):
    return angka1 - angka2


def kali(angka1, angka2):
    return angka1*angka2


def bagi(angka1, angka2):
    return angka1/angka2


def kalkulator():
    print("kalkulator Sederhana")
    print("Pilih Operasi :")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    angka1 = float(input("Masukkan Angka Pertama: "))
    angka2 = float(input("masukkan angka kedua: "))

    if pilihan == '1':
        hasil = tambah(angka1, angka2)
        operator = '+'
    elif pilihan == '2':
        hasil = kurang(angka1, angka2)
        operator = '-'
    elif pilihan == '3':
        hasil = kali(angka1, angka2)
        operator = 'x'
    elif pilihan == '4':
        hasil = bagi(angka1, angka2)
        operator = '/'

    print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")


kalkulator()
