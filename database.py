import sqlite3

def create_table():
    conn = sqlite3.connect('locations.db')
    cursor = conn.cursor()

    # Crear una tabla llamada 'locations'
    cursor.execute('''CREATE TABLE IF NOT EXISTS locations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ip_address TEXT,
                        latitude REAL,
                        longitude REAL
                    )''')

    conn.commit()
    conn.close()