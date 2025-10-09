from nicegui import ui
from components.navbar import show_navbar

@ui.page('/signin')
def show_signin_page():
    show_navbar()

    with ui.element('div').classes('w-full h-screen flex flex-col justify-center items-center py-20'):
        ui.label("Welcome Back!")
        ui.label("Log in to continue your journey with Tankas.")
        with ui.card().classes('w-[30%] flex flex-col items-center shadow-lg'):
            ui.label("Email or Username")
            ui.input(placeholder='you@example.com').classes('w-full').props('outlined')
            ui.label("Password")
            ui.input(placeholder='********', password=True, password_toggle_button=True).classes('w-full').props('outlined')
            ui.label("Forgot Password?")
            ui.button("Login").props('flat dense no-caps').classes('w-full')
        with ui.row():
            ui.label("Don't have an account?")
            ui.link("Sign Up", '/signup')