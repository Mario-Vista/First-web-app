"""
File per inizializzare il database
"""

from database import db

def init_database():
    connection = None
    query = """CREATE TABLE IF NOT EXISTS users (ID SERIAL PRIMARY KEY , username VARCHAR(50) UNIQUE NOT NULL, password VARCHAR(255) NOT NULL, dataCreazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""

    try:
        connection = db.get_connection()
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print("Connection failure", e)
        if connection:
            connection.rollback()
    finally:
        db.release_connection(connection)


