from nicegui import ui

def show_navbar():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    ui.label("Navbar contents here...")