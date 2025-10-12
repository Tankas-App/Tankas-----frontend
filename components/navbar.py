from nicegui import ui

def show_navbar():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    with ui.element('div').classes('w-full flex flex-row justify-between items-center px-20 py-5 fixed top-0 left-0 z-50 bg-white text-sm shadow-md').style('font-family: "Raleway", serif;'):
        with ui.row():
            ui.link('Home', '/').classes('no-underline text-green-800 font-semibold ')
            
        with ui.row():
            ui.link('Issue Detail', '/issue_detail').classes('no-underline text-green-800 font-semibold ')
            ui.link('Issue Confirmation', '/issue_confirmation').classes('no-underline text-green-800 font-semibold ')

        ui.button(text="Join Now", on_click=lambda: ui.navigate.to('/signup')).props('flat dense no-caps').classes('bg-green text-black px-5 py-1 rounded-lg shadow-sm shadow-gray-200 font-semibold')