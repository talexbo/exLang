#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:23:45 2026

@author: alex
"""

class Fractie:
    def __init__(self,numa,numi):
        if numi == 0:
            raise ValueError('Numitorul nu poate fi 0')
        self.numa=numa
        self.numi=numi
    
    def __add__(self, fract):
        numa = self.numa * fract.numi + self.numi * fract.numa
        numi = self.numi * fract.numi
        return Fractie(numa,numi)
    
    def __str__(self):
        return f'{self.numa}/{self.numi}'
    
    def __amp__(self,a):
        if a == 0:
            raise ValueError('Numarul trebuie sa fie difereit de 0')
        self.numa = a * self.numa
        self.numi = a * self.numi
    
    def __pow__(self,exp):
        if exp == 0:
            return Fractie(1,1)
        if exp > 0:
            numa = self.numa ** exp
            numi = self.numi ** exp
        else:
            numi = self.numa ** -exp
            numa = self.numi ** -exp
        return Fractie(numa,numi)
    
f1 = Fractie(1,2)
f2 = Fractie(1,3)

print(f1.__add__(f2))
print(f1)
f1.__amp__(2)
print(f1)

print(f1.__pow__(3))
print(f1.__pow__(-1))

