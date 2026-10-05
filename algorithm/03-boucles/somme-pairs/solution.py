n = int(input("Donner n : "))

somme = 0

for i in range(2, n + 1, 2):
    somme = somme + i

print("Somme des nombres pairs =", somme)