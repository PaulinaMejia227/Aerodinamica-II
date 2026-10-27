# ============================================================
# AERODINÁMICA II - TAREA 3
# DIAGRAMA 2: PROPIEDADES DE UNA ONDA DE CHOQUE NORMAL
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
import csv
from pathlib import Path

# ------------------------------------------------------------
# 1. DATOS INICIALES
# ------------------------------------------------------------

gamma = 1.4

# Mach inicial de 1 a 5, incrementos de 0.25
M1 = np.arange(1, 5.01, 0.25)

# Carpeta donde se guardarán los resultados
carpeta = Path(__file__).resolve().parent / "diagramas"
carpeta.mkdir(exist_ok=True)

# ------------------------------------------------------------
# 2. CÁLCULO DE PROPIEDADES
# ------------------------------------------------------------

# Relación de presiones
p_ratio = 1 + (2 * gamma / (gamma + 1)) * (M1**2 - 1)

# Relación de densidades
rho_ratio = ((gamma + 1) * M1**2) / (
    (gamma - 1) * M1**2 + 2
)

# Relación de temperaturas
T_ratio = p_ratio / rho_ratio

# Número de Mach después del choque
M2 = np.sqrt(
    (1 + ((gamma - 1) / 2) * M1**2) /
    (gamma * M1**2 - (gamma - 1) / 2)
)

# ------------------------------------------------------------
# 3. TABLA DE RESULTADOS
# ------------------------------------------------------------

print("\nPROPIEDADES DE UNA ONDA DE CHOQUE NORMAL")
print("-" * 65)

print(
    f"{'M1':>8} {'p2/p1':>12} "
    f"{'rho2/rho1':>12} {'T2/T1':>12} {'M2':>10}"
)

for i in range(len(M1)):
    print(
        f"{M1[i]:8.2f} "
        f"{p_ratio[i]:12.4f} "
        f"{rho_ratio[i]:12.4f} "
        f"{T_ratio[i]:12.4f} "
        f"{M2[i]:10.4f}"
    )

# Guardar tabla en CSV
with open(
    carpeta / "tabla_propiedades_choque.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as archivo:

    escritor = csv.writer(archivo)

    escritor.writerow([
        "M1",
        "p2/p1",
        "rho2/rho1",
        "T2/T1",
        "M2"
    ])

    for i in range(len(M1)):
        escritor.writerow([
            round(float(M1[i]), 2),
            round(float(p_ratio[i]), 4),
            round(float(rho_ratio[i]), 4),
            round(float(T_ratio[i]), 4),
            round(float(M2[i]), 4)
        ])

# ------------------------------------------------------------
# 4. GENERACIÓN DE GRÁFICAS
# ------------------------------------------------------------

graficas = [
    (p_ratio, "Relación de presiones", "p₂/p₁",
     "grafica_presion.png"),

    (rho_ratio, "Relación de densidades", "ρ₂/ρ₁",
     "grafica_densidad.png"),

    (T_ratio, "Relación de temperaturas", "T₂/T₁",
     "grafica_temperatura.png"),

    (M2, "Número de Mach después del choque", "M₂",
     "grafica_mach.png")
]

for valores, titulo, etiqueta, nombre in graficas:

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        M1,
        valores,
        linewidth=2,
        marker="o",
        markersize=4
    )

    ax.set_title(titulo, fontsize=14, fontweight="bold")
    ax.set_xlabel("Número de Mach inicial (M₁)")
    ax.set_ylabel(etiqueta)

    ax.set_xticks(M1)
    ax.tick_params(axis="x", labelrotation=45)

    ax.grid(True, linestyle="--", alpha=0.5)

    fig.tight_layout()

    fig.savefig(
        carpeta / nombre,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

print("\nLas cuatro gráficas se guardaron correctamente.")
print("La tabla CSV también se generó.")
print(f"Ubicación: {carpeta}")