from nicegui import ui, app, run
from components.navbar import show_navbar
import requests
from utils.api import base_url

_signin_btn: ui.button = None

def _run_signin(data):
    return requests.post(f"{base_url}/api/auth/login", data=data)

async def _signin_user(data):
    _signin_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_signin, data)
    print(response.status_code, response.content)
    _signin_btn.props(remove="disable loading")
    if response.status_code == 200:
        json_data = response.json()
        app.storage.user["access_token"] = json_data["access_token"]
        return ui.navigate.back()

@ui.page('/signin')
def show_signin_page():
    global _signin_btn
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )

    show_navbar()

    with ui.element('div').classes('w-full h-screen flex flex-col justify-center items-center py-20'):
        ui.label("Welcome Back!")
        ui.label("Log in to continue your journey with Tankas.")
        with ui.card().classes('w-[30%] flex flex-col items-center shadow-lg'):
            ui.label("Username")
            username = ui.input(placeholder='Enter your username').classes('w-full').props('outlined')
            ui.label("Password")
            password = ui.input(placeholder='********', password=True, password_toggle_button=True).classes('w-full').props('outlined')
            ui.link("Forgot Password?", "#")
            # ui.button("Login")
            _signin_btn = ui.button("Login", on_click=lambda: _signin_user(
                data={"username": username.value,
                      "password": password.value}
            )).props('flat dense no-caps').classes('w-full')
        with ui.row():
            ui.label("Don't have an account?")
            ui.link("Sign Up", '/signup')