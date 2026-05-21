#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:13:53 2026

@author: alex
"""
import math

class Punct:
    def __init__(self,x,y): # definire metoda pentru obiectul curent
        self.x = x
        self.y = y
    
    def translatie(self, dx, dy): # metoda translatie
        self.x = self.x + dx
        self.y = self.y + dy
    
    def translatie_b(self, dx, dy):
        B = Punct(self.x + dx , self.y + dy)
        return B
    
    def afiseaza(self):
        print(f"({self.x}, {self.y})")
    
    def distanta_de_la_origine(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
        
class Cerc:
    def __init__(self, raza):
        
        def aria(self):
            return
            
        def perimetrul(self):
            return 
        
A = Punct(2,3)
print(A.x)
print(A.y)
A.afiseaza()
Punct.afiseaza(A)
A.translatie(2, 2)
A.afiseaza()
print(A.translatie_b(-2,-2).afiseaza())
print(A.distanta_de_la_origine())