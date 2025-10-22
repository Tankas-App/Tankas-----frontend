from nicegui import ui


def show_issue_card(issue):
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    with ui.card().on(type="click", handler=lambda: ui.navigate.to(f"/issue_detail?id={issue["id"]}")).classes('flex flex-col justify-center items-center w-full cursor-pointer').style('font-family: "Raleway", serif;'):
        with ui.element('div').classes('w-full flex flex-row justify-between items-center text-xs mb-4'):
            ui.image(issue["picture_url"]).classes('w-full h-32 object-cover rounded-lg mb-4')

            with ui.column().classes('w-[70%]'):
                ui.label(text=issue["title"]).classes('font-bold text-sm')
                ui.label(text=issue["description"]).classes('text-xs text-gray-600')
                ui.label(text=f"Location: ({issue['latitude']:.4f}, {issue['longitude']:.4f})").classes('text-xs text-gray-600 mt-2')
                # with ui.row().classes('flex flex-row items-center gap-1'):
                #     ui.icon('star').style('color: #2E86AB')
                #     ui.label(text=issue["points_assigned"]).style('color: #2E86AB').classes('font-bold')
                #     ui.label("Points")
            with ui.column().classes('w-[30%] flex flex-col justify-between items-center'):
                if issue['difficulty'] == 'Easy':
                    ui.label(text=issue["difficulty"]).classes('text-sm text-green-600 font-semibold')
                elif issue['difficulty'] == 'Medium':
                    ui.label(text=issue["difficulty"]).classes('text-sm text-yellow-600 font-semibold')
                else:
                    ui.label(text=issue["difficulty"]).classes('text-sm text-red-600 font-semibold')
                
                with ui.row().classes('flex flex-row items-center gap-1'):
                    ui.icon('star').style('color: #f8d50eff')
                    ui.label(text=issue["points_assigned"]).style('color: #f8d50eff').classes('font-bold')
                    ui.label("Points")
        ui.button('Volunteer').props('flat dense no-caps').classes('w-full text-white py-2').style('background-color: #007F7C;')
        