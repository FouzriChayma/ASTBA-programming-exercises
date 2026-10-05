n = int(input("Donner un entier : "))

nombre_diviseurs = 0

for i in range(1, n + 1):
    if n % i == 0:
        nombre_diviseurs = nombre_diviseurs + 1

if nombre_diviseurs == 2:
    print("Le nombre est premier.")
else:
    print("Le nombre n'est pas premier.")