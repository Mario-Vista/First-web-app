"""
File to initialize the database.
This script creates the 'users' table if it does not exist.
"""

from database import db


def init_database():
    """
    Initializes the database by creating the 'users' table.

    Table schema:
    - ID: Auto-incremented primary key
    - username: Unique username (max 50 chars)
    - password: Hashed password (max 255 chars)
    - dataCreazione: Timestamp of creation (default: current timestamp)
    """
    connection = None

    # SQL query to create the 'users' table if it doesn't exist
    query = """
    CREATE TABLE IF NOT EXISTS users (
        ID SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        dataCreazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    try:
        # Acquire a connection from the pool
        connection = db.get_connection()

        # Execute the query
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()  # Commit the transaction

        print("Database initialized successfully.")

    except Exception as e:
        # Handle any errors and rollback if needed
        print("Connection failure:", e)
        if connection:
            connection.rollback()

    finally:
        # Always release the connection back to the pool
        db.release_connection(connection)
