from nicegui import ui

def show_navbar():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    with ui.element('div').classes('w-full flex flex-row justify-between items-center px-20 py-5 fixed top-0 left-0 z-50 bg-white text-sm shadow-md').style('font-family: "Raleway", serif; color: #2E86AB'):
        with ui.row():
            ui.link('Home', '/').classes('no-underline font-semibold ')
            
        with ui.row():
            ui.link('Issue Detail', '/issue_detail').classes('no-underline font-semibold ')
            ui.link('Issue Confirmation', '/issue_confirmation').classes('no-underline font-semibold ')
            ui.link('Suggest Reward', '/suggest_reward').classes('no-underline font-semibold ')
            ui.link('Post Issue', '/post_issue').classes('no-underline font-semibold ')

        with ui.row().classes('gap-0'):
            ui.button(text="Join Now", on_click=lambda: ui.navigate.to('/signup')).props('flat dense no-caps').classes('text-white px-5 py-1 shadow-sm shadow-gray-200 font-semibold').style('background-color: #007F7C')
            ui.button(text="Login", on_click=lambda: ui.navigate.to('/signin')).props('flat dense no-caps').classes('text-white px-5 py-1 shadow-sm shadow-gray-200 font-semibold').style('background-color: #ade6e5ff')