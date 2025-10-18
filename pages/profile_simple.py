from nicegui import ui

@ui.page('/profile_simple')
def show_simple_profile():
    ui.label('Simple Profile Page').classes('text-3xl font-bold')
    ui.label('This is a working profile page').classes('text-lg')
    ui.button('Back', on_click=lambda: ui.navigate.to('/user_profile'))