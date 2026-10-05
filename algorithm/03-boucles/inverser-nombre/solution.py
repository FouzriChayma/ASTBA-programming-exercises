n = int(input("Donner un entier : "))

signe = 1

if n < 0:
    signe = -1
    n = -n

inverse = 0

while n > 0:
    chiffre = n % 10
    inverse = inverse * 10 + chiffre
    n = n // 10

inverse = inverse * signe

print("Nombre inversé =", inverse)