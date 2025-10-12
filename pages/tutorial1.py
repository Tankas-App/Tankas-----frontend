from nicegui import ui


@ui.page("/tutorial1")
def show_tutorial1():
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    with ui.element("main").classes("w-full h-screen flex justify-center items-center").style('font-family: "Raleway", serif;'):
        with ui.card().classes('w-[40%] h-[80%] flex items-center'):
            ui.image(
                "/assets/cleaner1.png"
            ).classes('w-1/2')
            with ui.element('div').classes('flex flex-col justify-center items-center'):
                ui.label("Welcome to Tankas").classes('text-3xl p-4 font-semibold')
                ui.label("Join a community dedicated to improving sanitation in your neighborhood. Report issues, volunteer for fixes, and earn rewards!").classes('text-gray-500 w-[80%]')
            with ui.element('div').classes('w-full flex flex-row justify-around items-center'):
                ui.button('Skip', on_click=lambda: ui.navigate.to('/signup')).props('flat dense no-caps').classes('bg-green-200 px-5 font-semibold text-black rounded-2xl')
                ui.button('Next', on_click=lambda: ui.navigate.to('/tutorial2')).props('flat dense no-caps').classes('bg-green-500 px-5 font-semibold text-black rounded-2xl')
