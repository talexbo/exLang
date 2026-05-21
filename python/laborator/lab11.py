#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:17:33 2026

@author: alex
"""

import math
import numpy as np
import matplotlib.pyplot as plt

class Punct:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
            
    def distanta_la_punct(self,alt_punct):
        return math.sqrt((self.x-alt_punct.x)**2 + (self.y - alt_punct.y)**2)
    
    def translatie(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    def simetric_fata_de_origine(self):
        x = -self.x
        y = -self.y
        return Punct(x,y)
        # SAU return (-self.x, -self.y)
    
    def simetric_fata_de_alt_pct(self,alt_punct):
        x = 2*alt_punct.x - self.x
        y = 2*alt_punct.y - self.y
        return Punct(x,y)
    # return Punct(2*alt_punct.x - self.x, 2*alt_punct.y - self.y)
    
    def __str__(self):
        return f'({self.x},{self.y})'

class Cerc:
    
    def __init__(self,c,r):
        if r <= 0:
            raise ValueError("Raza trebuie sa fie pozitiva.")
        
        self.c = c
        self.r = r
    
    def aria(self):
        return math.pi + self.r**2
    
    def perimetru(self):
        return 2 * math.pi * self.r

    def contine_punct(self, P):
        distanta = self.c.distanta_la_punct(P)
        return distanta <= self.r
    
    def scimba_raza(self,r_2):
        if r_2 <= 0:
            raise ValueError("Raza trebuie sa fie pozitiva.")
        
        self.r = r_2
        
    def coordonate(self):
        t = np.linspace(0,2*np.pi,400)
        X = self.c.x + self.r * np.cos(t)
        Y = self.c.y + self.r * np.sin(t)
        return X, Y
    
    def deseneaza(self):
        X,Y = self.coordonate()
        plt.plot(X,Y, label = "Cerc")
        plt.scatter(self.c.x, self.c.y, label="Centru")
        plt.text(self.c.x, self.c.y, " O")
        
        plt.axhline(0,color="black", linewidth=0.8)
        plt.axvline(0,color="black", linewidth=0.8)
        plt.grid(True)
        plt.gca().set_aspect("equal")
        plt.title("Cerc")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(loc='upper right')
        plt.show()
        
    
    
    def __str__(self):
        return f"Cerc cu centrul {self.c} si raza {self.r}"

class Student:
    def __init__(self, nume, nota):
        
        if nume == "":
            raise ValueError("Numele nu poate fi vid.")
        if nota < 1 or nota > 10:
            raise ValueError("Nota trebuie sa fie intre și 10")
        self.nume = nume
        self.nota = nota
    
    def este_promovat(self):
        return self.nota >= 5
    
    def modifica_nota(self,nota_noua):
        if nota_noua < 1 or nota_noua > 10:
            raise ValueError("Nota trebuie sa intre de la 1 și 10")
        self.nota = nota_noua
        
    def __str__(self):
        return f"{self.nume}: {self.nota}"
    
    
s1 = Student("Ion Popescu", 9)
print(s1.este_promovat())    
s1.modifica_nota(4)
print(s1.este_promovat())
print(s1.__str__())
    

x1 = Punct(2,1)
x1.translatie(1, 5)
print(x1.distanta_la_punct(Punct(0,0)))
print(x1.__str__())
x2 = Punct(0,0)
x3 = Punct(1,1)
x1_sim = x1.simetric_fata_de_origine()
print(x1_sim.__str__())
x1_sim_x2 = x1.simetric_fata_de_alt_pct(x2)
print(x1_sim_x2.__str__())
x1_sim_x3 = x1.simetric_fata_de_alt_pct(x3) 
print(x1_sim_x3.__str__())
x_sim = Punct(2,2).simetric_fata_de_alt_pct(Punct(1,1))
print(x_sim.__str__())

c_1 = Cerc(Punct(1,1), 1)
print(c_1.contine_punct(Punct(0,1)))
c_1.scimba_raza(2)
print(c_1.contine_punct(Punct(0,1)))
print(c_1.__str__())

c_1.deseneaza()