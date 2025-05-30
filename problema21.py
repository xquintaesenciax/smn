import numpy as np
import matplotlib.pyplot as plt

# Direcciones <111>
directions = [
    [1, 1, 1],
    [1, 1, -1],
    [1, -1, 1],
    [1, -1, -1],
    [-1, 1, 1],
    [-1, 1, -1],
    [-1, -1, 1],
    [-1, -1, -1],
]

# Normalizamos las direcciones
directions = np.array([v/np.linalg.norm(v) for v in directions])

# Configuración del gráfico
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Dibujamos los bordes del cubo
r = [-1, 1]
for s, e in [
    [[-1, -1, -1], [1, -1, -1]],
    [[-1, -1, -1], [-1, 1, -1]],
    [[-1, -1, -1], [-1, -1, 1]],
    [[1, 1, 1], [-1, 1, 1]],
    [[1, 1, 1], [1, -1, 1]],
    [[1, 1, 1], [1, 1, -1]],
    [[-1, 1, -1], [1, 1, -1]],
    [[-1, 1, -1], [-1, 1, 1]],
    [[1, -1, -1], [1, 1, -1]],
    [[1, -1, -1], [1, -1, 1]],
    [[-1, -1, 1], [1, -1, 1]],
    [[-1, -1, 1], [-1, 1, 1]]
]:
    ax.plot3D(*zip(s, e), color="gray", alpha=0.5)

# Dibujamos los vectores <111>
for vec in directions:
    ax.quiver(0, 0, 0, *vec, color="red", length=1.5, arrow_length_ratio=0.1)

# Ajustes finales
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Direcciones <111> en un cristal cúbico")
ax.view_init(elev=20, azim=30)
ax.set_box_aspect([1, 1, 1])
plt.show()