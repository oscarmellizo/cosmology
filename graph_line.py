import numpy as np
import matplotlib.pyplot as plt

# Definir la ecuación de la línea y = 10.04x + 16.24
def linea(intercept, slope, x):
    return slope * x + intercept

# Crear un rango de valores de x para graficar
x = np.linspace(0, 1, 19) 

# Calcular los valores de y usando la fórmula de la línea
y = linea(16.24, 10.04, x)

print(y)

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 10.04x + 16.24', color='red')

# Etiquetas y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de la línea y = 10.04x + 16.24')
plt.grid(True)

# Añadir leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
