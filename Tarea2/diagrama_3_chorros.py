import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================
# AERODINÁMICA II - TAREA 2
# PARTE B - DIAGRAMA 3
# ESQUEMAS DE CHORROS SUPERSÓNICOS
# ============================================

fig, axes = plt.subplots(3, 1, figsize=(12, 10))

colores = {
    "tobera": "navy",
    "chorro": "lightblue",
    "choque": "red",
    "expansion": "green"
}

# Geometría de la tobera
x_tobera = np.linspace(-3, 0, 150)
r_tobera = 0.5 + 0.4 * (
    (x_tobera + 3) / 3
)

# ============================================
# FUNCIÓN PARA DIBUJAR LA TOBERA
# ============================================

def dibujar_tobera(ax):

    ax.plot(
        x_tobera, r_tobera,
        color=colores["tobera"],
        linewidth=2.5
    )

    ax.plot(
        x_tobera, -r_tobera,
        color=colores["tobera"],
        linewidth=2.5
    )

    ax.fill_between(
        x_tobera,
        -r_tobera,
        r_tobera,
        color="lightgray",
        alpha=0.3
    )

    ax.axvline(
        0,
        color="gray",
        linestyle=":",
        alpha=0.7
    )

    ax.set_xlim(-3.2, 7)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect("equal")
    ax.grid(alpha=0.2)


# ============================================
# A) CHORRO SOBREEXPANDIDO
# pe < pb
# ============================================

ax = axes[0]
dibujar_tobera(ax)

x = np.linspace(0, 6, 300)

# Contracción inicial del chorro
r = 0.9 - 0.25 * np.exp(-x / 2) * np.sin(2 * x)

ax.plot(x, r, color="blue", linewidth=2)
ax.plot(x, -r, color="blue", linewidth=2)

ax.fill_between(
    x, -r, r,
    color=colores["chorro"],
    alpha=0.4
)

# Ondas de compresión / choque
for xi in [0.5, 2.0, 3.5]:
    ax.plot(
        [xi, xi + 0.8],
        [0.75, -0.75],
        color=colores["choque"],
        linewidth=1.5
    )

    ax.plot(
        [xi, xi + 0.8],
        [-0.75, 0.75],
        color=colores["choque"],
        linewidth=1.5
    )

ax.set_title(
    "A) Chorro sobreexpandido (pe < pb)\n"
    "Ondas de compresión y choques oblicuos"
)

# ============================================
# B) CHORRO ADAPTADO
# pe = pb
# ============================================

ax = axes[1]
dibujar_tobera(ax)

x = np.linspace(0, 6, 300)
r = np.ones_like(x) * 0.9

ax.plot(x, r, color="blue", linewidth=2)
ax.plot(x, -r, color="blue", linewidth=2)

ax.fill_between(
    x, -r, r,
    color=colores["chorro"],
    alpha=0.4
)

ax.set_title(
    "B) Chorro adaptado (pe = pb)\n"
    "Sin ondas de ajuste de presión"
)

# ============================================
# C) CHORRO SUBEXPANDIDO
# pe > pb
# ============================================

ax = axes[2]
dibujar_tobera(ax)

x = np.linspace(0, 6, 300)

# Expansión inicial del chorro
r = 0.9 + 0.35 * np.exp(-x / 3) * np.sin(1.8 * x)

ax.plot(x, r, color="blue", linewidth=2)
ax.plot(x, -r, color="blue", linewidth=2)

ax.fill_between(
    x, -r, r,
    color=colores["chorro"],
    alpha=0.4
)

# Abanicos de expansión
for angulo in np.linspace(-0.6, 0.6, 7):

    ax.plot(
        [0, 1.5],
        [0.9, 0.9 + angulo],
        color=colores["expansion"],
        linewidth=1
    )

    ax.plot(
        [0, 1.5],
        [-0.9, -0.9 - angulo],
        color=colores["expansion"],
        linewidth=1
    )

# Ondas de choque posteriores
for xi in [2.0, 4.0]:

    ax.plot(
        [xi, xi + 0.8],
        [0.7, -0.7],
        color=colores["choque"],
        linewidth=1.5
    )

    ax.plot(
        [xi, xi + 0.8],
        [-0.7, 0.7],
        color=colores["choque"],
        linewidth=1.5
    )

ax.set_title(
    "C) Chorro subexpandido (pe > pb)\n"
    "Abanicos de expansión y ondas de choque"
)

# ============================================
# FORMATO GENERAL
# ============================================

for ax in axes:
    ax.set_xlabel("Dirección del flujo")
    ax.set_ylabel("Posición transversal")

plt.suptitle(
    "Esquemas de chorros a la salida de una tobera de Laval",
    fontsize=15,
    fontweight="bold"
)

plt.tight_layout()

# ============================================
# GUARDAR IMAGEN
# ============================================

carpeta = Path(__file__).parent / "Diagramas"
carpeta.mkdir(exist_ok=True)

plt.savefig(
    carpeta / "diagrama_3_chorros.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nDIAGRAMA 3 GENERADO CORRECTAMENTE")
print("Sobreexpandida: pe < pb")
print("Adaptada: pe = pb")
print("Subexpandida: pe > pb")