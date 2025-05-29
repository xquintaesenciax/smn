import numpy as np

def contar_ligaduras(matriz):
    """
    Cuenta las ligaduras AA, BB y AB en una matriz 2D de caracteres 'A' y 'B'.
    Solo cuenta vecinos horizontales (incluyendo entre bordes de filas)
    y también considera ligaduras entre los bordes de las filas.
    """
    N_AA, N_BB, N_AB = 0, 0, 0
    filas, cols = matriz.shape

    for i in range(filas):
        for j in range(cols):
            actual = matriz[i, j]
            # Ligadura horizontal derecha
            derecha = matriz[i, (j + 1) % cols]  # Usamos módulo para bordes
            if actual == derecha == 'A':
                N_AA += 1
            elif actual == derecha == 'B':
                N_BB += 1
            elif {actual, derecha} == {'A', 'B'}:
                N_AB += 1

    return N_AA , N_BB , N_AB 

# Ejemplo de prueba
matriz_ejemplo = np.array([
    list("ABBBABBA"),
    list("ABBABAAA"),
    list("AAAAAABB"),
    list("BBBABBAA"),
    list("BABABBAB"),
    list("BBAABBBA"),
    list("ABABAAAB"),
    list("BABBABAA")
])

N_AA, N_BB, N_AB = contar_ligaduras(matriz_ejemplo)
N_A = np.count_nonzero(matriz_ejemplo == 'A')
N_B = np.count_nonzero(matriz_ejemplo == 'B')

print(N_A, N_B, N_AA, N_BB, N_AB)