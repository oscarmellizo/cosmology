import requests

# URL del endpoint de la API para consultas SQL
url = "https://skyserver.sdss.org/dr17/SkyServerWS/SearchTools/SqlSearch"

# Consulta SQL (obtener los primeros 1000 objetos de la tabla PhotoObj)
sql_query = """
SELECT TOP 1000
p.ra,p.dec,p.r,p.u,p.g,p.i,p.z,
s.class, s.z as redshift
FROM PhotoObj AS p
JOIN dbo.fgetNearByObjEq(120.01667, 44.93694, 25) n ON
n.objID=p.objID
LEFT OUTER JOIN SpecObj AS s ON s.bestobjid = p.objid
WHERE
s.z BETWEEN 0.2851 - 0.015 AND 0.2851 + 0.015 and s.class = 'GALAXY'
"""

# Parámetros de la solicitud HTTP
params = {
    "cmd": sql_query,  # La consulta SQL como parámetro cmd
    "format": "json"   # Puedes elegir otros formatos como csv o xml
}

# Hacer la solicitud HTTP GET con la consulta SQL
response = requests.get(url, params=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Imprimir la respuesta JSON
    data = response.json()
    print(data)
else:
    print(f"Error en la consulta: {response.status_code}")
