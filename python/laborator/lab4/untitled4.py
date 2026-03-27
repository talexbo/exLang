#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:49:16 2026

@author: alex
"""
# Scrie o functie rotire lista k care roteste lista circular la dreapta cu n elemente
def rotire(lista, k):
    lista_2 = []
    for i in lista:
        lista_2=lista[k+1:] + lista[:-k]
    return lista_2

lista =[1,2,3,4,5]
lista = rotire(lista,2)
print(lista)
