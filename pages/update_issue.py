from nicegui import ui, app
from components.navbar import show_navbar
import requests
from utils.api import base_url

issue_image = None


def _handle_image_upload(issue):
    global _issue_image
    _issue_image = issue.content


# function to create a post issue
def _post_issue(data, files):
    print(data)
    response = requests.post(
        url=f"{base_url}/api/issues",
        data=data,
        files=files,
        headers={"Authorization": f"Bearer {app.storage.user.get("access_token")}"},
    )
    print(response.status_code, response.content)
    if response.status_code == 200:
        # json_data = response.json()
        # print(json_data)
        # issue = json_data["data"]
        ui.notify(message="Issues added successfully!", type="positive")
        return ui.navigate.to("/issue_confirmation")
    elif response.status_code == 422:
        return ui.notify(
            message="Please ensure all inputs are filled!", type="negative"
        )
    elif response.status_code == 401:
        return ui.navigate.to("/signin")
    elif response.status_code == 403:
        return ui.notify(
            message="Access denied!",
            type="info",
        )


@ui.page("/update_issue")
def show_update_issue():
    show_navbar()

    ui.query(".nicegui-row").classes("flex-nowrap")
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">'
    )
    with ui.element().style(
        "font-family: Raleway, serif; background-color:#F7FFF7"
    ).classes(
        "w-full min-h-screen flex flex-col justify-center items-center py-20 mt-10"
    ):
        ui.label("Update an Issue").classes("text-3xl font-semibold mb-2")

        with ui.card().classes(
            "w-[30%] flex flex-col justify-center items-center mt-8 mb-8"
        ):
            title = (
                ui.input(label="Title", placeholder="enter your issue title")
                .props("outlined")
                .classes("w-full bg-white")
            )
            description = (
                ui.textarea(
                    "Description", placeholder="describe your issue in detail..."
                )
                .props("outlined")
                .classes("w-full bg-white")
            )
            status = (
                ui.input(label="status", placeholder="isuse status")
                .props("outlined")
                .classes("w-full bg-white")
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
            ui.upload(
                label="Upload photos",
                auto_upload=True,
                multiple=True,
                on_upload=_handle_image_upload,
            ).props("color=teal-7").classes("w-full")
            ui.button(
                text="Submit Update",
            ).props("flat dense no-caps").style(
                "background-color:#007F7C"
            ).classes("w-full text-white py-2")
