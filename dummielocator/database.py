import sqlite3

def create_table():
    try:
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
        
    except sqlite3.Error as sqlite_error:
        # Manejar errores relacionados con la base de datos SQLite
        print(f"Error de base de datos SQLite: {sqlite_error}")

def reset_table():
    try:
        conn = sqlite3.connect('locations.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM locations')  # Elimina todos los registros de la tabla
        conn.commit()
        conn.close()
        
    except sqlite3.Error as sqlite_error:
        # Manejar errores relacionados con la base de datos SQLite
        print(f"Error de base de datos SQLite: {sqlite_error}")
