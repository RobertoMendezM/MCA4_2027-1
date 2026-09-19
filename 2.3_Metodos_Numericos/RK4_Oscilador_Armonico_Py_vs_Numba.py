# -*- coding: utf-8 -*-
"""
Solución Numérica (RK4) del Oscilador armónico amortiguado forzado 

        y'' + 2γ y' + ω₀² y = F·cos(ω_d t)

reescrito como un sistema de 1er orden:
    
        y' = v
        v' = F·cos(ω_d t) - 2γ·v - ω₀²·y

Curso: MCA4
       
Sección Temario: 2.3 Métodos Numéricos

Temas: 
    Uso de Métodos Numérico Runge Kutta
    Uso de Numba para acelerar calculos
    Comparativo en tiempos de ejecución para RK4 con python "normal" 
    y RK4 con Numba
 
Autor: Deepseek
Editor: Roberto Méndez Mëndez
Creación: 18 Septiembre 2026
Edición:  19 Septiembre 2026 
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from numba import njit

# ---------- Sistema de EDOs ----------
@njit(cache=True, fastmath=True)
def f(t, y, v, gamma, w0, F, wd):
    return v, F*np.cos(wd*t) - 2.0*gamma*v - w0*w0*y

# ---------- RK4 en Python puro ----------
def rk4_python(y0, v0, t0, tf, h, gamma, w0, F, wd):
    n = int((tf - t0) / h) + 1
    t = np.empty(n)
    y = np.empty(n)
    v = np.empty(n)
    t[0], y[0], v[0] = t0, y0, v0
    for i in range(n - 1):
        ti, yi, vi = t[i], y[i], v[i]
        k1y, k1v = f(ti, yi, vi, gamma, w0, F, wd)
        k2y, k2v = f(ti + h/2, yi + h/2*k1y, vi + h/2*k1v, gamma, w0, F, wd)
        k3y, k3v = f(ti + h/2, yi + h/2*k2y, vi + h/2*k2v, gamma, w0, F, wd)
        k4y, k4v = f(ti + h,   yi + h*k3y,   vi + h*k3v,   gamma, w0, F, wd)
        y[i+1] = yi + h/6*(k1y + 2*k2y + 2*k3y + k4y)
        v[i+1] = vi + h/6*(k1v + 2*k2v + 2*k3v + k4v)
        t[i+1] = ti + h
    return t, y, v

# ---------- RK4 con Numba (la función f también está compilada) ----------
@njit(cache=True, fastmath=True)
def rk4_numba(y0, v0, t0, tf, h, gamma, w0, F, wd):
    n = int((tf - t0) / h) + 1
    t = np.empty(n)
    y = np.empty(n)
    v = np.empty(n)
    t[0], y[0], v[0] = t0, y0, v0
    for i in range(n - 1):
        ti, yi, vi = t[i], y[i], v[i]
        k1y, k1v = f(ti, yi, vi, gamma, w0, F, wd)
        k2y, k2v = f(ti + h/2, yi + h/2*k1y, vi + h/2*k1v, gamma, w0, F, wd)
        k3y, k3v = f(ti + h/2, yi + h/2*k2y, vi + h/2*k2v, gamma, w0, F, wd)
        k4y, k4v = f(ti + h,   yi + h*k3y,   vi + h*k3v,   gamma, w0, F, wd)
        y[i+1] = yi + h/6*(k1y + 2*k2y + 2*k3y + k4y)
        v[i+1] = vi + h/6*(k1v + 2*k2v + 2*k3v + k4v)
        t[i+1] = ti + h
    return t, y, v

# ---------- Parámetros ----------
y0, v0 = 1.0, 0.0
t0, tf = 0.0, 50.0
h = 1e-5              # 5 millones de pasos
gamma, w0, F, wd = 0.1, 2.0, 0.5, 1.5

# Compilación (JIT) — primera llamada
_ = rk4_numba(y0, v0, t0, t0+h, h, gamma, w0, F, wd)

# ---------- Benchmark ----------
print("\nTiempos de Ejecución: \n ")

t1 = time.perf_counter()
t_np, y_np, v_np = rk4_numba(y0, v0, t0, tf, h, gamma, w0, F, wd)
t2 = time.perf_counter()
print(f"\tCon Numba : {t2 - t1:.3f} s")

t1 = time.perf_counter()
t_py, y_py, v_py = rk4_python(y0, v0, t0, tf, h, gamma, w0, F, wd)
t2 = time.perf_counter()
print(f"\tCon Python: {t2 - t1:.3f} s")

# Verificación de Error 
err = np.max(np.abs(y_np - y_py))
print(f"\nError máximo entre ambos métodos: {err:.2e}")

# Grafica Comparativa del Resultado con ambos esquemas 
plt.plot(t_np[::1000], y_np[::1000], color = "orange", label="Numba RK4")
plt.plot(t_py[::1000], y_py[::1000], label="Python RK4", 
         linestyle = "dotted", linewidth=2)
plt.xlabel("t"); plt.ylabel("y(t)")
plt.title("Oscilador armónico amortiguado forzado", pad=8, fontsize=18)
plt.legend(); plt.grid(True)
plt.show()

