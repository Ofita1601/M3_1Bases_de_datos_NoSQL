import requests

# URL de la API y ID del registro a eliminar
url = "https://66b4e5429f9169621ea4c32c.mockapi.io/api/v1/contactos"
registro_id = "1"  # Cambia este valor por el ID del registro que deseas eliminar

# Realizar la solicitud DELETE para eliminar el registro
response = requests.delete(f"{url}/{registro_id}")

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    print("Registro eliminado con éxito.")
else:
    print(f"Error al eliminar el registro. Código de estado: {response.status_code}")
    print(f"Mensaje de error: {response.text}")