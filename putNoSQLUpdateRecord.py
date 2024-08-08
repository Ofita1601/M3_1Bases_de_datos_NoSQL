import requests
import json

# URL de la API y ID del registro a modificar
url = "https://66b4e5429f9169621ea4c32c.mockapi.io/api/v1/contactos"
registro_id = "1"  # Cambia este valor por el ID del registro que deseas modificar

# Datos que deseas actualizar en el registro
datos_actualizados = {
    "nombre": "Nuevo Nombre",
    "email": "nuevoemail@example.com",
    "telefono": "1234567890"
    # Agrega otros campos según sea necesario
}

# Realizar la solicitud PUT para actualizar el registro
response = requests.put(f"{url}/{registro_id}", json=datos_actualizados)

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Obtener la respuesta en formato JSON
    data = response.json()

    # Mostrar los datos actualizados en formato plano
    print("Registro actualizado con éxito:")
    for key, value in data.items():
        print(f"{key}: {value}")
else:
    print(f"Error al hacer la solicitud a la API. Código de estado: {response.status_code}")
    print(f"Mensaje de error: {response.text}")
