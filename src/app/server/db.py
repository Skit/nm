import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()


class Db:

    def __init__(self):
        self.connection = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_connection(self):
        return self.connection


class StoreException(Exception):
    def __init__(self, message, *errors):
        def __init__(self, message, *errors):
            Exception.__init__(self, message)
            self.errors = errors
