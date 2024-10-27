import matplotlib.pyplot as plt
from astropy.cosmology import LambdaCDM
from astropy import units as u

H0_values = [40, 45, 50, 55, 60, 65, 67, 70, 75, 80, 85, 90, 95, 100, 200, 300]
Om0 = 1  # Densidad de materia
Ode0 = 0  # Densidad de energía oscura

ages = []

for H0 in H0_values:
    cosmo = LambdaCDM(H0=H0 * u.km / u.s / u.Mpc, Om0=Om0, Ode0=Ode0)
    age = cosmo.age(0)
    ages.append(age.value)

print(ages)

plt.figure(figsize=(10, 6))
plt.plot(H0_values, ages, marker='o', color='b', linestyle='-')
plt.xlabel("H0 (km/s/Mpc)")
plt.ylabel("Edad del Universo (Gyr)")
plt.title("Edad del Universo vs Constante de Hubble (H0)")
plt.grid(True)

plt.xlim(30, 300)
plt.xticks([40, 45, 50, 55, 60, 65, 67, 70, 75, 80, 85, 90, 95, 100, 200])

plt.show()
