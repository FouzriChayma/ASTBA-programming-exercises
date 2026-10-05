a = int(input("Donner la base : "))
n = int(input("Donner l'exposant : "))

resultat = 1

for i in range(n):
    resultat = resultat * a

print("Résultat =", resultat)