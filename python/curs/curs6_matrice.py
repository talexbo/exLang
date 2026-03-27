# -*- coding: utf-8 -*-
import numpy as np

#NumPy avansat

def delimit(i):
    print(" ")
    print(f"-({i})-" + 48*"-")

delimit(0)#################################################################

v = np.array([1,2,3,4,5,6])

print(v[0])
print(v[2])
print(v[-1])
print(v[1:4]) # de la 1 pana inainte de 4
print(v[:3]) # pana inainte de 3
print(v[3:]) # de la 3 
print(v[::2]) # pas

delimit(1)#################################################################


L = [1,2,3,4,5,6]
L[1:4] = [0,0,0] # atribuie lista; L[1:4] = 0 gresit
print(L)

v[1:4] = 0 # atribuie scalar direct
print(v)

delimit(2)#################################################################

A = np.array([[1,2,3],
              [3,4,6],
              [7,8,9]])
print(A)
print(A.ndim)
print(A.size)

delimit(3)#################################################################

Z = np.zeros((2,3))
O = np.ones((3,2))
I = np.eye(3)

print(A)
print(O)
print(I)

delimit(4)#################################################################

a= np.arange(1,7)
A = a.reshape(2,3)
print(a)
print(A)

delimit(5)#################################################################

A = np.array([[1,2,3],
              [3,4,6],
              [7,8,9]])

print(A[0,0]) # extrage element
print(A[1,2])
print(A[2,1])
print(A[1,:]) # extragere de linii; linia a doua
print(A[:, 0]) # extrage coloana 1

A = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
print(A[0:2, 1:3]) #extrage submatrice taind 0:2 pe linii si 1:3 pe col

delimit(6)#################################################################

# Operatii cu matrice in NumPy

#A*B nu inseamna in general produs matricial

A = np.array([[1,2],
              [3,4]])
B = np.array([[1,2],
              [3,4]])

print(A+B)
print(A-B)

# A * B
print(A * B) # element cu element nu matricial

# A @ B
print(A @ B) # inmultire normala

# Inmultirea cu scalar
print(3 * A) 

# alte operatii

print(A.T) # transpusa
print(np.linalg.inv(A)) # inversa cu .inv din sublibraria .linalg
print(A^(-1)) # matricea cu inversele per element

delimit(7)#################################################################

# Broadcasting

# combina automat array-uri cu forme diferite, extinzand implicit o dim.
# pentru a face operatia posibila
# functioneaza doar atunci cand formele array-urilor sunt compatibile

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
v = np.array([1,2,3]) #vector linie

print(A+10) # scalarul 10 este extins la forma matricei ex. (3x3)
print(A + v) # vectorul (:1) este extins la forma 3x3 i.e adauga vectorul 
# pe cate numere sunt necesare

u = np.array([[10],
              [20],
              [30]]) # vector coloana

print(A + u)

print(u+v) # adunare vector linie cu vector coloana
# extinde vectorul coloana in asa fel sa se potriveasca cu numarul de col
# a vectorului linie, si analog extinde vectorul inie i.e. (1x3) + (3x1) = (3x3)
# dimensiunea vec col = dim vec linie pentru ca numpy sa nu dea EROARE
# broadcasting-ul functioneaza cand dim matricilor sunt egale sau cand 
# una dintre dimensiuni este 1.

delimit(8)#################################################################

A = np.array([[1, 2, 3],
              [4, 5, 6]])
print(np.sum(A))
print(np.min(A))
print(np.max(A))
print(np.mean(A))
# functiile de mai sus se fac cu toate elementele matricei

#sume pe linie sau coloana

print(np.sum(A, axis=0)) #return matrice cu sume per coloane
print(np.sum(A, axis=1)) #return matrice cu sume per linii

print(np.mean(A, axis=0)) #return matrice cu medii per coloane
print(np.mean(A, axis=1)) #return matrice cu medii per linii

print(np.max(A, axis=0)) #return matrice cu maxime de pe coloane
print(np.max(A, axis=1)) #return matrice cu maxime de pe linii

print(np.min(A, axis=0)) #return matrice cu minime de pe coloane
print(np.min(A, axis=1)) #return matrice cu minime de pe linii
#axis = 0 coloane
#axis = 1 linii

delimit(9)#################################################################
# A de mai sus

