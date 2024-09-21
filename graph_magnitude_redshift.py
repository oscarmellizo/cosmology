import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Leer el archivo CSV con los datos
df = pd.read_csv('resultados.csv')  # Asegúrate de usar el nombre correcto de tu archivo

# Asignar los datos de las columnas REDSHIFT y PROMEDIO_R (o la columna de magnitud)
redshift = np.array(df['REDSHIFT'])
magnitud = np.array(df['PROMEDIO_R'])  

# Crear el gráfico de dispersión (scatter plot)
plt.figure(figsize=(8, 6))
plt.scatter(redshift, magnitud, color='blue', label='Redshift vs Magnitud')
# Aplicar escala logarítmica en el eje x
plt.xscale('log')

# Etiquetas y título
plt.xlabel('Redshift (z)')
plt.ylabel('Magnitud')
plt.title('Redshift vs Magnitud')
#plt.gca().invert_yaxis()  # Invertir el eje Y porque las magnitudes más bajas son más brillantes
plt.grid(True)

# Añadir leyenda
plt.legend()

# Mostrar la gráfica
plt.show()