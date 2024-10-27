import matplotlib.pyplot as plt
from astropy.cosmology import LambdaCDM
from astropy import units as u

# Lista de valores de H0 a probar (en km/s/Mpc)
H0_values = [40, 50, 60, 67, 70, 80, 90, 100, 200, 300, 400, 500]
# Constantes cosmológicas para un universo plano
Om0 = 1  # Densidad de materia
Ode0 = 0  # Densidad de energía oscura

# Lista para almacenar las edades del universo
ages = []

# Calcular la edad del universo para cada valor de H0
for H0 in H0_values:
    # Crear el modelo cosmológico con el valor actual de H0
    cosmo = LambdaCDM(H0=H0 * u.km / u.s / u.Mpc, Om0=Om0, Ode0=Ode0)
    # Calcular la edad del universo en el presente (redshift = 0)
    age = cosmo.age(0)
    # Añadir la edad a la lista
    ages.append(age.value)

# Graficar Edad del Universo vs H0
plt.figure(figsize=(10, 6))
plt.plot(H0_values, ages, marker='o', color='b', linestyle='-')
plt.xlabel("H0 (km/s/Mpc)")
plt.ylabel("Edad del Universo (Gyr)")
plt.title("Edad del Universo vs Constante de Hubble (H0)")
plt.grid(True)
plt.show()
