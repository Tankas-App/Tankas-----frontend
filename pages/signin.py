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

_login_btn: ui.button = None


def _run_login(data):
    return requests.post(f"{base_url}/api/auth/login", json=data)


async def _login_user(data):
    _login_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_login, data)
    _login_btn.props(remove="disable loading")
    print(response.status_code, response.content)
    if response.status_code == 200:
        json_data = response.json()
        app.storage.user["access_token"] = json_data["access_token"]
        return ui.navigate.to("/dashboard")


@ui.page("/signin")
def show_signin_page():
    global _login_btn
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    show_navbar()

    with ui.element("div").classes(
        "w-full h-full flex flex-col justify-center items-center py-20 mt-10"
    ).style('font-family: "Raleway", serif; background-color:#F7FFF7;'):
        ui.label("Welcome Back!").classes('text-3xl font-semibold mb-4')
        ui.label("Log in to continue your journey with Tankas.").classes('font-semibold text-lg mb-4').style('color: #2E86AB')
        with ui.card().classes("w-[30%] flex shadow-lg font-semibold mb-8"):
            ui.label("Username")
            username = (
                ui.input(placeholder="enter username")
                .classes("w-full")
                .props("outlined")
            )
            ui.label("Password")
            password = (
                ui.input(
                    placeholder="********", password=True, password_toggle_button=True
                )
                .classes("w-full")
                .props("outlined")
            )
            ui.link("Forgot Password?", "#").classes('no-underline font-semibold').style('color: #2E86AB')
            _login_btn = ui.button(
                "Login",
                on_click=lambda: _login_user(
                    {"username": username.value, "password": password.value}
                ),
            ).props("flat dense no-caps").classes("w-full text-white py-2").style('background-color: #007F7C')
            # ui.button("Login", on_click= _signin_user(
            #     data={}
            # )).props('flat dense no-caps').classes('w-full')
        with ui.row().classes('gap-0'):
            ui.label("Don't have an account?")
            ui.link("Sign Up", "/signup").classes('no-underline font-semibold').style('color: #2E86AB')
