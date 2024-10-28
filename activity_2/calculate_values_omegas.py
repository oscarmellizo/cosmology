import itertools

# Definir los rangos de valores para Omega_k, Omega_m y Omega_lambda con saltos de 0.1
Omega_k_values = [round(-0.3 + i * 0.1, 1) for i in range(7)]  # De -0.3 a 0.3
Omega_m_values = [round(i * 0.1, 1) for i in range(11)]  # De 0.0 a 1.0
Omega_lambda_values = [round(i * 0.1, 1) for i in range(11)]  # De 0.0 a 1.0

# Lista para almacenar las combinaciones válidas
valid_combinations = []

# Iterar sobre todos los valores de Omega_k
for Omega_k in Omega_k_values:
    # Iterar sobre todas las combinaciones posibles de Omega_m y Omega_lambda
    for Omega_m, Omega_lambda in itertools.product(Omega_m_values, Omega_lambda_values):
        # Verificar si la combinación cumple con la suma requerida
        if round(Omega_m + Omega_lambda + Omega_k, 1) == 1.0:
            valid_combinations.append((Omega_m, Omega_lambda, Omega_k))

# Mostrar las combinaciones válidas
for Omega_m, Omega_lambda, Omega_k in valid_combinations:
    print(f"Omega_m = {Omega_m}, Omega_lambda = {Omega_lambda}, Omega_k = {Omega_k}")
