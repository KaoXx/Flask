
import requests
from flask import request

def getData():
    client_ip = request.headers.get('X-Forwarded-For')
    # Asegurarse de obtener la dirección IP pública en caso de que haya múltiples direcciones en el encabezado
    if client_ip is not None:
        client_ip = client_ip.split(',')[0].strip()
    else:
        client_ip = '166.171.248.255'
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=1d47c06ff0d1471b9cb48d41e095c64d&ip_address="+client_ip)
    data = response.json()
    location = {
        'client_ip': client_ip,
        'latitude': data['latitude'],
        'longitude': data['longitude']
    }
    return location