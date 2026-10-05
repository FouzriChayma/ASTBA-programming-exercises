a = int(input("Donner a : "))
b = int(input("Donner b : "))

a = abs(a)
b = abs(b)

while b != 0:
    r = a % b
    a = b
    b = r

print("PGCD =", a)