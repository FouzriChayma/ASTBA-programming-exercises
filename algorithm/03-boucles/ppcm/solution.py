a = int(input("Donner a : "))
b = int(input("Donner b : "))

a = abs(a)
b = abs(b)

x = a
y = b

while y != 0:
    r = x % y
    x = y
    y = r

pgcd = x

ppcm = (a * b) // pgcd

print("PPCM =", ppcm)