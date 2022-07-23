import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


class Db:

    def __init__(self):
        self.connection = psycopg.connect(os.getenv('DB_DSN'))

    def get_connection(self):
        return self.connection


class StoreException(Exception):
    def __init__(self, message, *errors):
        Exception.__init__(self, message)
        self.errors = errors
