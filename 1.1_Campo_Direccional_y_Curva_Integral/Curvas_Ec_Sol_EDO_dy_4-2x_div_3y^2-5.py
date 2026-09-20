# -*- coding: utf-8 -*-
"""
Gráficas de la solución implícita AMONG_US

                   y**3 - 5*y + x**2  - 4*x = C

para distintos C,  de la EDO separable

                 y' = (4 - 2x)/(3y^2 - 5)

Curso:  MCA 4  2027-1            

Tema:  Identificar adecuadamente las curvas solución de la EDO

Referencias:
    * Edwards & Penney (2015). Differential Equations and Boundary 
      Value Problems, 5th edition, Pearson. pag. 32 
    * Motas: Cuaderno Kuma, Astronauta 19 Sep 2026  
    
Software:
    Pyton 3.14.7
    Spyder 6.1.6

Editor:: Roberto Méndez Méndez    
Editado  20 Septiembre 2026
"""
from sympy import symbols, Eq
from sympy import plot_implicit
import math

x, y = symbols('x y')


# Rectas donde y(t) no está definida en la EDO 
l1 = plot_implicit(Eq(y, math.sqrt(5/3)), (x, -2, 6),
              (y, -3, 3), line_color = 'black', show=False)

l2 = plot_implicit(Eq(y, -math.sqrt(5/3)), (x, -2, 6), (y, -3, 3), linestyle='dashed', 
    line_color= 'black', 
    show=False)

mis_colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
# Gráfica de la ecución solución para distintas c
# c < c2 = -10(5/3)^(1/2) - 4 = -8.3033
c = -8.37
p1 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, c), (x, -2, 6),
              (y, -3, 3), line_color = mis_colores[0], 
               title = f"y^3 - 5y + x^2  - 4x = {c} ",
               fontsize = 'medium', 
               xlabel = "", ylabel="", show=False);
p1.append(l2[0])
p1.show()

c = -6
p2 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, c), (x, -2, 6),
              (y, -3, 3), line_color = mis_colores[1], 
               title = f"y^3 - 5y + x^2  - 4x = {c} ",
               fontsize = 'medium');
c = -4
p3 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, c), (x, -2, 6),
              (y, -3, 3), line_color = mis_colores[2], 
               title = f"y^3 - 5y + x^2  - 4x = {c} ",
               fontsize = 'medium');

c = -1
p4 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, c), (x, -2, 6),
              (y, -3, 3), line_color = mis_colores[3], 
               title = f" y^3 - 5y + x^2  - 4x = {c} ",
               fontsize = 'medium');

# c > c1 = 10(5/3)^(1/2) - 4 = 0.3033
c = 4
p5 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, c), (x, -2, 6),
              (y, -3, 3), line_color = mis_colores[4], 
               title = f" y^3 - 5y + x^2  - 4x = {c} ",
               fontsize = 'medium', points=100);

#Gráfica conjunta, incluyendo las rectas donde y(t)  está indefinida
p7 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, -8.37), (x, -2, 6),
              (y, -3, 3), line_color = mis_colores[0], 
              title = ("Gráficas de la Solución  y^3 - 5y + x^2  - 4x = c \n"  
                      " con c = -8.37, -6, -4, -1, 4  e y(x)= +-(5/3)^1/2"),
              ylabel="",
              fontsize = 'medium', points=120, show=False);
for g in (p2, p3, p4, p5, l1, l2):
    p7.extend(g)   
p7.save("Grafica_Ec_Sol_EDO_dy=(4-2x)÷(3y^2-5).png")




