#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:28:27 2026

@author: alex
"""

def inverseaza(lista):
    lung = len(lista)
    inv = []
    for i in range(0,lung):
        inv.append(lista[lung-1-i])
    return inv
lista = [1,3,4,2,5,6]
print(lista)
lista = inverseaza(lista)
print(lista)

def inverseaza_2(lista):
    lista_2 = []
    for n in lista:
        lista_2.insert(0,n)
    return lista_2

lista = inverseaza_2(lista)
print(lista)
