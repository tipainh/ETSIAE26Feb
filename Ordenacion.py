# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:10:39 2020

@author: TiagoFilipe
"""

n = 10

import random
lista1 = [random.randint(0,n-1) for i in range(n)]
print(lista1)

lista2 = list(reversed(range(n)))
print(lista2)

lista3 = [i for i in range(n)] 
lista3[random.choice(lista3)] = random.randint(0,n-1)
print(lista3)

lista4 = [i for i in range(n)]
pos_impar_lista4 = [lista4[i] for i in range(n) if i % 2 != 0]
pos_impar_lista4 = list(reversed(pos_impar_lista4))
j=0
for i in range(1,n,2):
    lista4[i] = pos_impar_lista4[j]
    j=j+1
print(lista4)

""" Intento de lista 4, por qué está mal?
lista4 = [i for i in range(n)] 
aux = lista4
for i in range(n):
    if i % 2 != 0:
        if i < (n/2):
            lista4[i] = lista4[-i]
        else:
            lista4[i] = aux[-i]
print(lista4)
"""
