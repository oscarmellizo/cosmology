import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

# Leer el archivo CSV y cargar los datos de las columnas REDSHIFT y PROMEDIO_R
df = pd.read_csv('resultados.csv') 

# Asignar los datos de las columnas REDSHIFT y PROMEDIO_R a arrays de numpy
redshift = np.array(df['REDSHIFT'])
magnitud = np.array(df['PROMEDIO_R'])
print(redshift)
print(magnitud)

# Calcular la línea de regresión
slope, intercept, r_value, p_value, std_err = stats.linregress(redshift, magnitud)

# Predicciones basadas en la recta obtenida
linea_ajustada = slope * redshift + intercept

# Crear la gráfica con la línea ajustada
plt.figure(figsize=(8, 6))
plt.scatter(redshift, magnitud, color='blue', label='Datos Originales')
plt.plot(redshift, linea_ajustada, color='red', label=f'Línea Ajustada: y = {slope:.2f}x + {intercept:.2f}')

# Escala logarítmica en el eje x (redshift)
plt.xscale('log')

# Mostrar la ecuación de la línea y el valor de R² en la gráfica
plt.text(0.4, 21.8, f'Ecuación: y = {slope:.2f}x + {intercept:.2f}', fontsize=12, color='red')
plt.text(0.4, 21.6, f'R² = {r_value**2:.4f}', fontsize=12, color='red')

# Etiquetas y título
plt.xlabel('Redshift (z)')
plt.ylabel('Magnitud')
plt.title('Redshift vs Magnitud con Línea de Regresión')
plt.grid(True)

# Añadir leyenda
plt.legend()

# Mostrar gráfica
plt.show()

# Mostrar ecuación y valor de R² en la consola
print(f"Ecuación de la línea ajustada: y = {slope:.2f}x + {intercept:.2f}")
print(f"R² = {r_value**2:.4f}")
