import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ==========================================
# AERODINÁMICA II - TAREA 3
# DIAGRAMA 1: ONDA DE CHOQUE NORMAL
# ==========================================

fig, ax = plt.subplots(figsize=(12, 6))

# Región del flujo
ax.add_patch(Rectangle((0, 1), 10, 3,
                       facecolor="lightblue",
                       alpha=0.15))

# Onda de choque normal
ax.axvline(x=5, ymin=0.2, ymax=0.8,
           color="red", linewidth=4)

# Dirección del flujo
ax.arrow(1, 2.5, 2.5, 0,
         head_width=0.15,
         head_length=0.25,
         fc="blue", ec="blue")

ax.arrow(6, 2.5, 1.5, 0,
         head_width=0.15,
         head_length=0.25,
         fc="green", ec="green")

# Estado 1
ax.text(1, 3.5, "ESTADO 1 - SUPERSÓNICO",
        fontsize=12, fontweight="bold")

ax.text(1, 1.4,
        "M₁ > 1\n"
        "p₁: menor\n"
        "T₁: menor\n"
        "ρ₁: menor\n"
        "V₁: mayor",
        fontsize=12)

# Estado 2
ax.text(6, 3.5, "ESTADO 2 - SUBSÓNICO",
        fontsize=12, fontweight="bold")

ax.text(6, 1.4,
        "M₂ < 1\n"
        "p₂ ↑\n"
        "T₂ ↑\n"
        "ρ₂ ↑\n"
        "V₂ ↓",
        fontsize=12)

# Etiqueta del choque
ax.text(5.15, 4.2, "Onda de choque normal",
        color="red", fontsize=12)

# Configuración
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis("off")

plt.title("Diagrama 1. Onda de choque normal",
          fontsize=15, fontweight="bold")

plt.tight_layout()

# Guardar imagen
plt.savefig("diagramas/diagrama1_choque_normal.png",
            dpi=300, bbox_inches="tight")

plt.show()