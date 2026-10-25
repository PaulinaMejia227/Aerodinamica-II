"""
AERODINÁMICA II - TAREA 1
PARTE B - DIAGRAMA 2

Relaciones isentrópicas en función del número de Mach.
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. DATOS DEL PROBLEMA
gamma = 1.4
M = np.linspace(0, 3, 100)

# 2. RELACIONES ISENTRÓPICAS
T0_T = 1 + ((gamma - 1) / 2) * M**2
p0_p = T0_T ** (gamma / (gamma - 1))
rho0_rho = T0_T ** (1 / (gamma - 1))

# 3. CREACIÓN DE LA GRÁFICA
plt.figure(figsize=(10, 6))

plt.plot(M, T0_T, label="Temperatura T₀/T", linewidth=2)
plt.plot(M, p0_p, label="Presión p₀/p", linewidth=2)
plt.plot(M, rho0_rho, label="Densidad ρ₀/ρ", linewidth=2)

# 4. VALORES IMPORTANTES DE MACH
plt.axvline(0.3, color="gray", linestyle="--", label="M = 0.3")
plt.axvline(1.0, color="black", linestyle="--", label="M = 1")

# 5. PRESENTACIÓN
plt.title("Relaciones isentrópicas en función del número de Mach")
plt.xlabel("Número de Mach (M)")
plt.ylabel("Relación adimensional")
plt.xlim(0, 3)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# 6. GUARDAR LA IMAGEN
plt.savefig("relaciones_isentropicas.png", dpi=300)

# 7. MOSTRAR LA GRÁFICA
plt.show()