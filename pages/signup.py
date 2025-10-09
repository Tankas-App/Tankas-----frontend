from nicegui import ui
from components.navbar import show_navbar

@ui.page('/signup')
def show_signup_page():
    show_navbar()

    with ui.element('div').classes('w-full h-full flex flex-col justify-center items-center py-20'):
        ui.label("Create your account")
        ui.label("Join our community for a cleaner tomorrow.")
        with ui.card().classes('w-[30%] flex flex-col items-center shadow-lg'):
            ui.label("Full Name")
            ui.input(placeholder='Enter your full name').classes('w-full').props('outlined')
            ui.label("Email")
            ui.input(placeholder='Enter your email').classes('w-full').props('outlined')
            ui.label("Password")
            ui.input(placeholder='Enter your password', password=True, password_toggle_button=True).classes('w-full').props('outlined')
            ui.label("Confirm Password")
            ui.input(placeholder='Confirm your password', password=True, password_toggle_button=True).classes('w-full').props('outlined')
            ui.button("Sign Up").props('flat dense no-caps').classes('w-full')
        with ui.row():
            ui.label("Already have an account?")
            ui.link("Sign in", '/signin')