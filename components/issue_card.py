from nicegui import ui


def show_issue_card(issue):
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    with ui.card().on(type="click", handler=lambda: ui.navigate.to(f"/issue_detail?id={issue["id"]}")).classes('flex flex-col justify-center items-center w-full cursor-pointer').style('font-family: "Raleway", serif;'):
        with ui.element('div').classes('w-full flex flex-row justify-between items-center text-xs mb-4'):
            with ui.column().classes('w-[70%]'):
                ui.label(text=issue["title"]).classes('font-bold text-sm')
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
        