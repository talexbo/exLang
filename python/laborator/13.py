#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:11:40 2026

@author: alex
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:17:33 2026

@author: alex
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# clasa catalog
# materie asoc 
# grupa
# lista studenti  vida SAU lista_existenta (valori implicite pentru parametrii)
#                                           (lista = None) 
# 1) adauga student
# 2) modifica student
# 3) filtrare student
            # promovari 
            # nepromovati
# 4) media notelor
# 5) afisare

# def __init__ (materie (str), grupa (str), lista=None)
class Student:
    def __init__(self, nume, nota):
        
        if nume == "":
            raise ValueError("Numele nu poate fi vid.")
        if nota < 1 or nota > 10:
            raise ValueError("Nota trebuie sa fie intre și 10")
        self.nume = nume
        self.nota = nota
    
    def este_promovat(self):
        return self.nota >= 5
    
    def modifica_nota(self, nota_noua):
        if nota_noua < 1 or nota_noua > 10:
            raise ValueError("Nota trebuie sa intre de la 1 și 10")
        self.nota = nota_noua
        
    def __str__(self):
        return f"{self.nume}: {self.nota}"

class Catalog :
    def __init__(self, materie, grupa, studenti=None):
        if materie == "":
            raise ValueError("Materie nu poate fi text vid")
        
        if grupa == "":
            raise ValueError("Grupa nu poate fi text vid")
    
        self.materie = materie
        self.grupa = grupa
            
        if studenti is None:
            self.studenti = []
        else:
            for student in studenti:
                if str(type(student)) != "<class '__main__.Student'>":
                    raise ValueError("Nu toate elementele sunt de tip student")
            self.studenti = studenti
    
    def adauga_student(self, student):
        if str(type(student)) != "<class '__main__.Student'>":
            raise ValueError("nu este de tip student")
        self.studenti.append(student)
        
    def cauta_student(self,nume):
        for student in self.studenti:
            if student.nume == nume:
                return student
        return None
    
    def modifica_nota_student(self, nume, nota_noua):
        if nota_noua < 1 or nota_noua >10:
            raise ValueError("Nota nu este intre 1 si 10")
        student = self.cauta_student(nume)
        if student is None:
            raise ValueError("Studentul nu exista in catalog.")
        student.modifica_nota(nota_noua)
        
    def media_notelor(self):
        if len(self.studenti) == 0:
            return 0
        suma = 0
        for student in self.studenti:
            suma += student.nota
        return suma / len(self.studenti)
    
    def studenti_promovati(self):
        rezultat = []
        
        for student in self.studenti:
            if student.este_promovat():
                rezultat.append(student)
        return rezultat
    
    def studenti_nepromovati(self):
        rezultat = []
        for student in self.studenti :
            if not student.este_promovat():
                rezultat.append(student)
    
    def __str__(self):
        
        text = f"Catalog: {self.materie}, grupa{self.grupa}\n"
        
        if len(self.studenti) == 0:
            text += "Nu exista studenti la catalog."
        else:
            for student in self.studenti:
                text += str(student) + "\n"
        
        return text
    
s1 = Student("Popescu Maria", 8)
s2 = Student("Ionescu Vald", 10)
s3 = Student("Anton Ioana", 9)
c1 = Catalog("Algebra", "10LF101")
c1.adauga_student(s1)
c1.adauga_student(s2)
c1.adauga_student(s3)
c1.modifica_nota_student("Popescu Maria", 9)
print(c1) 
c1.modifica_nota_student("Ionescu Vald", 4)
c_promovati = c1.studenti_promovati()
for student in c_promovati:
    print(student)
