from nicegui import ui
from aopc.io import JSONGetter
from aopc.ui import market, crafting, transport, item_list, settings


def main():
    view = MarketView('https://europe.albion-online-data.com', 'T4_BAG')
    view.set_data()
    print(view.get_data())


if __name__ == "__main__":
    main()
