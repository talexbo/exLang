#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:12:41 2026

@author: alex
"""

# lista

x1 = 3
x2 = 7
x3 = 10
x4 = 12

print (x1 + x2 + x3 + x4)

valori = [3,7,10,12]
print(sum(valori))

# tipuri: liste, tuple, set ,dictionar
# lista col ord mod; tuple col ord nemod
# set col fara duplicate
# dic - map C++
# ordonate =/= sortate; pastreaza ordinea data
# lista -> vector nr. ex

note = [7,8,9,10]
print(note)
date = [3,4.5,"Ana"]
print(date)
print(note[0])
print(note[2])
print(note[-1])
print(note[-4])

note = [7, 8, 9]
note[1] = 10
print(note)

valori = [1,2,3]
valori.append(4)
print(valori)
valori.remove(2) # sterge 2 din lista, nu indexul 2
print(valori)

x = valori.pop() # scoate ultimul si da return
print(x)
print(valori)

note = [7,8,9,10]
for n in note:
    print(n)

# Exercitii

#1

lista = []

for i in range(1,11):
    lista.append(i)

print(sum(lista))
print(lista)

elemente = [2, 5.6, "Text"]
print(elemente[-1])
print(elemente[-2])
elemente[-1] = 7
print(elemente[-1])

#Tuple
#paranteze rotunde, nu se modifica, pot avea oricate elemente
punct = (2,5)
data = ( 15, 3, 2005)
culoate = (0,0,0)
#accesarea
print(data[0])
print(data[1])
print(data[2])

punct=(2,5)
#punct[0] = 1 EROARE

def impartire(a,b):
        cat = a // b
        rest = a % b
        return(cat,rest)
print(impartire(2,3))

coordonate = (2,5)
print(coordonate)
print(f"abscisa: {coordonate[0]}, ordonata: {coordonate[1]} ")

c = (5, coordonate[1])
coordonate = c
coordonate = (coordonate[0], 3)
print(coordonate)

#Seturi
#fara duplicate, ordine neimportatnta, operatii cu multimi

A = {1,2,3,3,4}
print(A)

A = {1,2,3}
B = {3,4,5}

print(A | B) #reuniune
print(A & B) #intersect
print(A - B) #dif

cuvant = "matematica"
litere = set(cuvant)
print(litere) #ordinea nu se pastreaza

litere1 = set("matematica")
litere2 = set("informatica")
print(litere1)
print(litere2)

print(litere1 | litere2)
print(litere1 & litere2)
print(litere1 - litere2)
print(litere2 - litere1)

#Dictionar
# cheie -> val
note = {
        "Ana": 10,
        "Ion": 8,
        "Maria": 9
}
print(note["Ana"])

note = {"Ana": 10, "Ion": 8}
note["Maria"] = 9
note["Ion"] = 10
print(note)

for nume, nota in note.items():
    print(nume,nota)

note = [7,8,9,10]
print(len(note)) # lungime
print(8 in note) # search function
print(5 in note)

valori = [10,20,30,40,50,60]
print(valori[1:4]) #slicing; ultima val nu e inclusa
print(valori[:3])
print(valori[3:])
print(valori[::2]) #din 2 in 2 (al 3lea parametru)

note = [7,8,9,10]

for n in note: # i.e. for each
    print(n)

for i in range(len(note)): # for range
    print("index =", i, "valoare = ", note[i])

for i, x in enumerate(note): # echivalent cu ^
    print(i, x)

#sort + reverse
valori = [7,2,9,1,5]
valori.reverse()
print(valori)
valori.sort()
print(valori)
valori.reverse()
print(valori)
# = sorted()
valori = [7,2,9,1,5]
copie_sortata = sorted(valori)
print(valori)
print(copie_sortata)

print(valori.count(2))
print(valori.count(3))
print(valori.index(2))

note = {"Ana": 10, "Ion":8 }
print(note.keys())
print(note.values())
print(note.items())
print("Ana" in note)
print("Maria" in note)

valori = [10,20,30]
#print(valori[3]) EROARE in afara listei

note = {"Ana": 10, "Ion":8 }
#print(note["Maria"]) EROARE pt. ca cheia nu exista in dictionar

a = {} #nu creaza multime vida; ci dic vid
b = set() #creaza multime vida
print(type(a))
print(type(b))

note =[7,8,9,10]
media = sum(note) /len(note)
print(media)

valori = [1,2,2,3,4,4,4,5] #transforma lista in set, i.e se elimina duplicate
distincte = set(valori)
print(distincte)

tabel = {} # asociaza elemente din domeniu in codomeniu
for x in range (-2,3): # util pentru functii ex. x -> x^2 + 1
    tabel[x] = x*x +1
print(tabel)
