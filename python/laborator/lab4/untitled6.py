#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:06:25 2026

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

lista = [1, 3, 2, 3, 1, 3, 2]
print(max(lista))
print(cel_mai_frecvent(lista))
