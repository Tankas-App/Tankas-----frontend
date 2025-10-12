from nicegui import ui

@ui.page('/issues')
def show_issues():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    with ui.element('main').classes('w-full h-full px-10 py-20 flex justify-center items-center').style('font-family: "Raleway", serif; background-color:#F7FFF7;'):
        ui.label("Issue Feed")
        ui.label("Search, filter, and find issues to resolve in your community.")
        with ui.element('div').classes('w-[80%] px-10 bg-white'):
            ui.input(placeholder='Search by keyboard, location, or reporter...').props('outlined')
            with ui.element('div').classes('w-full flex justify-between items-center'):
                ui.select(options=["All", "High", "Medium", "Low"], label="Priority", value="All").props('outlined').classes('w-1/2')
                ui.select(options=["All", "High", "Medium", "Easy"], label="Difficulty", value="All").props('outlined').classes('w-1/2')