from nicegui import ui
from aopc.io import JSONGetter
from aopc.core import MarketView


def main():
    view = MarketView('https://europe.albion-online-data.com', 'T4_BAG')
    view.set_data()
    print(view.get_data())


if __name__ in {"__main__", "__mp_main__"}:
    main()