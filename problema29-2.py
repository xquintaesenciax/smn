import numpy as np
import matplotlib.pyplot as plt

# Parámetros físicos
R_parallel = 120  # Ohmios (cuando M // I)
R_perpendicular = 100  # Ohmios (cuando M ⟂ I)
K_shape = 1e5  # erg/cm^3
M = 1000       # emu/cm^3
H_vals = np.linspace(0, 300, 300)
H_crit = 2 * K_shape / M

# R para α = 0: la magnetización siempre está alineada con la corriente
def R_0(H_array):
    return np.full_like(H_array, R_parallel)

# R para α = π/2: la magnetización rota desde x hasta y con H
def R_90(H_array):
    R = np.empty_like(H_array)
    for i, h in enumerate(H_array):
        if h < H_crit:
            phi = np.arcsin(M * h / (2 * K_shape))
            R[i] = R_perpendicular + (R_parallel - R_perpendicular) * np.cos(phi)**2
        else:
            R[i] = R_perpendicular
    return R

# Calcular resistencias
R0_vals = R_0(H_vals)
R90_vals = R_90(H_vals)

# Calcular AMR en porcentaje
AMR_percent = (R0_vals - R90_vals) / R0_vals * 100

# Gráfico 1: Resistencias
plt.figure(figsize=(8, 5))
plt.plot(H_vals, R0_vals, label=r"$\alpha = 0$", color="orange")
plt.plot(H_vals, R90_vals, label=r"$\alpha = \pi/2$", color="orangered")
plt.axvline(H_crit, color="gray", linestyle="--", label=r"$H_\mathrm{crit}$")
plt.xlabel("Campo magnético $H$")
plt.ylabel("Resistencia $R(H)$")
plt.title("Dependencia angular de la resistencia (AMR)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Gráfico 2: AMR relativa en porcentaje
plt.figure(figsize=(8, 4))
plt.plot(H_vals, AMR_percent, color="blue")
plt.axvline(H_crit, color="gray", linestyle="--", label=r"$H_\mathrm{crit}$")
plt.xlabel("Campo magnético $H$")
plt.ylabel("AMR relativa [%]")
plt.title("Magnetorresistencia relativa vs. H")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
