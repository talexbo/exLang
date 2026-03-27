#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:18:48 2026

@author: alex
"""

import numpy as np

a = np.array([1,2,3,4,5,6,7,8])
rez = a[a>5]
print(rez)

a = np.zeros(7)
b = np.ones(5)
c = np.arange(0,15,2)
print(a, b, c)

d = np.linspace(-2, 2, 9)
print(d)
print(len(d))

f = np.arange(-5,6,1)
print(f)

x = np.array([-3,-2,-1,0,1,2,3])
print(x+2)
print(3*x -1)
print(x**2)
print(x**2 + 3*x +2)
print(np.abs(x))
print(abs(x))

y = np.array([0,1,2,3,4,5])
print(y*y + 3)

y_1 = y.tolist()
print([i**2 + 3 for i in y_1])

a = np.array([4,7,2,9,6,2,9])
print(np.sum(a))
print(np.mean(a))
print(f"minimul este {min(a)} la pozitia {np.argmax(a)}; maximul este {max(b)} la pozitia {np.argmin(a)}")
print(np.where(a == np.min(a)))
print(np.where(a == np.max(a)))
print(np.sort(a))

a = np.array([-4,-1,0,2,5,7,8,11])
print(a[a>0])
print(a[a%2 == 0])
print(a[(a >= 0) & (a <= 7)])
print(a[a > np.mean(a)])


c = np.array([12,15,18,21,24,19,16])

f = c *(9/5) + 32

print(f)
print(np.mean(c))
print(np.argmax(c))
print(c - np.mean(c))
print(c[c > np.mean(c)])

def distanta_fata_de_medie(a):
    return np.abs((a-np.mean(a)))

a = np.arange(-100,1,10)
print(a)
print(distanta_fata_de_medie(a))

def raport_fata_de_max(a):
    if np.max(a) == 0:
        return None
    else:
        return(a / np.max(a))

print(a)
print(raport_fata_de_max(a))
a = np.arange(0,101,10)
print(a)
print(raport_fata_de_max(a))

a = np.arange(1,25,3)

def normalizare_0_1(a):
    if np.max(a) == np.min(a):
        return a*0
    else:
        return((a-np.min(a))/(np.max(a)-np.min(a)))

print(a)
print(normalizare_0_1(a))

a = np.zeros(20)

print(normalizare_0_1(a))

def este_sortat_crescator(a):
    b = np.sort(a)
    if np.array_equal(a,b):
        print("Sirul este sortat")
    else:
        print("Sirul nu este sortat")

ns = np.array([1,200,3,4,22,19])
este_sortat_crescator(ns)
s = np.arange(1,10)
este_sortat_crescator(s)
