from nicegui import ui


def show_issue_card(issue):
    with ui.card().classes('flex flex-col justify-center items-center w-full'):
        with ui.element('div').classes('w-full flex flex-row justify-between items-center text-xs mb-4'):
            with ui.column().classes('w-[70%]'):
                ui.label("Title (Overflowing Trash Bin)").classes('font-bold text-sm')
                ui.label("Location (Labone Juntion)")
                with ui.row().classes('flex flex-row items-center gap-1'):
                    ui.icon('star').style('color: #2E86AB')
                    ui.label("50").style('color: #2E86AB').classes('font-bold')
                    ui.label("Points")
            with ui.column().classes('w-[30%] flex flex-col justify-between items-center'):
                ui.label("Difficulty")
                with ui.row().classes('flex flex-row items-center gap-1'):
                    ui.icon('star').style('color: #f8d50eff')
                    ui.label("100").style('color: #f8d50eff').classes('font-bold')
                    ui.label("Coins")
        ui.button('Volunteer').props('flat dense no-caps').classes('w-full text-white py-2').style('background-color: #007F7C;')
        