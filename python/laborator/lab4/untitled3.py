#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:38:04 2026

@author: alex
"""

#def comune(A,B):
#    intrare = ""
#    print("adauga in A: ")
#    while intrare != -1:
#        intrare = input()
#        A.append(intrare)
#    print("adauga in B: ")
#    A = int(A)
#    while intrare != -1:
#        intrare = input()
#        B.append(intrare)
#    B = int(B)
#    print(A)
#    print(B)
#
#A = []
#B = []
#comune(A,B)

def comune(A,B):
    A = set(A)
    B = set(B)
    intersectia = A & B
    intersectia = list(intersectia)
    intersectia.sort()
    return intersectia

A = [1,2,3,4,4]
B = [3,4,5,6,7]
C = comune(A,B)
print(C)
