
import requests

import requests

def getData(client_ip):
    try:
        # Asegurarse de obtener la dirección IP pública en caso de que haya múltiples direcciones en el encabezado
        if client_ip is not None:
            client_ip = client_ip.split(',')[0].strip()
        else:
            client_ip = '0.0.0.0'
        
        response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=1d47c06ff0d1471b9cb48d41e095c64d&ip_address="+client_ip)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        response.raise_for_status()
        
        data = response.json()
        location = {
            'client_ip': client_ip,
            'latitude': data['latitude'],
            'longitude': data['longitude']
        }
        return location
    
    except requests.exceptions.RequestException as req_exc:
        # Manejar errores de solicitud, como problemas de red, URL incorrecta, etc.
        print(f"Error de solicitud: {req_exc}")
        return None
    
    except ValueError as value_error:
        # Manejar errores al analizar la respuesta JSON
        print(f"Error al analizar JSON: {value_error}")
        return None
    
    except KeyError as key_error:
        # Manejar errores si falta una clave en el JSON
        print(f"Error de clave en JSON: {key_error}")
        return None
