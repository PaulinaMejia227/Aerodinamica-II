import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from pathlib import Path

# ==========================================
# AERODINÁMICA II - TAREA 2
# PARTE B - DIAGRAMA 1: TOBERA DE LAVAL
# ==========================================

gamma = 1.4

# Dimensiones de la tobera (mm)
D_garganta = 40
D_salida = 80
D_entrada = 90

L = 200
x_garganta = 80

# Coordenadas longitudinales
x = np.linspace(0, L, 501)

r_g = D_garganta / 2
r_e = D_salida / 2
r_i = D_entrada / 2

# Geometría convergente-divergente
r = np.zeros_like(x)

for i, xi in enumerate(x):

    if xi <= x_garganta:
        s = xi / x_garganta
        r[i] = r_g + (r_i - r_g) * (
            1 + np.cos(np.pi * s)
        ) / 2

    else:
        s = (xi - x_garganta) / (L - x_garganta)
        r[i] = r_g + (r_e - r_g) * (
            1 - np.cos(np.pi * s)
        ) / 2

# Relación de áreas
A_Astar = (r / r_g) ** 2

# Ecuación área-Mach
def relacion_area(M):
    return (1 / M) * (
        (2 / (gamma + 1)) *
        (1 + (gamma - 1) * M**2 / 2)
    ) ** ((gamma + 1) / (2 * (gamma - 1)))

# Cálculo de Mach
Mach = np.zeros_like(x)

for i, xi in enumerate(x):

    if np.isclose(A_Astar[i], 1, atol=1e-8):
        Mach[i] = 1.0

    elif xi < x_garganta:
        Mach[i] = brentq(
            lambda M: relacion_area(M) - A_Astar[i],
            0.001, 0.999999
        )

    else:
        Mach[i] = brentq(
            lambda M: relacion_area(M) - A_Astar[i],
            1.000001, 10
        )

# Relaciones isentrópicas
T_T0 = 1 / (1 + (gamma - 1) * Mach**2 / 2)
p_p0 = T_T0 ** (gamma / (gamma - 1))

# ==========================================
# GRÁFICAS
# ==========================================

fig, axes = plt.subplots(
    4, 1,
    figsize=(11, 12),
    sharex=True
)

# 1. Geometría
axes[0].plot(x, r, color="navy", linewidth=2)
axes[0].plot(x, -r, color="navy", linewidth=2)

axes[0].fill_between(
    x, -r, r,
    color="lightblue",
    alpha=0.4
)

axes[0].set_ylabel("Radio (mm)")
axes[0].set_title(
    "Tobera de Laval - Ae/A* = 4"
)
axes[0].set_aspect("equal", adjustable="datalim")
axes[0].grid(True)

# 2. Número de Mach
axes[1].plot(x, Mach, color="red", linewidth=2)
axes[1].set_ylabel("Mach (M)")
axes[1].grid(True)

# 3. Presión
axes[2].plot(x, p_p0, color="green", linewidth=2)
axes[2].set_ylabel("p/p₀")
axes[2].grid(True)

# 4. Temperatura
axes[3].plot(x, T_T0, color="purple", linewidth=2)
axes[3].set_ylabel("T/T₀")
axes[3].set_xlabel("Posición x (mm)")
axes[3].grid(True)

# Marcar la garganta
for ax in axes:
    ax.axvline(
        x_garganta,
        color="gray",
        linestyle="--",
        alpha=0.7
    )
    ax.set_xlim(0, L)

plt.tight_layout()

# Guardar imagen
carpeta = Path(__file__).parent / "Diagramas"
carpeta.mkdir(exist_ok=True)

plt.savefig(
    carpeta / "diagrama_1_tobera_laval.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Verificación
print("\nRESULTADOS DEL DIAGRAMA 1")
print("----------------------------")
print(f"Diámetro de garganta: {D_garganta} mm")
print(f"Diámetro de salida: {D_salida} mm")
print(f"Relación de áreas: {A_Astar[-1]:.2f}")
print(f"Mach en garganta: {Mach[np.argmin(r)]:.3f}")
print(f"Mach de salida: {Mach[-1]:.3f}")
print(f"Presión relativa de salida: {p_p0[-1]:.4f}")
print(f"Temperatura relativa de salida: {T_T0[-1]:.4f}")