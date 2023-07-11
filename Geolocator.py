from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    ip_address = request.remote_addr  # Obtiene la dirección IP del cliente
    location = get_location(ip_address)  # Obtiene la ubicación geográfica
    print(ip_address)
    # Renderiza la plantilla HTML y pasa los datos de ubicación al template
    return render_template('index.html', latitude=location['latitude'], longitude=location['longitude'])

def get_location(ip_address):
    # Llama a la API de geolocalización de Abstract API
    api_key = '1d47c06ff0d1471b9cb48d41e095c64d'  # Reemplaza con tu clave de API de Abstract API
    url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address={ip_address}'
    response = requests.get(url)
    data = response.json()
    
    # Extrae la información de ubicación del JSON de respuesta
    location = {
        'latitude': data['latitude'],
        'longitude': data['longitude']
    }
    
    return location

if __name__ == '__main__':
    app.run()
