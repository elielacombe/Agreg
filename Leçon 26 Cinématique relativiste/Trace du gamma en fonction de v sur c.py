#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:20:29 2024

@author: elacombe
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:59:47 2019

@author: jules.fillette
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate values for x and corresponding gamma values
x = np.linspace(0, 0.99, 100)
gamma = 1 / np.sqrt(1 - x**2)

# Generate a constant y array for comparison
y = np.linspace(1.10, 1.10, 100)

# Plot gamma and the constant y array
plt.plot(x, gamma, label='$\gamma$')
plt.plot(x, y, label='$y = 1.10$', linestyle='--')
plt.axis([0, 1, 0.9, 7])
plt.xlabel('vitesse (en unités de c)')
plt.ylabel('$\gamma = 1/\sqrt{1-(v/c)^2}$')
plt.title('$\gamma$ en fonction de $v/c$')
plt.grid(axis='both')
plt.legend()
plt.show()
