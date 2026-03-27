#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:39:09 2026

@author: alex
"""

import math

#functii
def expr(a, b):
    return (a*a - b*b)/(a + b)

def este_prim(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5 + 1)):
        if n%i == 0:
            return False
    return True

def putere(x, p=2):
    return x**p
#p=2 val default, param def la final

def f(a,b,c=0):
    return a + 10*b +100*c

def adauga(x, lista=None):
    if lista is None:
        lista = []
    lista.append(x)
    return lista

def impartire(a,b):
    cat = a//b
    rest = a%b
    return cat,rest


def aplica(f, lista):
    rezultat = []
    for x in lista:
        rezultat.append(f(x))
    return rezultat

def gdc(a, b):
    if b == 0:
        return a
    return gdc(b, a % b)

def fact(n):
    if n <=1: # conditie
        return 1
    return n * fact(n-1) # pas recursiv

def fact_it(n):
    p = 1
    for k in range(2,n+1):
        p *= k
    return p #nerecursiv

print(expr(10,5))

print(este_prim(3))

print(putere(3)) #functie cu puterea 2 default
print(f(1,2,c=3)) #exemplu parametrii
print(f(1,2,3))

lista=[1,2,3]
adauga(4,lista)
print(lista)

c, r = impartire(17,5)
print(c,r)

valori = [0, 1, 4, 9, 16]

print(aplica(math.sqrt, valori)) # functia este paramentrul altei functii sus

print(gdc(2, 9))
print(fact(10))
print(fact_it(10))

#functii de o linie lambda
patrat = lambda x: x*x
print(patrat(5))

semn = lambda x: -1 if x < 0 else 1
print(semn(-7),semn(3))

numere = [1, 4, 9, 16, 25]
radacini = list(map(math.sqrt, numere)) #map prelucreaza lista si transforma
#fiecare element al listei, transformare in-place / map(f, [a,b,c]) => [f(a), f(b), f(c)]
#nu are legatura cu structura map din c++
print(radacini)

pare = list(filter(lambda x: x%2 == 0, range(10)))
#filtreaza
print(pare)

numere1= list(range(10))
pare1 = list(filter(lambda x: x%2 == 0, numere1))
# filter(p, [a,b,c]) p = paramentrul de filtrare i.e. functie cu return
print(pare1)

#Recursivitate
print(fact(5))

#Comprehensions: metoda const o colectie (lista/dict/set) dintr-un iterabil
#folosind for si optional if
#lista = []
#for x in A: lista.append(expresie)
#eq
#[expresie for x in A]
patrate = [x*x for x in range(10)]
print(patrate)

patrate_pare = [x*x for x in range(10) if x%2 == 0]
print(patrate_pare)

func = lambda x: x*x - 5*x + 6
sol = [x for x in range (-10, 11) if func(x) < 0]
print(sol)

#list map filter comprehensions diferente
#list(map(f,A)) ... [f(x) for x in A]
#list(filter(p,A)) .. [x for x in A if p(x)]
#list(map(f, filter(p,A))) ... [f(x) for x in A if p(x)]