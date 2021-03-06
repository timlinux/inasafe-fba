from contextlib import contextmanager
import psycopg2
import os


class DBConnection:

    def __init__(self):
        self.conn = DBConnection.conn()

    def table_exists(self, table_name, table_schema='public'):
        cur = self.conn.cursor()
        query = (
            'select '
            'exists('
            'select 1 '
            'from information_schema.tables '
            'where table_name = %s and table_schema = %s)')
        cur.execute(query, (table_name, table_schema))
        try:
            row = cur.fetchone()
            return row[0]
        except:
            return False

    @staticmethod
    def conn():
        return psycopg2.connect(
            host=os.environ.get('POSTGRES_HOST'),
            database=os.environ.get('POSTGRES_DB'),
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASS'),
            port=os.environ.get('POSTGRES_PORT')
        )
