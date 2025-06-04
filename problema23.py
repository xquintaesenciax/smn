import sympy as sp

H, M_F, t_F, K_F, K_AF, t_AF, J = sp.symbols("H M_F t_F K_F K_AF t_AF J", real=True)
alpha, beta, theta = sp.symbols("alpha beta theta", real=True)

E = - H * M_F * t_F * sp.cos(theta - beta) + K_F * t_F * sp.sin(beta)**2 + K_AF * t_AF * sp.sin(alpha)**2 - J * sp.cos(beta - alpha)

dE_dalpha= sp.diff(E, alpha)

print("dE/dalpha = ",dE_dalpha)

dE_dbeta = sp.diff(E, beta)

print("dE/dbeta = ", dE_dbeta)