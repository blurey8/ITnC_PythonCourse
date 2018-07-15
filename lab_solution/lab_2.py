print("Rumus umum parabola: y = ax^2 + bx + c")
print()

# Input a, b, c
a = int(input("Masukkan nilai a : "))
b = int(input("Masukkan nilai b : "))
c = int(input("Masukkan nilai c : "))

# Print rumusnya
print()
print("Rumus parabola: y = ",a,"x^2 + ",b,"x + ",c, sep="")
print()

# Input x
x = int(input("Masukkan nilai x : "))
# Hitung nilai y
y = (a*(x**2)) + (b*x) + c

# Print nilai y
print("Nilai y pada x =",x,"adalah",y)

# BONUS
print()
print("Lihat gambar kurva di : (untuk a = 0 atau b = 0, gambar mungkin tidak akan keluar)")
print("https://www.google.com/search?q=",a,"x^2+%2B+",b,"x+%2B+",c, sep="")