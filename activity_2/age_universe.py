from astropy.cosmology import LambdaCDM
from astropy import units as u

# Define los valores iniciales de las constantes cosmológicas
H0 = 50 * u.km / u.s / u.Mpc  # Constante de Hubble
Om0 = 1                     # Densidad de materia
Ode0 = 0                    # Densidad de energía oscura
Ok0 = 0                       # Curvatura (0 para un universo plano)

# Crear el modelo cosmológico Lambda-CDM con los valores iniciales
cosmo = LambdaCDM(H0=H0, Om0=Om0, Ode0=Ode0)

# Calcular la edad del universo para este conjunto de parámetros
edad_universo = cosmo.age(0)  # Redshift 0 significa el presente

print(f"Edad del universo con H0={H0}, Om0={Om0}, Ode0={Ode0}, Ok0={Ok0}: {edad_universo:.2f}")

# Para probar otras configuraciones de constantes cosmológicas
# Ejemplo: Cambiar H0 a 67 km/s/Mpc, Om0 a 0.4, Ode0 a 0.6
H0_nuevo = 67 * u.km / u.s / u.Mpc
Om0_nuevo = 0.309
Ode0_nuevo = 0.691

# Crear el modelo cosmológico ajustado
cosmo_nuevo = LambdaCDM(H0=H0_nuevo, Om0=Om0_nuevo, Ode0=Ode0_nuevo)

# Calcular la nueva edad del universo
edad_universo_nueva = cosmo_nuevo.age(0)

print(f"Edad del universo con H0={H0_nuevo}, Om0={Om0_nuevo}, Ode0={Ode0_nuevo}, Ok0={Ok0}: {edad_universo_nueva:.2f}")
