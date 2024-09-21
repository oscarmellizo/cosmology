import pandas as pd
from astropy.cosmology import Planck18 as cosmo
import requests
from io import StringIO

# Cargar los datos de los cúmulos
cumulos = pd.read_csv('cumulos_asegurados.csv')

# Nombre del archivo de salida
archivo_salida = 'resultados.csv'

# Escribir el encabezado en el archivo de salida (si es la primera vez que se corre)
with open(archivo_salida, 'w') as f:
    f.write('ID,RA,DEC,REDSHIFT,PROMEDIO_R\n')

# Iterar sobre cada cúmulo
for index, row in cumulos.iterrows():
    ra = row['RA']
    dec = row['DEC']
    redshift = row['REDSHIFT']

    # Calcular la distancia comóvil en Mpc
    comovil_distance = cosmo.comoving_distance(redshift).value

    # Calcular el radio en arcominutos
    radius = (1 / comovil_distance) * 3437.75

    # Crear la consulta SQL
    query = f"""
    SELECT p.ra, p.dec, p.r, p.u, p.g, p.i, p.z, s.class, s.z as redshift
    FROM PhotoObj AS p
    JOIN dbo.fgetNearByObjEq({ra}, {dec}, {radius}) n ON n.objID = p.objID
    LEFT OUTER JOIN SpecObj AS s ON s.bestobjid = p.objid
    WHERE s.z BETWEEN {redshift} - 0.015 AND {redshift} + 0.015 AND s.class = 'GALAXY'
    """

    # Ejecutar la consulta en SkyServer
    url = 'https://skyserver.sdss.org/dr17/SkyServerWS/SearchTools/SqlSearch'
    params = {'cmd': query, 'format': 'csv'}
    response = requests.get(url, params=params)

    number_galaxies_expected = 10

    # Guardar el resultado
    if response.status_code == 200:
        csv_content = response.content.decode('utf-8').strip()
        if csv_content:
            lines = csv_content.splitlines()
            if len(lines) > number_galaxies_expected:
                print(f"Se encontraron {len(lines) - 1} galaxias en el cúmulo {row['ID']}.")
                csv_data = StringIO(csv_content)
                
                # Procesar csv_data
                df = pd.read_csv(csv_data, header=1)
                
                # Limpiar nombres de las columnas
                df.columns = df.columns.str.strip()
                
                # Calcular el promedio de la columna 'r'
                if 'r' in df.columns:
                    promedio_r = df['r'].mean()

                    # Escribir el resultado en el archivo de salida
                    with open(archivo_salida, 'a') as f:
                        f.write(f"{row['ID']},{row['RA']},{row['DEC']},{row['REDSHIFT']},{promedio_r}\n")
                else:
                    print(f"La columna 'r' no se encuentra en los datos procesados para el cúmulo {row['ID']}.")
            else:
                print(f"No se encontraron suficientes resultados para el cúmulo {row['ID']}.")
        else:
            print("La consulta devolvió una respuesta vacía para el cúmulo {row['ID']}.")
    else:
        print(f"Error en el cúmulo {row['ID']}: {response.status_code}")
