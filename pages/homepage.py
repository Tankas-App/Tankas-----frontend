from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page('/')
def homepage():
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )
    
    show_navbar()

    with ui.element('main').classes('w-full h-screen flex flex-col justify-center items-center'):
        ui.label("hello")

    show_footer()