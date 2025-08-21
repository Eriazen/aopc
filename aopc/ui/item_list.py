from nicegui import ui


def init_item_list():
    with ui.list().props('w-full'):
        with ui.expansion(text='Weapons').props('expand-separator').classes('w-full'):
            ui.button(text='t4 bag')
        with ui.expansion(text='Armour').props('expand-separator'):
            ui.button(text='yippe')