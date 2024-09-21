import pandas as pd
from astropy.cosmology import Planck18 as cosmo

# Cargar los datos de los cúmulos
cumulos = pd.read_csv('cumulos.csv')  # Asume que tienes los datos en un CSV

for index, row in cumulos.iterrows():
    ra = row['RA']
    dec = row['DEC']
    redshift = row['REDSHIFT']
    
    # Calcular la distancia comóvil en Mpc
    distancia_comovil = cosmo.comoving_distance(redshift).value

    # Calcular el radio en arcominutos
    radio = (1 / distancia_comovil) * 3437.75
    
    print(f"RA: {ra}, DEC: {dec}, Radio: {radio:.2f} arcminutos, Redshift: {redshift}")