#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:34:19 2026

@author: alex
"""

def f(x):
    return x*x -3*x +2
tabel = {}
for x in range(-3,6):
    tabel[x] = f(x)
#afisare tabel

print(f"{'x':>5} | {'f(x)':>6}")
print("-" * 15)
for x, val in tabel.items():
    print(f"{x:>5} | {val:>6}")

radacini = [x for x,val in tabel.items() if val == 0]
print(f"\nRadacini in [-3,5]: {radacini}")
