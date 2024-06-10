#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:52:39 2024

@author: elacombe
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:29:09 2024

@author: elacombe
"""
import numpy as np
import matplotlib.pyplot as plt

# Données expérimentales ou calculées pour l'enthalpie libre de la réaction en fonction de l'avancement
taux_eps = np.linspace(0, 1, 100)  # Avancement de la réaction de 0 à 1

#  On se place à pH = 4.8 initialement

V = 1 # L
R = 8.314 # J/(mol.K)
T= 298 # K
K_0=10**(-4.8)

def delta_G(eps):
    Ca = 1 # mol/L
    
    delta_G =R*T*np.log((eps*Ca*V)**2/(Ca*V-eps*Ca*V))

    return delta_G

# Tracer du graphique
plt.figure()
plt.plot(taux_eps, delta_G(taux_eps), label='Entropie libre de la réaction')
plt.title("Delta_r_G d'une réaction d'acide éthanoïque avec l'eau")
plt.xlabel("Avancement de la réaction (-)")
plt.ylabel("Enthalpie libre (kJ/mol)")

plt.show()
