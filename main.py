from nicegui import ui
from aopc.io import JSONGetter
from aopc.core import MarketView
from aopc.db import create


def main():
    new_db = create.Database()
    new_db.create_table()
    new_db.insert()
    new_db.disconnect()
    new_db.purge()


if __name__ in {"__main__", "__mp_main__"}:
    main()