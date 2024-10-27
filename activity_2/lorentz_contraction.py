from astropy.constants import c  # velocidad de la luz
from astropy import units as u
import math

# Longitud en reposo (longitud del bus)
L0 = 20 * u.m  # 20 metros
# Longitud del garaje (longitud observada)
L = 10 * u.m   # 10 metros

# Aplicar la fórmula de la contracción de Lorentz para calcular la velocidad
v = c * math.sqrt(1 - (L / L0)**2)

# Convertir la velocidad a unidades prácticas (m/s)
v = v.to(u.m / u.s)

percentage_c = v * 100 / c

print(f"La velocidad necesaria para que el bus entre en el garaje es aproximadamente {v:.2f} que es un {percentage_c:2f}% de la velocidad de la luz")

print(f"La velocidad de la luz es {c:.2f}")

