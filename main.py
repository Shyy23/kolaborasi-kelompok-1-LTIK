"""
Projek kolaborasi sederhana Kelompok 1
RPL Kelas 1C

Kalkulator Sederhana
"""
import operator as op

# Variabel Global
pembatas = "="*30

# Fungsi Operator
def operator(pilihan):
    if pilihan == 1:
        return op.add
    elif pilihan == 2:
        return op.sub
    elif pilihan == 3:
        return op.mul
    elif pilihan == 4:
        return op.truediv
    elif pilihan == 5:
        return op.mod
    elif pilihan == 6:
        return op.pow

# Fungsi Kalkulator
def kalkulator(operator):
    angka1 = int(input("Masukkan Angka Pertama: "))
    angka2 = int(input("Masukkan Angka Kedua: "))
    hasil = operator(angka1, angka2)
    return hasil

# Sistem Kalkulator Sederhana 


print(pembatas)
print("Selamat Datang!! di SiKaSeh")
print("( Sistem Kalkulator Sederhana )")
print(pembatas)

print("Apa yang ingin anda Lakukan?")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Modulus")
print("6. Pangkat")
print("7. Keluar")

# Logika Kalkulator
while True:
    pilihan = int(input("Masukan pilihan no menu (1-7) diatas: "))

    if pilihan == 7:
        print(pembatas)
        print("Terimakasih & Sampai Jumpa!")
        print(pembatas)
        break

    elif pilihan in [1,2,3,4,5,6]:
        operasi = operator(pilihan)
        print(pembatas)
        print(f"Hasil: {kalkulator(operasi)}")
        print(pembatas)
        input("Tekan ENTER untuk mencoba lagi...")

    else:
        print(pembatas)
        print("Pilihan tidak valid! maukan (1-7)")
        print(pembatas)
        input("Tekan ENTER untuk mencoba lagi...")
