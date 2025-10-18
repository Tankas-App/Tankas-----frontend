from nicegui import ui
from components.sidebar import show_sidebar
from components.user_profile import show_user_profile

@ui.page('/dashboard')
def show_dashboard():
    
    ui.query(".nicegui-row").classes("flex-nowrap")

    with ui.element("main").classes("w-full flex flex-row justify-between items-center"):
        with ui.row().classes('w-[20%] h-screen'):
            show_sidebar()
        # Main content area (right)
        with ui.column().classes(
            "flex-1 flex flex-col h-full overflow-y-auto p-8"
        ):
            # Top: user profile section
            with ui.row().classes(
                "w-full justify-between items-center mb-6 pb-4 border-b border-gray-200"
            ):
                show_user_profile()

            # Main content
            with ui.column().classes("w-full flex-1 mt-4 z-50 m-0 p-0 gap-0"):
                ui.label('Dashboard').classes('text-4xl font-bold mb-2 text-blue-600')
                ui.label('Welcome to your dashboard area.').classes('text-gray-600 mb-8')

                # Example content section
                with ui.row().classes(' w-full gap-4'):
                    with ui.card().classes(" w-2/3 shadow-lg p-6 rounded-2xl bg-teal-100"):
                        with ui.row().classes('items-center'):
                            ui.label('1200').classes('text-lg font-bold').style('color: #007F7C')
                            ui.label('Points').classes('text-xs text-gray-500')
                    with ui.card().classes(" w-2/3 shadow-lg p-6 rounded-2xl bg-teal-100"):
                        with ui.row().classes('items-center'):
                            ui.label('35').classes('text-lg font-bold').style('color: #007F7C')
                            ui.label('Tasks').classes('text-xs text-gray-500')
                    with ui.card().classes("w-2/3 shadow-lg p-6 rounded-2xl bg-teal-100"):
                        with ui.row().classes('items-center'):
                            ui.label('15').classes('text-lg font-bold').style('color: #007F7C')
                            ui.label('Badges').classes('text-xs text-gray-500')
                
