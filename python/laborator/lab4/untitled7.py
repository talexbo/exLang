#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:24:08 2026

@author: alex
"""

def cel_mai_frecvent(lista):
    frec = [0] * (max(lista) + 1)

    for n in lista:
        frec[n] += 1

    maxim = 0
    for i in range(len(frec)):
        if frec[i] > maxim:
            maxim = frec[i]
            el = i

    return el


def frecventa(lista):
    rezultat = {}
    for x in lista:
        if x in rezultat:
            rezultat[x] += 1
        else:
            rezultat[x] = 1
    return rezultat


lista = [1, 3, 2, 3, 1, 3, 2]
print(max(lista))
print(cel_mai_frecvent(lista))
note = [7,8,9,7,10,8,7,9,9,10,1]
freq = frecventa(note)
print(freq)
for nota,cnt in sorted(freq.items()):
    print(f"Nota {nota}: aparede {cnt} ori")
