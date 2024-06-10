#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:29:09 2024

@author: elacombe
"""
import numpy as np 
import matplotlib.pyplot as plt

y0 = 1 # mol/l
tf = 3000 # s
n = 3000 # nb de pas 
t0 = 0 # s
k = 0.001 # s-1

def euler(F,t0,tf,y0, n):
    """Données:
    F(y,t) une fonction
    t0,t1 deux réels avec t0 < t1
    y0 un réel
    n un entier
    Résultat: le tuple constitué de la liste des temps [t0,...,tn] et la liste des (qui constituent une approximation de la solution y sur [t0,tf]
    de l’ED y’=F(y,t) avec la condition initiale y(t0) = y0
    """
    h = (tf-t0)/n
    y = y0
    t = t0
    Y = [y0]
    T = [t0]
    for k in range(n): # n itérations donc n+1 points
        y = y + h*F(y,t)
        t = t + h
        Y.append(y)
        T.append(t)
    
    return T,Y

def F(y,t):
    return -k*y

T,Y = euler(F,t0,tf,y0,n)

plt.plot(T,Y)
plt.title("Concentration versus time")
plt.xlabel("temps (s)")
plt.ylabel("Concentration (mol/L)")

plt.show()

