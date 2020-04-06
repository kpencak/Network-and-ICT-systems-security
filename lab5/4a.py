from random import randint
from math import sqrt

def nwd(a, b):
    while b:
        a, b = b, a%b
    return a

pierwsze = 0
for i in range(100000):
    liczba1 = randint(1, 2147483647)
    liczba2 = randint(1, 2147483647)
    if (nwd(liczba1, liczba2) == 1):
        pierwsze += 1
    
odsetek = pierwsze/100000
pi = sqrt(6/odsetek)

print("Odsetek: ", odsetek)
print("PI: ", pi)