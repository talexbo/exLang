#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:16:54 2026

@author: alex
"""

#Lab 4

note = [7, 8, 9, 10]
puncte = [(1,2), (3,4, (5,6))]
print(note[0])
print(note[-1])
print(note[-2])

v = [10, 20, 30, 40, 50, 60, 70, 80]
print(v[2:5])
print(v[:5])
print(v[::2])
print(v[::-1])

note = [7,8,9,10]

for i, val in enumerate(note):
    print(f"{i}  {val}")
