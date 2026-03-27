#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:16:17 2026

@author: alex
"""
import numpy as np

#ndarray

def delimit(i):
    print(" ")
    print(f"-({i})-" + 48*"-")

delimit(0)


x = [1, 2, 3, 4]

# fara numpy
rez = []
for t in x:
    rez.append(t*t + 1)
print(rez)

# cu numpy
x = np.array([1, 2, 3, 4])
rez = x * x + 1
print(rez)

delimit(1)


a = np.array([1, 2, 3])
b = np.zeros(4) # 4 zerouri

print(np.mean(a))

a = np.array([1, 2, 3, 4])
print(a)
print(type(a)) #ndarray

delimit(2)


A = np.array([[1,2,3],
              [4,5,6]])
print(A)
print(A.shape)
print(A.ndim)

delimit(3)


L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2) #concatenare

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b) #adunare vectoriala

print(L1*2) #dublare lista
print(a*2) #inmultire cu scalar

delimit(4)


a = np.array([1, 2, 3])
b = a * a + 1
print(a)
print(b)

delimit(5)


a = np.array([[1, 2, 3]]) #matrice de o linie si 3 coloane
print(a.shape) #(linii, coloane)
a = np.array([1,2,3]) # matrice de 3 linii si '0' coloane
# a doua forma e transpusa primei si viceversa
print(a.shape)

b = a + a + 1 # exhivalent cu b = 2*a + 1

print(a)
print(b)
print(b-a)

delimit(6)


c = np.array([[1,2,3],
             [4,5,6]])

print(c)
print(c.shape)

delimit(7)


lista = [1,2,3]
#print(lista  + 1 ) # EROARE
lista2 = [1]
print(lista + lista2) #corect
print(lista + [6]) # corect

delimit(8)


x = [0,1,2,3]
y = []
for t in x:
    y.append(t**2 + 1)
print(y) #explicit

y = [t**2 + 1 for t in x]
print(y) #list comprehensions

x = np.array([0,1,2,3])
y = x**2 + 1 #array in numpy
print(y)

# echivalente ^

delimit(9)


a = np.array([10,20,30,40])
print(a)
print(a.shape) # 4 linii 1 col (4,)
print(a.size) # numarul de elemente
print(a.dtype) # tipul elementelor i.e. int64
print(a.ndim) # numarul de dimensiuni ale array-ului

delimit(10)


c = np.array([[1,2,3],
             [4,5,6]])

print(c)
print(c.shape)
print(c.size)
print(c.dtype)
print(c.ndim)

delimit(11)


#tip date int si float
a = np.array([1, 2, 3])
b = np.array([1., 2., 3.])
b_1 = np.array([1., 2, 3.])

print(a.dtype)
print(b.dtype)
print(b_1.dtype)

delimit(12)


a = np.zeros(5) # 5 zerouri
b = np.ones(4) # 4 de 1
c = np.arange(0, 10, 2) # A RANGE de la 0 la 10 din 2 in 2 (pas);
                        # 10 nu e luat in calcul
d = np.linspace(0, 1, 5) # multime de la 0 la 1 cu 5 elemente echidistante
        # se foloseste pentru a crea domeniul unei functii pe interval
print(a)
print(b)
print(c)
print(d)

delimit(13)


# operatii vectorizate

a = np.array([1,2,3])
print(a + 1)
print(a - 1)
print(a / 2)
print(a // 2)
print(2 * a)

b = np.array([4,5,6])

print(a + b)
print(b - a)
print(b / a)
print(a * b)

c = np.array([1,2,3])
d = np.array([10,20])
#print(c+d) # EROARE, array-urile trebuies sa fie de marime egala

delimit(14)


a = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print(np.sin(a))
print(np.cos(a))
#face aproximari a lui pi si deci cos(pi/2) nu e exact 0

delimit(15)


y = np.array([1,1,4,9,16,16])
print(np.sqrt(y))

print(np.min(y))
print(np.max(y))
print(np.argmin(y)) # prima pozitie la care apare min
print(np.argmax(y)) # prima pozitie la care apare max
                    # indexate de la 0
print(np.where(y == np.min(y)))
#gaseste toate pozitiile la care se gaseste elementul care
#satisface conditia ex. min
print(np.sum(y)) # suma
print(np.mean(y)) # media
print(np.std(y)) # eroarea medie statistica

n = np.array([-1,-1,-4,-9,-16,-16,1,1,4,9,16,16])
print(np.abs(n)) # modul

a = np.array([4,7,2,9,10])
print(np.sort(a))
print(a) # nu modifica pe loc variabila

delimit(16)


L = [1, 2, 3, 4]
a = np.array(L)

print(L)
print(a)
print(type(L))
print(type(a))
L_1 = a.tolist()
print(L_1)
print(type(L_1))

delimit(17)


# Exemplu de program numpy.array vs list + for

temperaturi = [10,15,30,40]
temperaturi_f = []
for temp in temperaturi:
    temperaturi_f += [(temp * (9/5) + 32)]
print(temperaturi_f)

temperaturi = np.array([10,15,30,40])
temperaturi_f = temperaturi * (9/5) + 32
print(temperaturi_f)
