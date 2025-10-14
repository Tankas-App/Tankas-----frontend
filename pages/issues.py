from nicegui import ui
from components.issue_card import show_issue_card
from components.navbar import show_navbar
import requests
from utils.api import base_url


@ui.page("/issues")
def show_issues():
    show_navbar()

    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    with ui.element('main').classes('w-full h-full px-10 py-20 flex flex-col justify-center items-center').style('font-family: "Raleway", serif; background-color:#F7FFF7;'):
        ui.label("Issue Feed").classes('text-3xl font-bold')
        ui.label("Search, filter, and find issues to resolve in your community.").classes('py-4 text-lg')
        with ui.element('div').classes('w-[90%] px-5 py-5 bg-white mb-8 rounded-2xl'):
            ui.input(placeholder='Search by keyboard, location, or reporter...').props('outlined').classes('w-full mb-4 rounded-2xl').style('background-color: #F7FFF7')
            with ui.element('div').classes('w-full flex justify-between items-center gap-2'):
                ui.select(options=["All", "High", "Medium", "Low"], label="Priority", value="All").props('outlined').classes('w-[48%]').style('background-color: #F7FFF7')
                ui.select(options=["All", "High", "Medium", "Easy"], label="Difficulty", value="All").props('outlined').classes('w-[48%]').style('background-color: #F7FFF7')
        with ui.grid(columns=3, rows=4).classes('w-[90%] px-5 gap-4'):
                # for i in range(6):
                #     show_issue_card()
                response = requests.get(url=f"{base_url}/api/issues?limit=0")
                print(response.status_code, response.content)
                json_data = response.json()
                for issue in json_data("data"):
                    show_issue_card(issue)
