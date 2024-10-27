import matplotlib.pyplot as plt
from astropy.cosmology import LambdaCDM
from astropy import units as u

# Constante de Hubble fija
H0 = 67 * u.km / u.s / u.Mpc

# Valores de Omega_m que van desde 0 hasta 5 con pasos de 0.1
Omega_m_values = [i * 0.1 for i in range(51)]
Omega_lambda_values = []
ages = []

# Calcular la edad del universo para cada valor de Omega_m y mostrar en consola
for Om0 in Omega_m_values:
    # Omega_lambda se calcula para mantener un universo plano: Omega_m + Omega_lambda = 1
    Ode0 = 1 - Om0
    Omega_lambda_values.append(Ode0)
    
    # Crear el modelo cosmológico con el valor actual de Om0 y Ode0
    cosmo = LambdaCDM(H0=H0, Om0=Om0, Ode0=Ode0)
    # Calcular la edad del universo en el presente (redshift = 0)
    age = cosmo.age(0)
    ages.append(age.value)
    
    # Mostrar en consola las parejas de Omega_m y edad del universo
    print(f"Omega_m: {Om0:.1f}, Edad del universo: {age.value:.2f} Gyr")

# Graficar Omega_m vs Edad del Universo
plt.figure(figsize=(10, 6))
plt.plot(Omega_m_values, ages, marker='o', color='b', linestyle='-')
plt.xlabel("Omega_m")
plt.ylabel("Edad del Universo (Gyr)")
plt.title("Edad del Universo vs Omega_m (con H0 fijo en 67 km/s/Mpc y Omega_lambda variable)")
plt.grid(True)
plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5])
plt.show()
