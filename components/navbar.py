from nicegui import ui

def show_navbar():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    with ui.element('div').classes('w-full flex flex-row justify-between items-center px-20 py-10 fixed top-0 left-0 z-50'):
        with ui.row():
            ui.link('Home', '/')
            
        with ui.row():
            ui.link('Issue Detail', '/issue_detail')
            ui.link('Issue Confirmation', '/issue_confirmation')
            ui.link('Signup', '/signup')
            ui.link('Signin', '/signin')