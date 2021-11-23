import pgdb
from lib.config import Config

#Databa
class Database:

    def __init__(self):
        self.config = Config().getConfig()

    def connect(self):
        conn =  pgdb.Connection( host=self.config['postgres']['host'], port=self.config['postgres']['port'] ,user=self.config['postgres']['user'], password=self.config['postgres']['password'], database=self.config['postgres']['db'])

        return conn

    def query(self, sql, conn):
        cursor = conn.cursor()
        cursor.execute(sql)

        return cursor

    def close_connect(self, conn):
        conn.close()


