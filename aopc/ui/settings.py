from nicegui import ui


def setup_ui():
    ui.colors(primary='#1C1C1E',
              secondary='#2C2C2E',
              accent='#3A3A3C',
              positive='#FF6B35',
              dark='#1C1C1E',
              light='#E5E5E7')
    
    ui.dark_mode(True)