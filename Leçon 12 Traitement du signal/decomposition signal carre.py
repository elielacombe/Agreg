#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:01:34 2024

@author: elacombe
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Recomposition de signal carrÃ©


BasÃ© sur le programme "CarrÃ©" (LY16PPY001.PY) de la promotion 2016/2017 de l'ENS de Lyon.

Ce programme calcule et affiche la fonction "crÃ©neaux" Ã   partir de sa sÃ©rie de Fourier.
Le slider permet de changer l'ordre maximal de la sÃ©rie de Fourier (le nombre de sinusoÃ Â¯des sommÃ©ees).
ATTENTION : faire des simples clics sur le slider pour avoir un rendu plus fluide.

"""

"""
Bibliothèques
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as wd



"""
Variables
"""

N = 10    # Ordre max de la sÃ©rie de Fourier


"""
Fonctions de définition des coefficients et du signal théorique
"""
def A(n):   # Amplitude du n-iÃ¨me terme de la sÃ©rie
    return 0

def B(n):   # Amplitude du n-iÃ¨me terme de la sÃ©rie
    if n % 2 == 0:      # Si le nombre est pair:
        return 0
    else:                # Si le nombre est impair :
        return 1.0/n*4/np.pi

def carre(x):     # crÃ©neau thÃ©orique (masquÃ© par dÃ©faut)
    pi = np.pi
    deuxpi = 2*np.pi
    a = x % deuxpi # Le modulo est assez embÃ Âªtant
    if a < pi:
        return 1
    else:
        return -1


"""
Calcul et affichage de la sÃ©rie de Fourier
"""

fa,ax=plt.subplots(1)
plt.subplots_adjust(left=0.15, bottom=0.25,hspace=0.4)

x = np.arange(-4, 8, 0.001);

y = 0
for n in range(1,N+1):
    y = y + A(n)*np.cos(n*x) + B(n)*np.sin(n*x)    # On somme une Ã   une les composantes


y_creneau = [ carre(p) for p in x ]
plt.plot(x, y_creneau, "r-")


plt.axis([-4.0,8.0,-1.5,1.5])

l, =  plt.plot(x, y, "b-")

plt.title("Recomposition d'un signal avec une série de Fourier ",fontsize=18)
plt.xlabel("Temps (s)",fontsize=18)
plt.ylabel("Amplitude (1)",fontsize=18)
plt.grid()


slider_boite = plt.axes([0.2, 0.05, 0.6, 0.03])
slider_ordre = wd.Slider(slider_boite, 'Ordre maximal', 1, 200, valinit=N)

def update(val):
    slider_ordre.valtext.set_text(int(slider_ordre.val))
    y_aju = 0
    for n in range(1,int(slider_ordre.val)+1):
        y_aju = y_aju + A(n)*np.cos(n*x) + B(n)*np.sin(n*x)    # On somme une Ã   une les composantes
    fa.canvas.draw_idle()
    l.set_ydata(y_aju)

slider_ordre.on_changed(update)

plt.show()

#plt.savefig("image.png")