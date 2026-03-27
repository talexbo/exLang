#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:12:20 2026

@author: alex
"""

#functii

def este_prim(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

def cmmdc(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a,b = b, a % b
    return a


def cmmc(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // cmmdc(a, b)


#cod

#for n in [1, 2, 3 ,4, 17, 18, 97, 100]:
#    stare = "prim" if este_prim(n) else "compus"
#    print(f"{n:3d} este {stare}")

perechi = [(12, 8), (100, 75), (17,13), (48, 36)]
print(f"{'a':>5} {'b':>5} {'CMMDC':>8} {'CMMC':>8}")
print("-" * 30)
for a, b in perechi:
    print(f"{a:>5} {b:>5} {cmmdc(a, b):>8} {cmmc(a, b):>8}")
