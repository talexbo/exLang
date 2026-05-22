#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:11:40 2026

@author: alex
"""
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
        return rezultat
    
    def __str__(self):
        
        text = f"Catalog: {self.materie}, grupa{self.grupa}\n"
        
        if len(self.studenti) == 0:
            text += "Nu exista studenti la catalog."
        else:
            for student in self.studenti:
                text += str(student) + "\n"
        
        return text

class Produs:
    def __init__(self, denumire, pret, stoc):
        if denumire == "":
            raise ValueError("Numele nu poate fi vid.")
        if pret <= 0:
            raise ValueError("Pretul nu poate fi gratis.")
        if stoc < 0:
            raise ValueError("Stocul nu poate fi un nr. negativ.")
        self.denumire = denumire
        self.pret = pret
        self.stoc = stoc
    
    def este_disponibil(self):
        if self.stoc > 0:
            return True
        else:
            return False
    
    def modifica_pret(self, pret_nou):
        if pret_nou <= 0:
            raise ValueError("Pretul nu poate fi mai mic sau egal cu 0.")
        self.pret = pret_nou
    
    def modifica_stoc(self, stoc_nou):
        if stoc_nou <= 0:
            raise ValueError("Stocul nu poate fi mai mic decat 0.")
        self.stoc = stoc_nou
    
    def __str__(self):
        return f"{self.denumire}: stoc = {self.stoc}, pret unitar = {self.pret}"
    
class Magazin:
    def __init__(self, nume, produse=None):
        if nume == "":
            raise ValueError("Lipsa nume.")
        self.nume = nume
        if produse is None:
            self.produse = []
        else:
            for p in produse:
                if str(type(p)) != "<class '__main__.Produs'>":
                    raise ValueError("Nu toate elementele sunt de tip student")
            self.produse = produse
            
    def adauga_produs(self, p):
        if str(type(p)) != "<class '__main__.Produs'>":
            raise ValueError("Element nu de tip produs.")
        self.produse.append(p)
    
    def cauta_produs(self,cautat):
        for p in self.produse:
            if p.denumire == cautat:
                return True
            else: return False
    
    def modifica_pret_produs(self, denumire, pret_nou):
        for p in self.produse:
            if p.denumire == denumire:
                p.modifica_pret(pret_nou)
                
    def val_tot_stoc(self):
        tot = 0
        for p in self.produse:
            tot += p.stoc * p.pret
        return tot
        
    def __str__(self):
        text = f"{self.nume}\n"
        
        if len(self.produse) == 0:
            text += "Nu exista produse."
        else:
            for p in self.produse:
                text += str(p) + "\n"
        
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
c_nepromovati = c1.studenti_nepromovati()
print("-----------------------------")
print(c1)
print("-----------------------------")
for student in c_promovati:
    print(student)
print("-----------------------------")    
for student in c_nepromovati:
    print(student)
print("-----------------------------")
studenti_initiali = [
    Student("Ana", 9),
    Student("Mihai",4),
    Student("Ioana",7),
    Student("Radu",10)]

catalog = Catalog("Programare Python", "1A", studenti_initiali)
print(catalog)
nepromovati = catalog.studenti_nepromovati()
for s in nepromovati:
    print(s)
print("-----------------------------")
print("-----------------------------")

m1 = Magazin("Taraba SA")
banane = Produs("banane", 6, 10000)
mango = Produs("mango ", 10, 200)
m1.adauga_produs(banane)
m1.adauga_produs(mango)
print(m1)