#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:58:42 2024

@author: elacombe
"""

import numpy as np

N = 100000        #nombre de tirages

L_val = 8.50E-02#  m
D_val = 0.1 #  m
lamb_val = 6.35E-07 #  m

L_inc = 1e-3 #  m
D_inc = 1e-3 #  m
lamb_inc = 5.00E-09 #  m

L = np.random.uniform(L_val- L_inc, L_val+ L_inc, size=N)
D = np.random.uniform(D_val - D_inc, D_val +  D_inc, size=N)
lamb = np.random.uniform(lamb_val - lamb_inc , lamb_val + lamb_inc, size=N)

a = (2*lamb*((L/2)**2+D**2)**(1/2))/L # pas du réseau m

amoy = np.average(a)       
ua = np.std(a,ddof=1) 

print(f'Valeur de X : {amoy} (unité de X)')
print(f'Incertitude-type u(X) : {ua} (unité de X)')