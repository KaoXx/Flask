
import requests
def getData():
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=1d47c06ff0d1471b9cb48d41e095c64d")
    data = response.json()
    location = {
        'ip_address': data['ip_address'],
        'latitude': data['latitude'],
        'longitude': data['longitude']
    }
    return location