# ============================================================
# AERODINÁMICA II - TAREA 3
# DIAGRAMA 3: CHOQUE NORMAL EN UNA TOBERA DE LAVAL
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.optimize import brentq

# ------------------------------------------------------------
# 1. PARÁMETROS
# ------------------------------------------------------------

gamma = 1.4

# Coordenada longitudinal
x = np.linspace(0, 10, 501)

# Garganta y posición del choque
x_garganta = 4.0
x_choque = 7.0

# Carpeta de resultados
carpeta = Path(__file__).resolve().parent / "diagramas"
carpeta.mkdir(exist_ok=True)

# ------------------------------------------------------------
# 2. GEOMETRÍA DE LA TOBERA
# ------------------------------------------------------------

def area(x):
    if x <= x_garganta:
        return 1 + 0.10 * (x_garganta - x)**2
    else:
        return 1 + 0.08 * (x - x_garganta)**2


# ------------------------------------------------------------
# 3. RELACIONES ISENTRÓPICAS
# ------------------------------------------------------------

def relacion_area(M):
    return (1 / M) * (
        (2 / (gamma + 1)) *
        (1 + ((gamma - 1) / 2) * M**2)
    )**((gamma + 1) / (2 * (gamma - 1)))


def mach_desde_area(A_ratio, supersonico=False):

    if abs(A_ratio - 1) < 1e-9:
        return 1.0

    if supersonico:
        return brentq(
            lambda M: relacion_area(M) - A_ratio,
            1.000001, 10
        )

    return brentq(
        lambda M: relacion_area(M) - A_ratio,
        0.000001, 0.999999
    )


def presion_isentropica(M):
    return (
        1 + ((gamma - 1) / 2) * M**2
    )**(-gamma / (gamma - 1))


# ------------------------------------------------------------
# 4. CONDICIONES ANTES DEL CHOQUE
# ------------------------------------------------------------

A_choque = area(x_choque)

M1 = mach_desde_area(A_choque, supersonico=True)

p1_p01 = presion_isentropica(M1)

# Relación de presión a través del choque
p2_p1 = 1 + (
    2 * gamma / (gamma + 1)
) * (M1**2 - 1)

# Mach después del choque
M2 = np.sqrt(
    (1 + ((gamma - 1) / 2) * M1**2) /
    (gamma * M1**2 - (gamma - 1) / 2)
)

p2_p01 = p1_p01 * p2_p1

# Presión total después del choque
p02_p01 = p2_p01 / presion_isentropica(M2)

# Nueva área crítica equivalente después del choque
A_estrella_2 = A_choque / relacion_area(M2)

# ------------------------------------------------------------
# 5. PERFIL DE PRESIÓN
# ------------------------------------------------------------

presion = np.zeros_like(x)
mach = np.zeros_like(x)

for i, xi in enumerate(x):

    A_local = area(xi)

    if xi < x_garganta:

        M = mach_desde_area(A_local)

        p = presion_isentropica(M)

    elif xi <= x_choque:

        M = mach_desde_area(
            A_local,
            supersonico=True
        )

        p = presion_isentropica(M)

    else:

        M = mach_desde_area(
            A_local / A_estrella_2
        )

        p = p02_p01 * presion_isentropica(M)

    mach[i] = M
    presion[i] = p

# ------------------------------------------------------------
# 6. GRÁFICA
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(12, 6))

# Perfil de presión
ax.plot(
    x,
    presion,
    color="navy",
    linewidth=2.5,
    label="Presión estática p/p₀₁"
)

# Salto discontinuo de presión en el choque
ax.plot(
    [x_choque, x_choque],
    [p1_p01, p2_p01],
    color="red",
    linewidth=3,
    label="Choque normal"
)

# Garganta
ax.axvline(
    x_garganta,
    color="green",
    linestyle="--",
    linewidth=2,
    label="Garganta (M = 1)"
)

# Posición del choque
ax.axvline(
    x_choque,
    color="red",
    linestyle=":",
    alpha=0.6
)

# Zonas del flujo
ax.axvspan(
    x_garganta,
    x_choque,
    color="orange",
    alpha=0.12
)

ax.axvspan(
    x_choque,
    10,
    color="lightblue",
    alpha=0.18
)

# Etiquetas
ax.text(
    4.4, 0.85,
    "Zona supersónica\nM > 1",
    fontsize=11
)

ax.text(
    7.5, 0.85,
    "Zona subsónica\nM < 1",
    fontsize=11
)

ax.annotate(
    "Aumento brusco\nde presión",
    xy=(x_choque, p2_p01),
    xytext=(7.6, 0.55),
    arrowprops=dict(
        arrowstyle="->",
        color="red"
    ),
    fontsize=10,
    color="darkred"
)

# Configuración
ax.set_title(
    "Diagrama 3. Choque normal en una tobera de Laval",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Posición longitudinal en la tobera")
ax.set_ylabel("Relación de presión estática p/p₀₁")

ax.set_xlim(0, 10)
ax.set_ylim(0, 1.05)

ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="lower left")

plt.tight_layout()

# Guardar imagen
plt.savefig(
    carpeta / "diagrama3_tobera.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nDIAGRAMA 3 - TOBERA DE LAVAL")
print("-" * 45)
print(f"Mach antes del choque: {M1:.4f}")
print(f"Mach después del choque: {M2:.4f}")
print(f"Presión antes del choque: {p1_p01:.4f}")
print(f"Presión después del choque: {p2_p01:.4f}")
print(f"Recuperación de presión total: {p02_p01:.4f}")

print("\nDiagrama guardado correctamente.")

plt.show()