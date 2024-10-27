import matplotlib.pyplot as plt
from astropy.cosmology import LambdaCDM
from astropy import units as u

H0_values = [40, 45, 50, 55, 60, 65, 67, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300]
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

plt.xlim(30, 310)
plt.xticks([40, 45, 50, 55, 60, 65, 67, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300])

plt.show()
