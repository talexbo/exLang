import numpy as np
# Problema 1

a = np.array([5, 10, 15, 20, 25, 30, 35])
print(a[0], a[3], a[-1])
print(a[2:5])
print(a[::2])
a[::2] = -1
print(a)

# Problema 2

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
print(np.shape(A))
print(np.ndim(A))
print(A[0, 0], A[1, 2], A[2, 1])
print(A[1, :])
print(A[:, 0])
print(A[0:1, 1:2])


# Problema 3

z = np.zeros((2, 4))
o = np.ones((3, 2))
I = np.eye(4)
v = np.arange(1, 13)
V = v.reshape(3, 4)
W = v.reshape(2, 6)
print(z)
print(o)
print(I)
print(v)
print(V)
print(W)

# Problema 4

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A+B)
print(A-B)
print(A*B)
print(A@B)
print(3*A)
print(A.T)


# Problema 5

A = np.array([[-1, 2, 31], [42, -5, 26]])
v = np.array([10, 20, 30])
u = np.array([[100], [200]])
print(A+10)
print(A*v)
print(A-u)
# d)
# print(A+np.array([10,2,5,-3])) -nu sunt egale, 4 cu e multiplu de 3

# Problema 6

A = np.array([[-1, 2, -3], [4, -5, 6], [4, -1, 7]])
print(np.sum(A), np.min(A), np.max(A), np.mean(A))
print(np.sum(A, axis=0))
print(np.sum(A, axis=1))
print(np.mean(A, axis=0))
print(np.mean(A, axis=1))
print(np.max(A, axis=0))
print(np.min(A, axis=1))

# Problema 7

A = np.array([[-1, 2, -3], [4, -5, 6], [4, -1, 7]])
B = np.array([[1, 2], [2, 4]])
print(np.linalg.det(A))
print(np.linalg.inv(A))
print(np.allclose(A@np.linalg.inv(A), np.eye(3)))
print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(B))
M = np.array([[2, 1], [1, 3]])
print(np.linalg.solve(M, [5, 7]))

# Problema 8

a = np.array([2, 7, 1, 9, 5, 8, 3])
A = np.array([[4, 2, 7], [1, 5, 1], [3, 6, 8]])
print(np.where(a > 3))
print(a[np.where(a > 3)])

print(np.where(A % 2 == 0))
poz = np.where(A % 2 == 0)
print(poz[0])
print(poz[1])

# Problema 9

v = np.linspace(0, np.pi, 9)
V = v.reshape(3, 3)
print(np.sin(V))
print(np.cos(V))
print(np.sin(V)+np.cos(V))
print(np.where(np.sin(V) > np.cos(V)))

# Problema 10

A = np. array([[-4, -1, 1], [1, 4, 9], [16, 25, 36]])
print(np.abs(A))
print(A**2)
print(np.where(A > 0, np.sqrt(A), A))
