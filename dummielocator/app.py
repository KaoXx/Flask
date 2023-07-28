from flask import Flask, request, render_template
import sqlite3
from locator import getData
from database import create_table,reset_table

app = Flask(__name__,static_url_path='/static')

create_table()

@app.route('/')
def index():

    
    # Resto del código para obtener la ubicación
    data = getData()
    
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
    return render_template('index.html', latitude=data['latitude'], longitude=data['longitude'], locations=locations)

@app.route('/reset')
def reset():
    reset_table()  # Llama a la función para resetear la tabla
    return 'La tabla ha sido reseteada. Todos los registros han sido borrados.'

if __name__ == '__main__':
    app.run()
