#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:36:50 2026

@author: alex
"""

import math

def putere(a, n):
    p = 1
    if n < 1:
        return p
    return a*putere(a, n-1)

def putere_it(a, n):
    p = 1
    for i in range (1, n+1):
        p = p*a
    return p

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def cifre_pare(n):
    n = abs(n)
    cif_pare = 0
    while n!= 0:
        if( (n%10)%2 == 0 ):
            cif_pare += 1
        n //= 10
    return cif_pare

def produs_div3(n):
    p=1
    while (n != 0):
        cifra = int(n%10)
        print(cifra)
        if (cifra % 3 == 0):
            p *= cifra
        n //= 10
    return p

def lungime(n):
    i = 0
    while n > 1:
        n //= 10
        i += 1
    return i

def oglindit(n):
    og = 0
    while n != 0:
        og += putere(10,lungime(n)) * int(n%10)
        n //= 10
    return og

def oglindit_2(n):
    ogl = 0
    while n!= 0:
        ogl = ogl * 10 + n%10
        n //= 10
    return ogl

def parab(x):
    return x*x

def integreaza(f, a, b, n=1000):
    h = (b - a) / n
    integr = 0
    for i in range(n):
        x = a + i*h
        integr += f(x) * h
    return integr

#print(putere(2, 10))
#print(putere_it(2, 10))
#print(factorial(5))
#print(comb(5, 2))
#print(cifre_pare(2486135))
#print(cifre_pare(2222222))
#print(produs_div3(39162))
#print(lungime(24))
#print(oglindit(123))
#print(oglindit_2(123))

print(integreaza(parab, 0, 1,10000))
print(integreaza(math.sin, 0, math.pi))
