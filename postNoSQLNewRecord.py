import requests
import json

# URL de la API y ID del registro a consultar
url = "https://66b4e5429f9169621ea4c32c.mockapi.io/api/v1/contactos"
registro_id = "1"  # Cambia este valor por el ID del registro que deseas consultar

# Realizar la solicitud GET para el registro específico
response = requests.get(f"{url}/{registro_id}")

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()

    # Mostrar los datos en formato plano
    print("Datos del registro en formato plano:")
    for key, value in data.items():
        print(f"{key}: {value}")
else:
    print(f"Error al hacer la solicitud a la API. Código de estado: {response.status_code}")
