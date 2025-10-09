from nicegui import ui
from components.navbar import show_navbar
import requests
from utils.api import base_url

# def _signin_user(data):
#     response = requests.post(f"{base_url}/users/login", data=data)
#     print(response.status_code, response.content)
#     if response.status_code == 200:
#         json_data = response.json()
#         app.storage.user["access_token"] = json_data["access_token"]
#         return ui.navigate.back()

@ui.page('/signin')
def show_signin_page():
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )

    show_navbar()

    with ui.element('div').classes('w-full h-screen flex flex-col justify-center items-center py-20'):
        ui.label("Welcome Back!")
        ui.label("Log in to continue your journey with Tankas.")
        with ui.card().classes('w-[30%] flex flex-col items-center shadow-lg'):
            ui.label("Email or Username")
            email = ui.input(placeholder='you@example.com').classes('w-full').props('outlined')
            ui.label("Password")
            password = ui.input(placeholder='********', password=True, password_toggle_button=True).classes('w-full').props('outlined')
            ui.link("Forgot Password?", "#")
            ui.button("Login")
            # ui.button("Login", on_click= _signin_user(
            #     data={}
            # )).props('flat dense no-caps').classes('w-full')
        with ui.row():
            ui.label("Don't have an account?")
            ui.link("Sign Up", '/signup')