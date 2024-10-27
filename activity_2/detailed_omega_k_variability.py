import matplotlib.pyplot as plt
from astropy.cosmology import LambdaCDM
from astropy import units as u

# Constantes cosmológicas fijas
H0 = 67 * u.km / u.s / u.Mpc   # Constante de Hubble fija
Om0 = 0.3                      # Densidad de materia
Ode0 = 0.7                     # Densidad de energía oscura

# Valores de Omega_k para variar desde -1 hasta 3 con pasos de 0.1
Omega_k_values = [i * 0.1 for i in range(-10, 31)]
ages = []

# Calcular la edad del universo para cada valor de Omega_k
for Ok0 in Omega_k_values:
    # Ajuste del modelo cosmológico con el valor actual de Ok0
    cosmo = LambdaCDM(H0=H0, Om0=Om0, Ode0=Ode0 + Ok0)  # Ajuste de Omega_lambda según Omega_k
    # Calcular la edad del universo en el presente (redshift = 0)
    age = cosmo.age(0)
    ages.append(age.value)
    
    # Mostrar en consola el par (Omega_k, Edad)
    print(f"Omega_k: {Ok0:.1f}, Edad del universo: {age.value:.2f} Gyr")

# Graficar Omega_k vs Edad del Universo
plt.figure(figsize=(10, 6))
plt.plot(Omega_k_values, ages, marker='o', color='b', linestyle='-')
plt.xlabel("Omega_k")
plt.ylabel("Edad del Universo (Gyr)")
plt.title("Edad del Universo vs Omega_k (con H0=67 km/s/Mpc, Omega_m=0.3)")
plt.grid(True)
plt.show()
