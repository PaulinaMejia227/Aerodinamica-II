"""
AERODINÁMICA II
TAREA 1 - PARTE B

Diagrama 1: Cono de Mach
Número de Mach = 2
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# 1. DATOS DEL PROBLEMA
# --------------------------------------------------

M = 2.0

# Cálculo del semiángulo de Mach
mu = np.degrees(np.arcsin(1 / M))

print("DIAGRAMA 1: CONO DE MACH")
print(f"Número de Mach: {M}")
print(f"Semiángulo de Mach: {mu:.2f} grados")

# --------------------------------------------------
# 2. POSICIÓN DE LA FUENTE
# --------------------------------------------------

# Posición actual de la fuente supersónica
x_fuente = 200

# Posiciones de emisión de las ondas
centros = [0, 50, 100]

# Radios de los tres frentes de onda
radios = [100, 75, 50]

# --------------------------------------------------
# 3. CREACIÓN DE LA FIGURA
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(11, 7))

theta = np.linspace(0, 2 * np.pi, 500)

# Dibujar los tres frentes de onda
for i, (centro, radio) in enumerate(zip(centros, radios)):

    x = centro + radio * np.cos(theta)
    y = radio * np.sin(theta)

    ax.plot(
        x, y,
        linewidth=1.8,
        label=f"Frente de onda {i + 1}"
    )

    ax.plot(centro, 0, "ko", markersize=4)

# --------------------------------------------------
# 4. TRAYECTORIA DE LA FUENTE
# --------------------------------------------------

ax.plot(
    [0, x_fuente],
    [0, 0],
    "k--",
    linewidth=1.5,
    label="Trayectoria de la fuente"
)

# Posición actual
ax.plot(
    x_fuente, 0,
    "ro",
    markersize=9,
    label="Fuente supersónica"
)

# --------------------------------------------------
# 5. LÍMITES DEL CONO DE MACH
# --------------------------------------------------

# Pendiente de las líneas del cono
pendiente = np.tan(np.radians(mu))

x_cono = np.linspace(0, x_fuente, 300)

y_superior = (x_fuente - x_cono) * pendiente
y_inferior = -(x_fuente - x_cono) * pendiente

ax.plot(
    x_cono,
    y_superior,
    "r-",
    linewidth=2,
    label="Límites del cono de Mach"
)

ax.plot(
    x_cono,
    y_inferior,
    "r-",
    linewidth=2
)

# --------------------------------------------------
# 6. IDENTIFICACIÓN DE REGIONES
# --------------------------------------------------

ax.text(
    65, 125,
    "Región sin perturbación",
    fontsize=10
)

ax.text(
    65, 15,
    "Región alcanzada\npor las perturbaciones",
    fontsize=10,
    ha="center"
)

ax.text(
    130, -65,
    f"Semiángulo de Mach = {mu:.1f}°",
    fontsize=10
)

# --------------------------------------------------
# 7. FORMATO DEL DIAGRAMA
# --------------------------------------------------

ax.set_title(
    "Cono de Mach para una fuente supersónica (M = 2)",
    fontsize=14,
    fontweight="bold"
)

ax.set_xlabel("Posición horizontal (mm, escala ilustrativa)")
ax.set_ylabel("Posición vertical (mm, escala ilustrativa)")

ax.set_aspect("equal")
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="upper right")

ax.set_xlim(-115, 235)
ax.set_ylim(-155, 155)

plt.tight_layout()

# --------------------------------------------------
# 8. GUARDAR EL DIAGRAMA
# --------------------------------------------------

carpeta = Path(__file__).resolve().parent

plt.savefig(
    carpeta / "cono_mach.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Diagrama guardado correctamente: cono_mach.png")