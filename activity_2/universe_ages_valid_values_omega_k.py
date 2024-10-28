from astropy.cosmology import LambdaCDM
from astropy import units as u
import pandas as pd
import itertools

# Constante de Hubble fija
H0_value = 67  # en km/s/Mpc
H0 = H0_value * u.km / u.s / u.Mpc

# Definir los rangos de valores para Omega_k, Omega_m y Omega_lambda con saltos de 0.1
Omega_k_values = [round(-0.3 + i * 0.1, 1) for i in range(7)]  # De -0.3 a 0.3
Omega_m_values = [round(i * 0.1, 1) for i in range(11)]  # De 0.0 a 1.0
Omega_lambda_values = [round(i * 0.1, 1) for i in range(11)]  # De 0.0 a 1.0

# Lista para almacenar las combinaciones válidas y sus edades del universo
results = []

# Iterar sobre todos los valores de Omega_k
for Omega_k in Omega_k_values:
    # Iterar sobre todas las combinaciones posibles de Omega_m y Omega_lambda
    for Omega_m, Omega_lambda in itertools.product(Omega_m_values, Omega_lambda_values):
        # Verificar si la combinación cumple con la suma requerida
        if round(Omega_m + Omega_lambda + Omega_k, 1) == 1.0:
            # Crear el modelo cosmológico con la combinación actual de parámetros
            cosmo = LambdaCDM(H0=H0, Om0=Omega_m, Ode0=Omega_lambda)
            # Calcular la edad del universo en el presente (redshift = 0)
            age = cosmo.age(0).value  # Obtener el valor en Gyr
            # Añadir la combinación y la edad a la lista de resultados
            results.append([H0_value, Omega_m, Omega_lambda, Omega_k, age])

# Crear un DataFrame para mostrar los resultados en formato tabular
df_results = pd.DataFrame(results, columns=["H0", "Omega_m", "Omega_lambda", "Omega_k", "Edad del Universo (Gyr)"])

# Mostrar la tabla de resultados
df_results.to_csv("resultados_edad_universo.csv", index=False)
print("La tabla completa se ha guardado en 'resultados_edad_universo.csv'.")
