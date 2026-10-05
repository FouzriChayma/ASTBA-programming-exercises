a = int(input("Donner a : "))
b = int(input("Donner b : "))
c = int(input("Donner c : "))

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

print("Le maximum est :", maximum)