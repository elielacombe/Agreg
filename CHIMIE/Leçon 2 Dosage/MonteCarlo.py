#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:58:42 2024

@author: elacombe
"""

import numpy as np

N = 100000        #nombre de tirages

A = np.random.uniform(10.8 , 11.2 , size=N)
B = np.random.uniform(21 , 22 , size=N)
C = np.random.triangular(2.5 , 2.7 , 2.9 , size=N)
D = np.random.uniform(16 , 16.7 , size=N)

X = A**2 * (B-C) / D

Xmoy = np.average(X)       
uX = np.std(X,ddof=1) 

print(f'Valeur de X : {Xmoy} (unité de X)')
print(f'Incertitude-type u(X) : {uX} (unité de X)')