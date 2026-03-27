#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:55:47 2026

@author: alex
"""

def inverseaza_dict(d):
    d_2 = dict()
    for k, el in d.items():
        d_2[el]=k
    return d_2
D = {"a":1 , "b":2, "c":3}
D = inverseaza_dict(D)
print(D)