rang_A = np.linalg.matrix_rank(A)
print(rang_A) # merge chiar daca matricea nu e patratica; rang deltaP

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(A)
det_A = np.linalg.det(A) 
print(det_A)
#A_inv = np.linalg.inv(A)
#print(A_inv) # det matricei de mai sus este 0 si nu are inversa

A_2 = np.array([[1,2,1],
                [4,5,6],
                [7,8,9]])

det_A_2 = np.linalg.det(A_2)
print(det_A_2)

A_2_inv = np.linalg.inv(A_2)
print(A_2_inv)

rang_A_2 = np.linalg.matrix_rank(A_2)
print(f"Rangul matricei A_2 (3x3) cu determinantul {det_A_2} este {rang_A_2}")

A = np.array([[2,1],
             [1,3]])
b = np.array([1,2]) #solve

print("Solutiile sistemului de ecuatii sunt: ", np.linalg.solve(A,b))

A = np.array([[1,2],
              [3,4]])

A_inv = np.linalg.inv(A)
print(A @ A_inv) # inversa se face prin aproximari deci inmultirea nu o sa
# de matricea unitate; 
# din acest motiv nu comparam direct matrici cu elemente de tip float folosind == 
# in schimb folosim np.allclose() sa vedem daca elementele sunt apropiate

print(A == A_inv)

A = np.array([[1,0,0],
              [0,1,0],
              [0,0,1]])
A_inv = np.linalg.inv(A)

print(A)
print(A_inv)
print(A.T)
simterica = np.allclose(A, A.T)

I = np.eye(A.shape[0]) # .shape() are output un tuple cu dimensiunile [0] scoate
                       # numarul liniilor, iar eye creaza mat. identitate de 
                       # dimensiunea respectiva
print(I) # float-uri
print(A) # inturi

print(I == A) # elementel din matrice sunt egale intre ele => matrice 3x3 de True
print(A == A_inv) # in cazul asta e True, dar mai sus e un exemplu pentru care
# aproximarile float al inversei cu val reale a inversei ar da False
ortogonala = np.allclose(A, A_inv) # true 
print(ortogonala) # matricea identitate este egala cu inversa ei

delimit(10)#################################################################

a = np.array([1,2,7,1,9,5,8,9])
print(a)

print(np.where(a == 1)) # vector print unde el. = 1
          

A = np.array([[4,2,7],
              [1,5,1],
              [3,6,8]])

poz = np.where(A == 1)
print(A)
print(poz) # pozitiile pentru care elementul din a este 1
print(poz[0]) # randurile pe care se gasesc
print(poz[1]) # coloanele pe care se gasesc

for row, col in zip(*poz):
    print(f"({row}, {col})")
# zip(*poz) face perechi element cu element din lista de tuples de tipul i,j
# altfel coordonatele sunt in doua liste separate

delimit(11)#################################################################

col = np.array([0,2,0,2,2,1])
print(np.unique(col)) # pastreaza din array doar elementele care sunt distincte
mat = np.array([[0,2,0],
                [2,2,1]]) # pe matrice o forteaza intr-un vector si da return
print(np.unique(mat))     # elementelor distincte

delimit(12)#################################################################

# Problema, se da o matrice sa se determine coloanele pe care apare val min din
#matrice iar pe aceste coloane sa se adauge o constanta c. (cu np.where)

c = 10 
minim = np.min(A)
linii, coloane = np.where(A == minim) #coloanele unde exista min
coloane_unice = np.unique(coloane) #elimina duplicate pentru nu a aduna c
                                   #de doua ori

A_nou = A.copy()
A_nou[:, coloane_unice] += c
#^merge pe fiecare linie pe coloanele din vectorul de coloane unice

print("Minimul:", minim)
print("Linii: ", linii)
print("Coloane: ", coloane)
print("Coloane distincte:", coloane_unice)

delimit(13)#################################################################

# Se da o matrice A. Sa se determine coloanele in care apare valoarea maxima 
# din matrice , iar toate elementele de pe aceste coloane sa fie inlocuite cu 0.

maxim = np.max(A)
linii, coloane = np.where(A == maxim)
coloane_unice = np.unique(coloane)
A_nou = A.copy()

A_nou[:, coloane_unice] = 0

print("Maximul: ", maxim)
print("Coloane unice: ", coloane_unice)
print("Matricea modificata: ")
print(A_nou)