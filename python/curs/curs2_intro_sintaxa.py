#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 15:17:23 2026

@author: alex
"""

import math

luna = 13
permis = 1 <= luna <=12 
print(permis)

s1 = "Matematica"
s2 = "info"
s3 = """Prima
linie"""

print ("Ana" + " " "Pop")
print ("=" * 20)

print(len("Matematica"))
print("mat" in "Matematica")

s = "string"
s = 'A' + s[1:]
print (s)

s = "Matematica"
print(s[0])
print(s[4])
print(s[-1])
print(s[-3])

#slicing s[start:stop:pas]

print(s[0:4])
print(s[4:])
print(s[:4])
print(s[::2])

s ="Buna ziua! "
t = s.strip()
print(t)
t = s.upper()
print(t)
t = s.lower()
print(t)
t = s.replace('ziua','dimineata')
print(t)

x = 1

if x>0:
        print('pozitiv')
        print('si real')
print('mereu')

raza = float(input("raza: "))
pi = math.pi

aria = pi*raza**2
circum = 2*pi*raza

print(f"aria este: {aria:.4f} m patrati")
print(f"circumferinta este: {circum:.4f} m")

n = int(input("n: "))

if n == 0:
    print("n este 0")
else:
    if n > 0:
        semn = "pozitiv"
    elif n < 0:
        semn = "negativ"
    if n % 2:
        print(f"{n} este par si {semn}")
    else:
        print(f"{n} este impar si {semn}")
        
n = 100
suma = 0
for i in range(1, n+1):
    suma += i
print(suma)
print(n*(n+1) // 2)

for i in range(5, 0, -1):
    print(i, end = ' ')

for litera in "Math":
    print(litera)
    
a = int(input('a= '))
b = int(input('b= '))

while b != 0:
    a, b = b, a % b
print (f"cmmdc = {a}")

numar = int(input("numarul este "))
card = int(0)
while numar != 0:
    numar //= 10 #doua // inseamna /
    card = card +1
print (f"numarul de cifre al numarului este {card}")

x = int(input("x = "))
if x > 0:
    print("pozitiv")
    if x > 100:
        print("mare")
        

numar_intreg = 42
numar_real = 3.14159
numar_complex = 3 + 4j
text = "matematica"
adevarat = True

print(type(numar_intreg))
print(type(numar_real))
print(type(numar_complex))
print(type(text))
print(type(adevarat))

z1 = 3 + 4j
z2 = 1 - 2j

print(z1.real)
print(z1.imag)
print(abs(z1))
print(z1+z2)
print(z1*z2)
print(z1.conjugate())

n = int(input("Numar: "))
print(n+1)

nume = "Ana"
varsta = 20
medie = 9.75

print("Studentul " + nume + " are " + str(varsta) + " ani ")

print(f"Studentul {nume} are {varsta} ani.")

print(f"Peste 5 ani {nume} va avea {varsta + 5} ani.")

print(f"Dublul mediei este {2 * medie}")

pi = math.pi

print(f"pi = {pi:.2f}")
print(f"pi = {pi:.5f}")

numar_mic = 0.000001234
print(f"{numar_mic:.3e}")

n = 1000000
print(f"{n:,}")

p = 0.8765
print(f"{p:.1%}")

for i in range(1,6):
    print(f"{i:3d} | {i**2:5d} | {math.sqrt(i):.4f}")
    

x = float(input("Introdu un numar real: "))
if x > 0:
    print(f"{x} este pozitiv")
elif x < 0:
    print(f"{x} este negativ")
else:
    print("Numarul este zero")
    
n = 10
suma = 0
for i in range (1,n+1):
    suma += i
    
print(f"Suma 1+2+3+...+{n} = {suma}")
formula = n * (n + 1) // 2
print(f"Formula lui Gauss: n*(n+1)/2 = {formula}")


n = int(input("Introdu un numar intreg pozitiv: "))
nr_cifre = 0
temp = n

while temp > 0:
    temp //= 10
    nr_cifre += 1

print(f"Numarul {n} are {nr_cifre} cifre")

n = int(input("n: "))
for i in range(1,n+1):
    if type(math.sqrt(i)) == int(math.sqrt(i)):
        print(f"{i:3d} | {i**2}  | {math.sqrt(i):.8f}")