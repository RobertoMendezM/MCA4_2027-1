# -*- coding: utf-8 -*-
"""
EDO Autónoma. Bifurcación tipo Fold / Saddle-Node 

                       x(t)' = mu - x(t)^2               

Curso: MCA 4              

Tema:  EDO de 1er orden. 
       Solución Analítica
                   - sin condición inicial (i.c.)
                   - con i.c. numérica
                   - con i.c. simbólica 

Referencias:
    Python for Mathematical Thinking (Editado) 2026 Singh Raman 
    página 341
    
Software:
    Pyton 3.14.7
    Spyder 6.1.6
    
Autor  : Roberto Méndez Méndez    
Editado: 28 Septiembre 2026. 
"""

import sympy as sp
from sympy import Eq, Derivative, dsolve

sp.init_printing(use_unicode=True)

sep = "=" * 40

# Variables
t = sp.symbols('t', real=True)
mu = sp.symbols('mu', negative=True)  

# Función 
x_fun = sp.Function('x')
x = x_fun(t)
x0_expr = x_fun(0)                       # x(0), reutilizable

# ---------------------
# EDO 
# ---------------------
ode = Eq(Derivative(x, t), mu - x**2)

# ---------------------
# Solución sin IC 
# ---------------------
sol_analytica = dsolve(ode)

print('\n'+ sep)
print("SOLUCIÓN ANALÍTICA DE  dx/dt = mu - x^2")
print(sep + '\n')

sp.pprint(sol_analytica)

# ---------------------
# Solución con IC numérica
# ---------------------
x0_num = 2
ic_num = {x0_expr: x0_num}

sol_analytica_ic_num = dsolve(ode, x, ics=ic_num)

print('\n'+ sep)
print(f"SOLUCIÓN ANALÍTICA DE  dx/dt = mu - x^2 \n con i.c. x0 = {x0_num}")
print(sep + '\n')

sp.pprint(sol_analytica_ic_num)

# ---------------------
# Solución con IC simbólica
# ---------------------
x0_sym = sp.symbols('x_0')
ic_sym = {x0_expr: x0_sym}

sol_analytica_ic_sym = dsolve(ode, x, ics=ic_sym)

print('\n'+ sep)
print(f"SOLUCIÓN ANALÍTICA DE  dx/dt = mu - x^2 \n con i.c. x0 = {x0_sym}")
print(sep + '\n')

sp.pprint(sol_analytica_ic_sym)