from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page('/')
def homepage():
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')
    
    show_navbar()

    with ui.element('main').classes('w-full h-screen flex flex-col justify-center items-center bg-[url("/assets/hero.jpg")] bg-cover bg-center').classes('').style('font-family: "Raleway", serif;'):
        with ui.element('div').classes('text-white bg-black/30 w-full h-full flex flex-col justify-center items-center'):
            ui.label("Clean Together, Thrive Together").style('font-family: "Archivo Black", sans-serif;').classes('text-6xl mb-8')
            ui.label("Join Tankas, the gamified sanitation app that turns community improvement into a fun, rewarding adventure. Earn points, badges, and recognition for making your neighborhood cleaner and greener.").classes('w-[40%] text-lg text-gray-300 mb-8')
            ui.button(text="Get Started", on_click=lambda: ui.navigate.to('/tutorial1')).props('flat dense no-caps').classes('bg-green-500 text-white px-10 py-2 rounded-lg shadow-sm shadow-gray-200 font-semibold')

    show_footer()