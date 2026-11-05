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

