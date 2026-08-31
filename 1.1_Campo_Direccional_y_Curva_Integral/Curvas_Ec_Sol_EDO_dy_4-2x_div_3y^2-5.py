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
    
Software:
    Pyton 3.14.7
    Spyder 6.1.6

Editor:: Roberto Méndez Méndez    
Editado  25 Agosto 2026
"""
from sympy import symbols, Eq
from sympy import plot_implicit
import math

x, y = symbols('x y')

# Gráfica de la ecución solución para distintas c
 
p1 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, -6), (x, -2, 6),
              (y, -3, 3), line_color = 'darkgoldenrod', 
               title = "y^3 - 5y + x^2  - 4x = -6 ",
               fontsize = 'medium' );

p2 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, 0), (x, -2, 6),
              (y, -3, 3), line_color = 'darkorange', 
               title = "y^3 - 5y + x^2  - 4x = 0 ",
               fontsize = 'medium');

p3 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, .5), (x, -2, 6),
              (y, -3, 3), line_color = 'olivedrab', 
               title = "y^3 - 5y + x^2  - 4x = 0.5 ",
               fontsize = 'medium');

p4 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, 6), (x, -2, 6),
              (y, -3, 3), line_color = 'crimson', 
               title = "Gráficas de la soución  y^3 - 5y + x^2  - 4x = 6 ",
               fontsize = 'medium');

# Rectas donde y(t) no está definida en la EDO 
p5 = plot_implicit(Eq(y, math.sqrt(5/3)), (x, -2, 6),
              (y, -3, 3), line_color = 'black', show=False);

p6 = plot_implicit(Eq(y, -math.sqrt(5/3)), (x, -2, 6),
              (y, -3, 3), line_color = 'black', show=False);

# Gráfica conjunta, incluyendo las rectas donde y(t)  está 
# indefinida
p7 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, -6), (x, -2, 6),
              (y, -3, 3), line_color = 'darkgoldenrod', 
               title = ("Gráficas de la Solución  y^3 - 5y + x^2  - 4x = c \n"  
                       " con c = -6, 0, 0.5,6  e y(x)= +-(5/3)^1/2"), 
               fontsize = 'medium', show=False);
p7.append(p2[0]);
p7.append(p3[0]);
p7.append(p4[0]);
p7.append(p5[0]);
p7.append(p6[0]);

p7.save('Grafica_Ec_Sol_EDO_dy=(4-2x)/(3y^2-5).png');

p7.show()
