import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Parámetros del problema
H = 0.1
M_F = 1
t_F = 1
K_F = 0.01
K_AF = 0.02
t_AF = 1
J = 0.05
theta = 0

# Energía total
def energia(alpha, beta):
    return (- H * M_F * t_F * np.cos(theta - beta)
            + K_F * t_F * np.sin(beta)**2
            + K_AF * t_AF * np.sin(alpha)**2
            - J * np.cos(beta - alpha))

# Sistema de ecuaciones
def sistema(variables):
    alpha, beta = variables
    eq1 = 2 * K_AF * t_AF * np.sin(alpha) * np.cos(alpha) - J * np.sin(beta - alpha)
    eq2 = - H * M_F * t_F * np.sin(theta - beta) + 2 * K_F * t_F * np.sin(beta) * np.cos(beta) + J * np.sin(beta - alpha)
    return [eq1, eq2]

# Condiciones iniciales
conds_ini = [
    [0.01, 0.01],
    [np.pi - 0.01, 0.01],
    [0.01, np.pi - 0.01],
    [np.pi - 0.01, np.pi - 0.01]
]

soluciones = []
energias = []

print("Resultados en múltiplos de pi:")
for i, cond in enumerate(conds_ini):
    sol = fsolve(sistema, cond)
    alpha_sol, beta_sol = sol
    E = energia(alpha_sol, beta_sol)
    soluciones.append((alpha_sol, beta_sol))
    energias.append(E)
    print(f"Solución {i+1}: alpha = {alpha_sol/np.pi:.4f} * pi, beta = {beta_sol/np.pi:.4f} * pi, E = {E:.4f} J")

# Gráfico de energía
alphas = np.linspace(0, np.pi, 100)
betas = np.linspace(0, np.pi, 100)
Alpha, Beta = np.meshgrid(alphas, betas)
Energia = energia(Alpha, Beta)

fig, ax = plt.subplots(figsize=(8,6))
cp = ax.contourf(Alpha, Beta, Energia, 50, cmap='viridis')
plt.colorbar(cp, label='Energía (J)')

# Formateo de los ejes como múltiplos de pi
def pi_formatter(x, pos):
    frac = x / np.pi
    if np.isclose(frac, 0): return "0"
    elif np.isclose(frac, 1): return r"$\pi$"
    elif np.isclose(frac, 0.5): return r"$\pi/2$"
    elif np.isclose(frac, 1.5): return r"$3\pi/2$"
    else: return f"{frac:.2f}$\pi$"

ax.xaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(pi_formatter))

plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\beta$')
plt.title('Paisaje de energía E(alpha, beta)')

# Marcar soluciones encontradas
for (a, b) in soluciones:
    ax.plot(a, b, 'ro')
plt.show()
