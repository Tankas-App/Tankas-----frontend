from nicegui import ui
@ui.page('/user_profile')
def show_user_profile():
    """Reusable profile widget for dashboard and other pages"""
    with ui.card().classes('w-full p-6 bg-teal-100'):
        with ui.row().classes('items-center gap-4'):
            # Profile avatar
            ui.avatar().classes('w-16 h-16').style('background: url("/assets/user1.png") center/cover')
            
            # User info
            with ui.column().classes('w-full flex-1'):
                ui.label('Sophia Clark').classes('text-xl font-bold')
                ui.label('Level 5 • 750/1000 XP').classes('text-sm').style('color: #007F7C')
                
                # Mini progress bar
                ui.linear_progress(value=0.75).classes('h-3 w-full mt-1').style('background-color: #007F7C')
            
            # Quick stats
            
        # Quick actions
        with ui.row().classes('gap-2 mt-4'):
            ui.button('View Profile', on_click=lambda: ui.navigate.to('/profile')).props("flat dense no-caps").classes('flex-1 py-2 text-white rounded-lg').style('background-color: #007F7C')
            ui.button('Edit', on_click=lambda: ui.notify('Edit clicked')).props("flat dense no-caps").classes('px-4 py-2 border rounded-lg').style('background-color: #007F7C')
def show_profile_summary():
    """Compact profile summary for sidebar"""
    with ui.row().classes('items-center gap-3 p-3 rounded-lg cursor-pointer hover:bg-gray-100').on('click', lambda: ui.navigate.to('/profile')):
        ui.avatar('SC').classes('w-10 h-10').style('background-color: #007F7C')
        with ui.column().classes('flex-1'):
            ui.label('Sophia Clark').classes('font-medium text-sm')
            ui.label('Level 5').classes('text-xs text-gray-500')