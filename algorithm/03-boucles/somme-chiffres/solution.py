n = int(input("Donner un entier : "))

n = abs(n)
somme = 0

while n > 0:
    chiffre = n % 10
    somme = somme + chiffre
    n = n // 10

print("Somme des chiffres =", somme)