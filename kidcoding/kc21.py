import math

nama = input("Masukkan nama anda: ")
print("Nama anda:", nama)

# Menghitung luas lingkaran
print(nama, "akan menghitung luas lingkaran :")
radius = input("Masukkan radius dari lingkaran : ")
radius = int(radius)
print("Luas lingkaran adalah pi * r * r = ", math.pi * (radius ** 2))
