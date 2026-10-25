"""
AERODINÁMICA II - TAREA 1
PARTE B - DIAGRAMA 3
Sistema Pitot-estático
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch

fig, ax = plt.subplots(figsize=(11, 6))

# Flujo de aire
for y in [1.2, 2.0, 2.8, 3.6, 4.4]:
    ax.annotate(
        "", xy=(3.2, y), xytext=(0.5, y),
        arrowprops=dict(arrowstyle="->", color="steelblue", lw=2)
    )

ax.text(0.6, 5.0, "Flujo de aire", fontsize=12, color="steelblue")

# Tubo Pitot
ax.add_patch(Rectangle((3.5, 2.3), 5.0, 1.4,
                       facecolor="lightgray", edgecolor="black", lw=2))

# Entrada frontal del Pitot
ax.plot([3.5, 3.5], [2.3, 3.7], color="black", lw=2)
ax.add_patch(Rectangle((3.5, 2.85), 3.5, 0.3,
                       facecolor="white", edgecolor="black"))

# Punto de estancamiento
ax.plot(3.5, 3.0, "ro", markersize=8)
ax.annotate(
    "Punto de estancamiento",
    xy=(3.5, 3.0), xytext=(1.0, 0.5),
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=11, color="red"
)

# Presión total
ax.annotate(
    "Presión total (p₀)",
    xy=(5.0, 3.0), xytext=(6.0, 4.8),
    arrowprops=dict(arrowstyle="->", color="darkgreen"),
    fontsize=12, color="darkgreen"
)

# Orificio de presión estática
ax.add_patch(Circle((6.5, 3.7), 0.09, color="purple"))

ax.annotate(
    "Presión estática (p)",
    xy=(6.5, 3.7), xytext=(7.0, 5.0),
    arrowprops=dict(arrowstyle="->", color="purple"),
    fontsize=12, color="purple"
)

# Etiquetas
ax.text(5.0, 1.5, "Tubo Pitot-estático", fontsize=13, weight="bold")
ax.text(4.0, 0.2, "Esquema conceptual (no a escala)", fontsize=10)

ax.set_xlim(0, 11)
ax.set_ylim(0, 6)
ax.set_aspect("equal")
ax.axis("off")

plt.title("Sistema Pitot-estático: medición de presiones", fontsize=14)
plt.tight_layout()

# Guardar imagen en la misma carpeta que este código
from pathlib import Path
ruta = Path(__file__).resolve().parent / "diagrama3_pitot.png"
plt.savefig(ruta, dpi=300, bbox_inches="tight")

plt.show()