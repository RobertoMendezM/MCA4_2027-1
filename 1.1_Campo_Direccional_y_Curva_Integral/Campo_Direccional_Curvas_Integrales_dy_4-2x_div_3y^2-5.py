# -*- coding: utf-8 -*-
"""
Campo Direccional de la EDO separable

                       y' = (4 - 2x)/(3y^2 - 5)               

Curso:  MCA 4 2027-1            

Tema:  Interpretaradecuadamente el campo direccional  e Identidicar 
       correctamente las curvas solución de la EDO

Referencias:
    * Edwards & Penney (2015). Differential Equations and Boundary 
      Value Problems, 5th edition, Pearson. pag. 32 
    
Software:
    Pyton 3.14.7
    Spyder 6.1.6
    
Autor  : Roberto Méndez Méndez    
Editado: 25 Ago 2026. v2 Actualizado a solve_ivp
"""

import numpy as np
from scipy.integrate import  solve_ivp
import matplotlib.pyplot as plt

# Definicónde la Derivadak
def f(x,y):
    return (4 - 2*x)/(3*y**2 - 5)

#  nx, ny = .3, .3
nx, ny = .3, .3
x = np.arange(-1.6, 5.4, nx)
y = np.arange(-3, 3, ny)

# MESHGRID
X, Y = np.meshgrid(x, y)

# Derivative
dy = f(X,Y)
dx = np.ones(X.shape)

# Normalización
dyu = dy/np.sqrt(dx**2 + dy**2)
dxu = dx/np.sqrt(dx**2 + dy**2)

# SOLUCIÓN NUMÉRICA

sol1 = solve_ivp(f, (0,4), [1.3], method='BDF')
sol2 = solve_ivp(f, (0,4), [1.2], method='LSODA')
sol3 = solve_ivp(f, (-0.8, 4.6), [-2.6], method='LSODA')
sol4 = solve_ivp(f,(-1.6, -0.09), [1.2])

# Gráfica Directional Field

plt.quiver(X,Y,dxu,dyu, color = "orange",  headwidth = 2)

# Gráficas de Curvas Integrales

plt.plot(sol1.t, sol1.y[0], color='brown')
plt.plot(sol2.t, sol2.y[0], color='salmon')
plt.plot(sol3.t, sol3.y[0], color='teal')
plt.plot(sol4.t, sol4.y[0], color='darkorchid')

plt.xticks(x, rotation = 60, fontsize=8)
plt.yticks(y, fontsize=8 )
plt.title(("Campo direccional y Curvas Integrales \n " 
           "y' = (4 - 2x)/(3y^2 - 5)"), color='blue',
          fontsize ='large')
plt.show()