from nicegui import ui
from aopc.io import JSONGetter
from aopc.ui import market, crafting, transport, item_list, settings

def main():
    x = JSONGetter("https://europe.albion-online-data.com", "/api/v2/stats/prices/", "T4_BAG", "1").get_dict()

    settings.setup_ui()

    with ui.header(elevated=True).classes('items-center justify-between flat bordered'):
        ui.label('aopc').props('width=150')
        ui.input(placeholder='Searchbar...').props('rounded outlined dense')
        server_select = ui.select({1: 'Europe',2: 'West',3: 'Asia'}, value=1)

    with ui.left_drawer().props('width=150').classes('px-0 py-0'):
        with ui.tabs().props('vertical').classes('w-full') as tabs:
            market_tab = ui.tab('Market', icon='store')
            crafting_tab = ui.tab('Craft', icon='handyman')
            transport_tab = ui.tab('Trans', icon='transfer_within_a_station')

    with ui.right_drawer().props('width=250').classes('px-0 py-0'):
        item_list.init_item_list()

    with ui.footer():
        ui.label('yippee')

    with ui.tab_panels(tabs, value=market_tab).props('vertical').classes('w-full h-full'):
            with ui.tab_panel(market_tab):
                market.init_market()
            with ui.tab_panel(crafting_tab):
                crafting.init_crafting()
            with ui.tab_panel(transport_tab):
                transport.init_transport()
    ui.run()


if __name__ == "__main__":
    main()