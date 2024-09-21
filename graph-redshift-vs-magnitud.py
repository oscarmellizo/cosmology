import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Leer el archivo CSV y cargar los datos de las columnas REDSHIFT y PROMEDIO_R
df = pd.read_csv('resultados.csv') 

# Asignar los datos de las columnas REDSHIFT y PROMEDIO_R a arrays de numpy
redshift = np.array(df['REDSHIFT'])
magnitud = np.array(df['PROMEDIO_R'])

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
