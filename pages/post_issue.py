from nicegui import ui, app
import requests
from components.navbar import show_navbar
from utils.api import base_url

_issue_image = None

def _handle_image_upload(issue):
    global _issue_image
    _issue_image = issue.content

# function to create a post issue
def _post_issue(data, files):
    print(data)
    response = requests.post(url=f"{base_url}/api/issues", data=data, files=files, headers={"Authorization": f"Bearer {app.storage.user.get("access_token")}"},)
    print(response.status_code, response.content)
    if response.status_code == 200:
        # json_data = response.json()
        # print(json_data)
        ui.notify(
            message= "Issues added successfully!",
            type="positive")
        return ui.navigate.to("/issue_confirmation")
    elif response.status_code == 422:
        return ui.notify(message="Please ensure all inputs are filled!", type="negative")
    elif response.status_code == 401:
        return ui.navigate.to("/signin")
    elif response.status_code == 403:
        return ui.notify(
            message="Access denied!",
            type="info",
        )

@ui.page("/post_issue")
def show_post_issue():
    ui.query(".nicegui-row").classes("flex-nowrap")
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">'
    )

    show_navbar()

    with ui.element().style(
        "font-family: Raleway, serif; background-color:#F7FFF7"
    ).classes(
        "w-full min-h-screen flex flex-col justify-center items-center py-20 mt-10"
    ):
        ui.label("Report a New Issue").classes("text-3xl font-semibold mb-2")

        with ui.card().classes(
            "w-[30%] flex flex-col justify-center items-center mt-8 mb-8"
        ):
            title = ui.input(label="Title", placeholder="enter your issue title").props(
                "outlined"
            ).classes("w-full bg-white")
            description = ui.textarea(
                "Description", placeholder="describe your issue in detail..."
            ).props("outlined").classes("w-full bg-white")
            with ui.row().classes("w-full flex flex-row justify-around items-center"):
                ui.label("latitude")
                ui.label("longitude")
            with ui.row().classes("w-full flex flex-row justify-between items-center"):
                latitude = (
                    ui.input("Latitude")
                    .props("outlined type=number")
                    .classes("bg-white")
                )
                longitude = (
                    ui.input("Longitude")
                    .props("outlined type=number")
                    .classes("bg-white")
                )
            with ui.row().classes("w-full flex flex-row justify-around items-center"):
                with ui.element("div"):
                    # ui.label("Priority:")
                    priority_slider = ui.slider(min=1, max=3, value=1, step=1).props(
                        "color=teal-4"
                    )
                    # ui.label().bind_text_from(slider, "value")
                    priority_label = ui.label()  # Label that updates automatically

                    priority_map = {
                        1: "Low",
                        2: "Medium",
                        3: "High",
                    }  # Map numbers to text

                    # Bind slider value to display the corresponding text
                    priority_label.bind_text_from(
                        priority_slider,
                        "value",
                        lambda v: f"Priority: {priority_map.get(int(v), 'Unknown')}",
                    )

                with ui.element("div"):
                    # ui.label("Difficulty:")
                    difficulty_slider = ui.slider(min=1, max=3, value=1, step=1).props(
                        "color=teal-4"
                    )
                    # ui.label().bind_text_from(slider, "value")
                    difficulty_label = ui.label()  # Label that updates automatically

                    difficulty_map = {
                        1: "Easy",
                        2: "Medium",
                        3: "High",
                    }  # Map numbers to text

                    # Bind slider value to display the corresponding text
                    difficulty_label.bind_text_from(
                        difficulty_slider,
                        "value",
                        lambda v: f"Difficulty: {difficulty_map.get(int(v), 'Unknown')}",
                    )
            ui.upload(label="Upload photos", auto_upload=True, multiple=True, on_upload=_handle_image_upload).props(
                "color=teal-7"
            ).classes("w-full")
            ui.button(text="Submit Report", on_click=lambda: _post_issue(
                data={
                    "title": title.value,
                    "description": description.value,
                    "latitude": latitude.value,
                    "longitude": longitude.value,
                    "difficulty": difficulty_map[difficulty_slider.value].lower(),
                    "priority": priority_map[priority_slider.value].lower()
                },
                files={"picture_url": _issue_image}
            )).props("flat dense no-caps").style(
                "background-color:#007F7C"
            ).classes("w-full text-white py-2")
