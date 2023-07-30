from flask import Flask, request, render_template, jsonify
import sqlite3
from locator import getData
from database import create_table, reset_table

app = Flask(__name__, static_url_path='/static')

try:
    create_table()
except sqlite3.Error as sqlite_error:
    # Manejar errores relacionados con la base de datos SQLite
    print(f"Error de base de datos SQLite al crear la tabla: {sqlite_error}")

@app.route('/')
def index():
    try:
        client_ip = request.cookies.get('client_ip')
        # Resto del código para obtener la ubicación
        data = getData(client_ip)
        # Almacenar la ubicación en la base de datos
        conn = sqlite3.connect('locations.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM locations')
        locations = cursor.fetchall()
        cursor.execute('''INSERT INTO locations (ip_address, latitude, longitude) 
                          VALUES (?, ?, ?)''', (data['client_ip'], data['latitude'], data['longitude']))
        conn.commit()
        conn.close()

        # Renderizar la plantilla HTML y pasar los datos de ubicación y las localizaciones al template
        return render_template('index.html', latitude=data['latitude'], longitude=data['longitude'], locations=locations, client_ip=client_ip)
    
    except sqlite3.Error as sqlite_error:
        # Manejar errores relacionados con la base de datos SQLite
        print(f"Error de base de datos SQLite en la función index: {sqlite_error}")
    
    except Exception as e:
        # Manejar otras excepciones no previstas
        print(f"Error inesperado en la función index: {e}")

@app.route('/reset')
def reset():
    try:
        reset_table()  # Llama a la función para resetear la tabla
        return 'La tabla ha sido reseteada. Todos los registros han sido borrados.'
    
    except sqlite3.Error as sqlite_error:
        # Manejar errores relacionados con la base de datos SQLite
        print(f"Error de base de datos SQLite en la función reset: {sqlite_error}")
        return 'Error al resetear la tabla.'

    except Exception as e:
        # Manejar otras excepciones no previstas
        print(f"Error inesperado en la función reset: {e}")
        return 'Error inesperado al resetear la tabla.'

if __name__ == '__main__':
    app.run()
