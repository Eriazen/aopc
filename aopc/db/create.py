import pathlib
import sqlite3
import csv
from platformdirs import user_data_path


class Database:
    def __init__(self):
        self.path = pathlib.Path(user_data_path('aopc', False))
        self.path.mkdir(parents=True, exist_ok=True)
        self.db_path = self.path / 'items.db'

        self.connect()

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.cur.close()
        self.conn.close()

    def purge(self):
        self.db_path.unlink(missing_ok=True)

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Item (
                                item_id TEXT PRIMARY KEY,
                                item_name TEXT NOT NULL
                            );''')
        self.conn.commit()

    def insert(self):
        with open('aopc/db/ao_items.dat', 'r') as f:
            dr = csv.DictReader(f)
            to_db = [(i['item_id'], i['name']) for i in dr]

        self.cur.executemany('''INSERT INTO Item (item_id, item_name) VALUES (?, ?);''', to_db)
        self.conn.commit()