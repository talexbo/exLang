#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:26:44 2026

@author: alex
"""

#model test lab 1

# Definiti clasa produs care modeleaza un produs dintr-un magazin si contine
# urmatoarele atribute: nume pret stoc

class Produs:
    def __init__(self, nume, pret, cantitate):
        if(nume == "" or pret <= 0 or cantitate < 0):
            raise ValueError("Date invalide")
        self.nume = nume
        self.pret = pret
        self.stoc = cantitate
    
    def valoare_stoc(self):
        return self.pret * self.stoc
    
    def este_disponibil(self):
        return self.stoc > 0
    
    def vinde(self, cantitate):
        if (self.stoc >= cantitate):
            self.stoc -= cantitate
            return True
        return False
    
    def __str__(self):
        return f"Produs: {self.nume}, Preŧ: {self.pret}, Stoc: {self.stoc}"
    
banane = Produs("Banane", 6, 2000)
mango = Produs("Mango", 10, 200)
print(banane.valoare_stoc())
print(banane)
print(mango)
banane.vinde(30)
print(banane)

# 2 liste

temperaturi = [18, 21, 16, 24, 27, 19, 22]

print(max(temperaturi))
print(min(temperaturi))
temp_medie = sum(temperaturi)/len(temperaturi)
print(temp_medie)
temp_peste_medie = [t for t in temperaturi if t >= temp_medie]

tF = [t * 9/5 + 32 for t in temperaturi]
print(tF)

temp_peste_20 = len([t for t in temperaturi if t >= 20])
print(temp_peste_20)

# numpy matpltlib

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,100)

y1 = x**2
y2 = 2*x + 1

plt.plot(x,y1, label="$x^2$")
plt.plot(x,y2, label = "2x + 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.title("Title")
plt.legend()
plt.show()

x_new = x[ y1 > y2] 
print(x_new[:5])