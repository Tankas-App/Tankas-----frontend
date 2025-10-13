from nicegui import ui

@ui.page('/tutorial4')
def show_tutorial4():
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    with ui.element("main").classes("w-full h-screen flex justify-center items-center").style('font-family: "Raleway", serif; background-color:F7FFF7;'):
        with ui.card().classes('w-[40%] h-[80%] flex items-center rounded-xl'):
            ui.image(
                "/assets/user3.png"
            ).classes('w-1/2')
            with ui.element('div').classes('flex flex-col justify-center items-center'):
                ui.label("Get Rewarded for Your Impact").classes('text-3xl p-4 font-semibold')
                ui.label("Earn points for every sanitation task you complete and redeem them for exciting rewards. Your efforts make a difference!").classes('text-gray-500 w-[80%]')
            with ui.element('div').classes('w-full flex flex-row justify-around items-center'):
                ui.button('Previous', on_click=lambda: ui.navigate.back()).props('flat dense no-caps').classes('px-5 font-semibold rounded-2xl').style('background-color: #ade6e5ff; color: #007F7C;')
                ui.button('Get Started', on_click=lambda: ui.navigate.to('/signup')).props('flat dense no-caps').classes('px-5 font-semibold text-white rounded-2xl').style('background-color: #007F7C')