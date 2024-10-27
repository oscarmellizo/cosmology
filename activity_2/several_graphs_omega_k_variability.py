import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from astropy.cosmology import LambdaCDM
from astropy import units as u

# Constante de Hubble fija
H0 = 67 * u.km / u.s / u.Mpc

# Rango de valores para Omega_m y Omega_lambda
Omega_m_values = [1 - i * 0.1 for i in range(11)]
Omega_lambda_values = [i * 0.1 for i in range(11)]

# Valores de Omega_k para variar desde -1 hasta 1
Omega_k_values = [i * 0.1 for i in range(-10, 11)]

# Crear la gráfica
plt.figure(figsize=(12, 8))

# Calcular la edad del universo para cada combinación de Omega_m, Omega_lambda y Omega_k
for Om0, Ode0 in zip(Omega_m_values, Omega_lambda_values):
    ages = []  # Lista para almacenar las edades del universo para cada Omega_k
    for Ok0 in Omega_k_values:
        # Ajuste del modelo cosmológico con el valor actual de Om0, Ode0 y Ok0
        cosmo = LambdaCDM(H0=H0, Om0=Om0, Ode0=Ode0 + Ok0)
        # Calcular la edad del universo en el presente (redshift = 0)
        age = cosmo.age(0)
        ages.append(age.value)
        
        print(f"Omega_m={Om0:.1f}, Omega_lambda={Ode0:.1f}, Omega_k={Ok0:.1f}, Edad del universo: {age.value:.2f} Gyr")
    
    # Graficar Omega_k vs Edad del Universo para la combinación actual de Omega_m y Omega_lambda
    plt.plot(Omega_k_values, ages, label=f"Omega_m={Om0:.1f}, Omega_lambda={Ode0:.1f}", linestyle='-')
    

# Personalización de la gráfica
plt.xlabel("Omega_k")
plt.ylabel("Edad del Universo (Gyr)")
plt.title("Edad del Universo vs Omega_k para distintas combinaciones de Omega_m y Omega_lambda")

# Mejorar el detalle del eje Y
plt.gca().yaxis.set_major_locator(MultipleLocator(1))  # Intervalo principal de 1 Gyr en el eje Y
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))  # Formato con dos decimales

plt.legend(loc="upper left", fontsize='small')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Mostrar la cuadrícula en mayor y menor escala
plt.show()
