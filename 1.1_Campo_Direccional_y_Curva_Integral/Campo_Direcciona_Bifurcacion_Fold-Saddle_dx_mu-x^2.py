# -*- coding: utf-8 -*-
"""
Campo Direccional de una EDO con Bifurcación tipo
Fold / Saddle-Node 

                       x(t)' = mu - x(t)^2               

Curso:              

Tema:  Bifurcaciones Codimension-1

Referencias:

    
Software:
    Pyton 3.14.7
    Spyder 6.1.6
    
Autor  : Roberto Méndez Méndez    
Editado: 30 Agosto 2026. 
"""

import numpy as np
import matplotlib.pyplot as plt

# Definicónde la Derivadak
def f(t,x, mu):
    return mu - x**2

#  nx, ny = .3, .3
nt, nx = .3, .3
t = np.arange(-1.6, 5.4, nt)
x = np.arange(-3, 3, nx)

# MESHGRID
T, X = np.meshgrid(t, x)

# Derivative
dt = np.ones_like(T)
dx = f(T,X, mu = -2)

# Normalización
N = np.sqrt(dt**2 + dx**2)
dxu = dx/N
dtu = dt/N

# Gráfica Directional Field
plt.quiver(T,X,dtu,dxu, color = "orange",  headwidth = 2)
plt.xticks(t, rotation = 60, fontsize=8)
plt.yticks(x, fontsize=8 )
plt.title("Campo Direccional \n x(t)' = mu - x(t)^2    mu < 0", color='blue',
          fontsize ='large')

plt.show()