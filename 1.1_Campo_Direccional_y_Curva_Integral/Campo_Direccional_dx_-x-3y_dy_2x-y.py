# -*- coding: utf-8 -*-
"""
Campo Direccional de una SEDO 

                       x'(t) = -x - 3y
                       
                       y'(t) = 2x - y 

 con punto de equilibrio tipo foco estable
             
Motivación: Tesis Maestria
            Prerequsito Fractales              

Tema:  Linear Stability Analysis

Referencias:
    Python for Mathematical Thinking (Editado) 2026 Singh Raman 
    página 340
    
Software:
    Pyton 3.14.7
    Spyder 6.1.6
    
Autor : Roberto Méndez Méndez   
Creado: 1 Septiembre 2026. 
"""

import numpy as np
import matplotlib.pyplot as plt

# Definicónd e la Derivada
def X(x,y):
    return -x - 3*y

def Y(x,y):
    return 2*x - y

#  nx, ny = .3, .3
nt, nx = .3, .3
x = np.arange(-4, 4, nt)
y = np.arange(-3, 3, nx)

# MESHGRID
Xp, Yp = np.meshgrid(x, y)

# Derivative
dx = X(Xp,Yp)
dy = Y(Xp,Yp)

# Normalización
N = np.sqrt(dx**2 + dy**2)
dxu = dx/N
dyu = dy/N

# Gráfica Directional Field
plt.quiver(Xp,Yp,dxu,dyu, color = "orange",  headwidth = 2)
plt.xticks(x, rotation = 60, fontsize=8)
plt.yticks(y, fontsize=8 )
plt.title(('Campo Direccional del SDEO \n '+
           "x'(t) = -x - 3y    y'(t) = 2x - y"), color='blue',
          fontsize ='large')
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.axis('scaled') 
plt.show()