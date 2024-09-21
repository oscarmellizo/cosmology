import pandas as pd

# Cargar los datos de los cúmulos
cumulos = pd.read_csv('cumulos.csv')  # Asume que tienes los datos en un CSV

for index, row in cumulos.iterrows():
    ra = row['RA']
    dec = row['DEC']
    redshift = row['REDSHIFT']
    
    print(f"RA: {ra}, DEC: {dec}, Redshift: {redshift}")