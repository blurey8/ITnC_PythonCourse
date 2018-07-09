# Import math [BONUS]
import math

# Minta input jari-jari
jari_jari = int(input("Masukkan jari-jari lingkaran : "))

# Masukkan nilai jari-jari tersebut ke dalam rumus luas dan keliling
# kemudian tampung hasilnya ke dalam variable
luas = math.pi * (jari_jari**2)
keliling = math.pi * 2 * jari_jari

# Cetak hasilnya
print()
print("Luas lingkaran tersebut adalah",luas,\
"dan panjang kelilingnya adalah",keliling)