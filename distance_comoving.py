from astropy.cosmology import Planck18 as cosmo

# Redshift del objeto
z = 0.1316  # Ejemplo de redshift

# Calcular la distancia comóvil en Mpc
distancia_comovil = cosmo.comoving_distance(z).value

print(f"La distancia comóvil es {distancia_comovil:.2f} Mpc")
