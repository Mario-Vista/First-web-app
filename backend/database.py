import psycopg2
from dotenv import load_dotenv
from psycopg2 import pool
import os
import dotenv

# Load environment variables from a .env file
load_dotenv()


class Database:
    """
    Database class that manages a PostgreSQL connection pool.

    This class handles:
    - Creating a connection pool
    - Providing connections to the application
    - Releasing connections back to the pool
    - Closing all connections
    """

    def __init__(self):
        """
        Constructor: Initializes the connection pool.
        """
        self.connection_pool = None  # Store the connection pool
        self.create_connection_pool()  # Initialize the pool

    def create_connection_pool(self):
        """
        Creates a connection pool for PostgreSQL using environment variables.

        The pool allows a minimum of 1 and a maximum of 10 concurrent connections.
        """
        try:
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(
                1,  # Minimum number of connections
                10, # Maximum number of connections
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("POSTGRES_HOST"),
                port=os.getenv("POSTGRES_PORT"),
                database=os.getenv("POSTGRES_DB")
            )
        except Exception as e:
            self.connection_pool = None
            print("Error: failed to create connection pool", e)

    def get_connection(self):
        """
        Retrieves a connection from the pool.

        :return: psycopg2 connection object
        :raises Exception: if the connection pool is not initialized
        """
        if not self.connection_pool:
            raise Exception("Connection pool not initialized")
        return self.connection_pool.getconn()

    def release_connection(self, conn):
        """
        Releases a previously acquired connection back to the pool.

        :param conn: Connection object to release
        """
        if self.connection_pool and conn:
            self.connection_pool.putconn(conn)

    def closeall_connection(self):
        """
        Closes all connections in the pool.
        """
        if self.connection_pool:
            self.connection_pool.closeall()


# Create a single instance of the Database class for global use
db = Database()
