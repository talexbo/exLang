#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:21:24 2026

@author: alex
"""
for bottles in range(99,0,-1):
  print(f"{bottles} bottles of beer on the wall")
  print(f"{bottles} bottles of beer")
  print("Take one down, pass it around")

for i in range (1,101): #fizzbuzz
  if (i%3==0 and i%5==0):
    print("FizzBuzz")
  elif (i%3==0):
    print("Fizz")
  elif (i%5==0):
    print("Buzz")
  else:
    print(i)



def exp(a,b):
  p = 1
  if(b<1):
      return p
  else:
    p *= exp(a,b)
  b = b -1

print(exp(2,2))
