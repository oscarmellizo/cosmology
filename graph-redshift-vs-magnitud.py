import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo (sustitúyelos por los reales)
redshift = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
magnitud = np.array([22.1, 21.5, 21.0, 20.5, 20.2, 19.8])

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.scatter(redshift, magnitud, color='blue', label='Redshift vs Magnitud')

# Escala logarítmica en el eje x (redshift)
plt.xscale('log')

# Etiquetas y título
plt.xlabel('Redshift (z)')
plt.ylabel('Magnitud')
plt.title('Redshift vs Magnitud')
plt.grid(True)

# Añadir leyenda
plt.legend()

# Mostrar gráfica
plt.show()