import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from pathlib import Path

# ============================================
# AERODINÁMICA II - TAREA 2
# PARTE B - DIAGRAMA 2
# REGÍMENES DE OPERACIÓN
# ============================================

gamma = 1.4

# Geometría normalizada
x = np.linspace(0, 1, 601)
x_g = 0.4

# Relación de áreas: Ae/A* = 2
A = np.zeros_like(x)

for i, xi in enumerate(x):

    if xi <= x_g:
        s = xi / x_g
        A[i] = 1 + 1.5 * (1 + np.cos(np.pi * s)) / 2

    else:
        s = (xi - x_g) / (1 - x_g)
        A[i] = 1 + (1 - np.cos(np.pi * s)) / 2


# ============================================
# RELACIONES ISENTRÓPICAS
# ============================================

def area_mach(M):

    return (1 / M) * (
        (2 / (gamma + 1)) *
        (1 + (gamma - 1) * M**2 / 2)
    ) ** ((gamma + 1) / (2 * (gamma - 1)))


def calcular_mach(area, rama):

    if np.isclose(area, 1):
        return 1.0

    if rama == "sub":
        return brentq(
            lambda M: area_mach(M) - area,
            0.001, 0.999999
        )

    return brentq(
        lambda M: area_mach(M) - area,
        1.000001, 10
    )


def presion(M):

    return (
        1 + (gamma - 1) * M**2 / 2
    ) ** (-gamma / (gamma - 1))


# ============================================
# PRIMER CRÍTICO
# ============================================

M_critico = np.array([
    calcular_mach(a, "sub") for a in A
])

p_critico = presion(M_critico)


# ============================================
# OPERACIÓN ADAPTADA
# ============================================

M_adaptada = np.zeros_like(x)

for i, xi in enumerate(x):

    if xi <= x_g:
        M_adaptada[i] = calcular_mach(A[i], "sub")

    else:
        M_adaptada[i] = calcular_mach(A[i], "sup")

p_adaptada = presion(M_adaptada)


# ============================================
# OPERACIÓN SUBEXPANDIDA
# ============================================

# Dentro de la tobera, la distribución
# isentrópica coincide con la adaptada.
p_subexpandida = p_adaptada.copy()


# ============================================
# CHOQUE NORMAL EN EL DIVERGENTE
# ============================================

x_choque = 0.72

A_choque = np.interp(x_choque, x, A)

M1 = calcular_mach(A_choque, "sup")

# Mach después del choque normal
M2 = np.sqrt(
    (1 + (gamma - 1) * M1**2 / 2) /
    (gamma * M1**2 - (gamma - 1) / 2)
)

# Relación de presiones del choque
p2_p1 = 1 + (
    2 * gamma / (gamma + 1)
) * (M1**2 - 1)

# Presión total después del choque
p01 = 1.0

p1 = presion(M1) * p01
p2 = p1 * p2_p1

p02 = p2 / presion(M2)

# Área crítica equivalente después del choque
Astar2 = A_choque / area_mach(M2)

p_choque = np.zeros_like(x)

for i, xi in enumerate(x):

    if xi < x_choque:
        p_choque[i] = p_adaptada[i]

    else:
        M = calcular_mach(A[i] / Astar2, "sub")
        p_choque[i] = p02 * presion(M)


# ============================================
# GRÁFICA
# ============================================

plt.figure(figsize=(11, 7))

plt.plot(
    x, p_critico,
    label="Primer crítico",
    linewidth=2
)

plt.plot(
    x, p_choque,
    label="Choque dentro del divergente",
    linewidth=2
)

plt.plot(
    x, p_adaptada,
    label="Operación adaptada",
    linewidth=2
)

plt.plot(
    x, p_subexpandida,
    "--",
    label="Operación subexpandida",
    linewidth=2
)

plt.axvline(
    x_g,
    color="gray",
    linestyle=":",
    label="Garganta"
)

plt.axvline(
    x_choque,
    color="black",
    linestyle=":",
    label="Posición del choque"
)

plt.xlabel("Posición normalizada x/L")
plt.ylabel("Presión normalizada p/p₀")

plt.title(
    "Regímenes de operación de una tobera de Laval\n"
    "Ae/A* = 2"
)

plt.grid(True)
plt.legend()
plt.tight_layout()

# Guardar imagen
carpeta = Path(__file__).parent / "Diagramas"
carpeta.mkdir(exist_ok=True)

plt.savefig(
    carpeta / "diagrama_2_regimenes.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Resultados
print("\nRESULTADOS DEL DIAGRAMA 2")
print("----------------------------")
print(f"Relación de áreas de salida: {A[-1]:.2f}")
print(f"Mach antes del choque: {M1:.3f}")
print(f"Mach después del choque: {M2:.3f}")
print(f"Presión relativa adaptada: {p_adaptada[-1]:.4f}")
print(f"Presión relativa con choque: {p_choque[-1]:.4f}")