# -*- coding: utf-8 -*-
"""
  EDO LEY DE ENFRIAMIENTO DE NEWTON
  
        dT/dt = -k(T - T_amb)
  
  Solución Analítica y Numérica 
          
Curso: MCA 4 2027-1       

Software:
    Pyton 3.14.7
    Spyder 6.1.6

Autor : Roberto Méndez Méndez
Creado: 30 Agosto 2026
"""

import sympy as sp
from sympy import Eq, Derivative, dsolve
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt 

sp.init_printing(use_unicode=True)

print("=" * 40)
print("SOLUCIÓN ANALÍTICA DE  dT/dt = -k*(T - T_amb)")
print("=" * 40)

# Variables
t = sp.symbols('t')
k = sp.symbols('k', positive=True)
T = sp.Function('T')(t)
T_amb = sp.symbols('T_amb', real=True)

# Parámetro
T0 = 100  # Temperatura inicial [°C]

# EDO dT/dt = -k*(T - T_amb)
ode1 = Eq(Derivative(T, t), -k*(T - T_amb))

# Condiciones iniciales
ic = {T.subs(t, 0): T0}

# SOLUCIÓN ANALÍTICA
sol1_analytica = dsolve(ode1, T, ics = ic)

sp.pprint(sol1_analytica)


# SOLUCIÓN CON CONDICIONES INICIALES

def newton_cooling(t, T, k=0.1, T_amb=25):
    return -k * (T - T_amb)

# Parámetros
k = 0.1   # Constante de enfriamiento
T_amb = 25  # Temperatura ambiente [°C]

t_span = (0, 50)
t_eval = np.linspace(0, 50, 1000)
sol1 = solve_ivp(lambda t, T: newton_cooling(t, T, k, T_amb), t_span,
                 [T0], t_eval=t_eval)

plt.plot(sol1.t, sol1.y[0], 'b-', linewidth=2,label=f'T_ini = {T0}°C')
plt.axhline(y=T_amb, color='r', linestyle='--', 
                      label=f'T_amb = {T_amb}°C')
plt.title('Ley de Enfriamiento de Newton \n dT/dt = -k(T - T_amb) ')
plt.xlabel('Tiempo (s)')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.legend()


