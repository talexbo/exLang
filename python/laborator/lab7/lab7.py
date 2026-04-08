#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:08:00 2026

@author: alex
"""
import numpy as np
import matplotlib.pyplot as plt

# 1

x = np.linspace(-3,3,100)
f_x = x**3 - 3*x

plt.title("$f(x)=x^3-3x$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid(True)
plt.plot(x,f_x,label="$x^3 - 3x$")

plt.legend()
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.show()

#2

x_g_h = np.linspace(-2,2,100)
g_x = np.exp(x_g_h)
h_x = np.exp(-x_g_h)

plt.title("$e^x$ si $e^{-x}$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.plot(x_g_h, g_x, label = "$e^x$")
plt.plot(x_g_h, h_x, label ="$e^{-x}$")
plt.scatter(0,1, s = 20, label="intersecție")

plt.legend()
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.show()

#3

x_trig = np.linspace(0, 2*np.pi, 600)
sin_x = np.sin(x_trig)
sin_2x = np.sin(2*x_trig)
sin_3x = np.sin(3*x_trig)

plt.title("$sin(x)$ $sin(2x)$ $sin(3x)$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.plot(x_trig, sin_x, label = "$sin(x)$")
plt.plot(x_trig, sin_2x, label = "$sin(2x)$")
plt.plot(x_trig, sin_3x, label = "$sin(3x)$")

plt.legend()
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.show()

#4

x = np.linspace(-10,10,10)
y_1 = x - 2
y_2 = x
y_3 = x + 2 
y_4 = x + 4

plt.title("Funcții liniare1")
plt.xlabel("$x$")
plt.ylabel("$y$")

plt.plot(x, y_1, label = "$x - 2$")
plt.plot(x, y_2, label = "$x$")
plt.plot(x, y_3, label = "$x+2$")
plt.plot(x, y_4, label = "$x+4$")
# dreptele au aceeasi panta
# nu se intersecteaza
# termenul liber e distanta fata de dreapta y = x

plt.legend()
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.show()

#5

x = np.linspace(-4,4,100)
y_1 = 1 / (x**2 + 1)
y_2 = 2 / (x**2 + 1)
y_3 = 3 / (x**2 + 1)

plt.title("Functii")
plt.xlabel("$x$")
plt.ylabel("$y$")

plt.plot(x, y_1, label = "$\\frac{1}{x^2 + 1}$")
plt.plot(x, y_2, label = "$\\frac{2}{x^2 + 1}$")
plt.plot(x, y_3, label = "$\\frac{3}{x^2 + 1}$")


plt.legend()
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.show()

#6 


x = np.linspace(-4.0,3,100)
y_1 = x**2 + 2*x
y_2 = 2*x + 3
x_int = np.array([-np.sqrt(3),np.sqrt(3)])
y_int = 2*x_int + 3
plt.scatter(x_int,y_int, s = 20)

plt.title("Functii")
plt.xlabel("$x$")
plt.ylabel("$y$")

plt.plot(x, y_1, label = "$x^2+2x$")
plt.plot(x, y_2, label = "$2x+3$")

plt.legend()
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.show()

#7

x = np.linspace(-1.5,1.5,100)
y_1 = x
y_2 = x**2
y_3 = x**4
y_4 = x**6

plt.title("Functii")
plt.xlabel("$x$")
plt.ylabel("$y$")

plt.plot(x, y_1, label = "$x$") #nu e para
plt.plot(x, y_2, label = "$x^2$")
plt.plot(x, y_3, label = "$x^4$")
plt.plot(x, y_3, label = "$x^6$")

plt.legend()
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.show()

#8

x = np.linspace(-2,2)
y = np.linspace(-2,2)
X, Y = np.meshgrid(x,y)
Z = X * np.exp(-(X**2 + Y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X,Y,Z, alpha=0.85)

ax.set_title("$f(x,y) = e^{-(x^2+y^2)}$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
plt.show()

#9

x = np.linspace(-2.4,2.4)
y = np.linspace(-2.4,2.4)
X, Y = np.meshgrid(x,y)
Z = X**2 + Y**2
Z_4 = Z*0 +4

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X,Y,Z, alpha=0.5)
ax.plot_surface(X,Y,Z_4, alpha=0.8)
ax.view_init(elev=5, azim=19)

ax.set_title("$f(x,y) = x^2 +y^2$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
plt.show()

