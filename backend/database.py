import psycopg2
from dotenv import load_dotenv
from psycopg2 import pool
import os
import dotenv

load_dotenv()

class Database:
    #Costruttore
    def __init__(self):
        self.connection_pool = None     #Pool di connessioni
        self.create_connection_pool()   #Metodo per la creazione della connection pool

    #Metodo per la creazione del pool di connessioni
    def create_connection_pool(self):
        try:
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(
                1,
                3,
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("POSTGRES_HOST"),
                port=os.getenv("POSTGRES_PORT"),
                database=os.getenv("POSTGRES_DB")
            )
        except Exception as e:
            print("Errore: connessione non riuscita ", e)

    def get_connection(self):
        return self.connection_pool.getconn()

    def release_connection(self, connessione):
        self.connection_pool.putconn(connessione)

    def closeall_connection(self):
        if self.connection_pool:
            self.connection_pool.closeall()


db = Database() #singola istanza del database