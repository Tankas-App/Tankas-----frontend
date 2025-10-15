from nicegui import ui
from components.sidebar import show_sidebar

@ui.page('/dashboard')
def show_dashboard():
    ui.query(".nicegui-row").classes("flex-nowrap")

    with ui.element("main").classes("w-full flex flex-row justify-between items-center"):
        with ui.row().classes('w-[20%] h-screen'):
            show_sidebar()
        with ui.column().classes('flex-1 p-8 w-[80%]'):
            ui.label('Main Content Area').classes('text-3xl font-bold mb-4')
            ui.label('This is a test page showing the sidebar in action.').classes('text-gray-600')
