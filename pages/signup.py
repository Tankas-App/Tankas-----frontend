from nicegui import ui, run
from components.navbar import show_navbar
import requests
from utils.api import base_url

# _signup_btn: ui.button = None

# def _run_signup(data):
#     return requests.post(f"{base_url}/users/register", data=data)

# async def _signup(data):
#     _signup_btn.props(add="disable loading")
#     response = await run.cpu_bound(_run_signup, data)
#     print(response.status_code, response.content)
#     _signup_btn.props(remove="disable loading")
#     if response.status_code == 200:
#         return ui.navigate.to('/signin')
#     elif response.status_code == 409:
#         return ui.notify(message="User already exist!", type="warning")


@ui.page('/signup')
def show_signup_page():
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )

    show_navbar()

    with ui.element('div').classes('w-full h-full flex flex-col justify-center items-center py-20'):
        ui.label("Create your account")
        ui.label("Join our community for a cleaner tomorrow.")
        with ui.card().classes('w-[30%] flex flex-col items-center shadow-lg'):
            ui.label("Full Name")
            username = ui.input(placeholder='Enter your full name').classes('w-full').props('outlined')
            ui.label("Email")
            email = ui.input(placeholder='Enter your email').classes('w-full').props('outlined')
            ui.label("Password")
            password = ui.input(placeholder='Enter your password', password=True, password_toggle_button=True).classes('w-full').props('outlined')
            ui.label("Confirm Password")
            confirm_password = ui.input(placeholder='Confirm your password', password=True, password_toggle_button=True).classes('w-full').props('outlined')
            ui.checkbox(
                text="Accept our terms and conditions and privacy policy"
            ).classes("text-gray-600 text-sm")
            ui.button("Sign Up").props('flat dense no-caps').classes('w-full')
        with ui.row():
            ui.label("Already have an account?")
            ui.link("Sign in", '/signin')