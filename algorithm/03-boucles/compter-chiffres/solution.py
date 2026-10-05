n = int(input("Donner un entier : "))

n = abs(n)

if n == 0:
    nombre_chiffres = 1
else:
    nombre_chiffres = 0

    while n > 0:
        n = n // 10
        nombre_chiffres = nombre_chiffres + 1

print("Nombre de chiffres =", nombre_chiffres)