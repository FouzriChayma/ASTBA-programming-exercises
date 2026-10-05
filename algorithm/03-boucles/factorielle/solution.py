n = int(input("Donner un entier : "))

factorielle = 1

for i in range(1, n + 1):
    factorielle = factorielle * i

print(n, "! =", factorielle)