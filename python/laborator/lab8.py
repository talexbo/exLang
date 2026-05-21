#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:13:07 2026

@author: alex
"""

import numpy as np
import matplotlib.pyplot as plt

# subgrafice si stilizare 
# plt.subplots

x = np.linspace(-2*np.pi, 2*np.pi, 500)

fig, axa = plt.subplots(1,2,figsize=(10,4))

axa[0].plot(x, np.sin(x), color='blue')
axa[0].set_title('$\sin(x)$')
axa[0].set_xlabel('x')
axa[0].set_ylabel('y')
axa[0].grid(True)

axa[1].plot(x, np.cos(x), color='red')
axa[1].set_title('$\cos(x)$')
axa[1].set_xlabel('x')
axa[1].set_ylabel('y')
axa[1].grid(True)

plt.tight_layout()
plt.show

########################

x = np.linspace(-3,3,400)

fix, axa = plt.subplots(2, 1, figsize=(7,7))
axa[0].plot(x, x**2, color='blue', linewidth=2)
axa[0].set_title('$y=x^2$')
axa[0].set_xlabel('x')
axa[0].set_ylabel('y')
axa[0].grid(True)

axa[1].plot(x, x**3, color='red',
            linestyle='--', linewidth=2)
axa[1].set_title('$y=x^3$')
axa[1].set_xlabel('x')
axa[1].set_ylabel('y')
axa[1].grid(True)

plt.tight_layout()
plt.show

########################

x = np.linspace(-2,2,400)

fix, axa = plt.subplots(2, 2, figsize=(16,9))
axa[0,0].plot(x, x)
axa[0,0].set_title(r'$y=x$')

axa[0,1].plot(x, x**2)
axa[0,1].set_title(r'$y=x^2$')

axa[1,0].plot(x, x**3)
axa[1,0].set_title(r'$y=x^3$')

axa[1,1].plot(x, x)
axa[1,1].set_title(r'$y=|x|$')

for i in range(2):
    for j in range(2):
        axa[i,j].set_xlabel('x')
        axa[i,j].set_ylabel('y')
        axa[i,j].grid(True)
        
plt.tight_layout()
plt.show()

#########################


M = np.array([[1, 4, 9, 16],
              [2, 3, 5, 7],
              [0, 1, 0, 1]])
linie = M[1,:]
x = np.arange(len(linie))
np.arange(len(linie))

plt.figure(figsize=(6.5, 4))
plt.plot(x, linie, marker='o', label='Linia a doua')
plt.title("Reprezentarea unei linii dintr-o matrice")
plt.xlabel('Indice')
plt.ylabel('Valoare')
plt.grid(True)
plt.legend()
plt.show()

######################### Probleme propuse

x = np.linspace(-2*np.pi, 2*np.pi, 500)

fig, axa = plt.subplots(1,2,figsize=(10,4))

axa[0].plot(x, np.sin(x), color='blue')
axa[0].set_title('$\sin(x)$')
axa[0].set_xlabel('x')
axa[0].set_ylabel('y')
axa[0].grid(True)

axa[1].plot(x, np.sin(2*x), color='red')
axa[1].set_title('$\sin(2x)$')
axa[1].set_xlabel('x')
axa[1].set_ylabel('y')
axa[1].grid(True)

plt.tight_layout()
plt.show

########################

x = np.linspace(-3,3,400)

fig, axa = plt.subplots(2, 1, figsize=(7,7))
axa[0].plot(x, x**2, color='blue', linewidth=2)
axa[0].set_title('$y=x^2$')
axa[0].set_xlabel('x')
axa[0].set_ylabel('y')
axa[0].grid(True)

axa[1].plot(x, x**4, color='red',
            linestyle='--', linewidth=2)
axa[1].set_title('$y=x^4$')
axa[1].set_xlabel('x')
axa[1].set_ylabel('y')
axa[1].grid(True)

plt.tight_layout()
plt.show()

########################

def cuburi(lista):
    return lista**2
lista = np.array([-2,-1,0,1,2,3])
print(cuburi(lista))

def poli3(x):
    return x**3 - 2*x

x = np.linspace(-3, 3, 100)

plt.title('Titlu')
plt.plot(x, poli3(x), label='$y = x^3 - 2x$')
plt.plot(x, x**2, linestyle='--', label='$y=x^2$')
plt.plot(x, (x**2 + 2*x), linestyle='-.', label='$y=x^2+2x$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()

########################

A = np.array([[1,0,2],
              [-1,3,1]])

B = A*A + 2*A
print(B)
col_B = B[:,0]
print(col_B)

#########################

x = np.linspace(-2,2,400)

fix, axa = plt.subplots(2, 2, figsize=(16,9))
axa[0,0].plot(x, x, linestyle='-.', color='black')
axa[0,0].set_title(r'$y=x$')

axa[0,1].plot(x, x**2, linestyle='--', color='blue')
axa[0,1].set_title(r'$y=x^2$')

axa[1,0].plot(x, x**3, linestyle=':', color='purple')
axa[1,0].set_title(r'$y=x^3$')

axa[1,1].plot(x, x, linestyle='dotted', color='red')
axa[1,1].set_title(r'$y=|x|$')

for i in range(2):
    for j in range(2):
        axa[i,j].set_xlabel('x')
        axa[i,j].set_ylabel('y')
        axa[i,j].grid(True)
        
plt.tight_layout()
plt.show()

#########################

#f(x,y) = exp(-(x^2+y^2)/2)
#g(x,y) = sin(x)cos(y)f(x) x,y = [-1,1]

x = np.linspace(-3,3,100)
y = np.linspace(-3,3,100)

X, Y = np.meshgrid(x,y)
Z = np.sin(X)*np.cos(Y)*np.exp(-(X**2 + Y**2)/2)
Z_f = np.exp(-(X**2 + Y**2)/2)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X,Y,Z, alpha=0.85, label='$g(x) = sin(x) \\cdot cos(x) \\cdot f(x)$')
ax.plot_surface(X,Y,Z_f, label='$f(x) = e^{\\frac{-(x^2+y^2)}{2}}$')
ax.legend()
ax.set_title("$g(x,y) = sin(x) \\cdot cos(x)\\cdot e^{\\frac{-(x^2+y^2)}{2}}$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
plt.show()

#########################

A = np.array([[1,2,1],
              [0,1,2],
              [0,1,1]])

S = A
for i in range(5):
    S = S*A
print(S)

#A^2*X = (3,8,6)

A_2 = A*A
A_2_inv = np.invert(A_2)
print(A_2_inv)

X = A_2_inv*np.array([3,8,6])

