# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# functii 

x = np.linspace(-3, 5,400)
y = x**2
x_int = np.array([-1.0,3])
y_int = x_int**2

plt.plot(x, y, label="$y=x^2$")
plt.plot(x, 2*x+3, label="y=2x+3")
plt.scatter(x_int,y_int, s = 60, label="intersecție")
plt.title("Graficul funcției $f(x)=x^2$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.legend()
plt.figure(figsize=(7.2,4.8))

plt.show()

# sin cos

rad = np.linspace(-2*np.pi, 2*np.pi, 100)
sinus = np.sin(rad)
cosin = np.cos(rad)

plt.title("Graficele funcțiilor sin(x) și cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.9)
plt.axhline(1, color="red")
plt.axhline(-1, color="red")
plt.axvline(0, color="black", linewidth=0.5)

plt.plot(rad, sinus, label="$sin(x)$")
plt.plot(rad, cosin, label="$cos(x)$")
plt.legend()

plt.show()

# suprafete plane

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

X, Y = np.meshgrid(x,y)
Z = X**2 + Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X,Y,Z, alpha=0.85)

ax.set_title("$f(x,y) = x^2 + y^2$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
plt.show()

