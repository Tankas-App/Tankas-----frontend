from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page('/')
def homepage():
    show_navbar()

    with ui.element('main').classes('w-full h-screen flex flex-col justify-center items-center'):
        ui.label("hello")

    show_footer()