
import requests
from flask import request

def getData():
    ip_address = request.headers.get('X-Forwarded-For')
    # Asegurarse de obtener la dirección IP pública en caso de que haya múltiples direcciones en el encabezado
    if ip_address is not None:
        ip_address = ip_address.split(',')[0].strip()
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=1d47c06ff0d1471b9cb48d41e095c64d&ip_address={ip_adresss}")
    data = response.json()
    location = {
        'ip_address': data['ip_address'],
        'latitude': data['latitude'],
        'longitude': data['longitude']
    }
    return location