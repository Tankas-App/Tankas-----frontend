from nicegui import ui, app
from components.sidebar import show_sidebar
import requests
from utils.api import base_url


@ui.page("/dashboard")
def show_dashboard():
    ui.query(".nicegui-row").classes("flex-nowrap")
    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">'
    )

    user = None

    try:
        response = requests.get(
            url=f"{base_url}/api/users/dashboard",
            headers={"Authorization": f"Bearer {app.storage.user.get("access_token")}"},
        )
        # print(response.status_code, response.content)
        if response.status_code == 200:
            json_data = response.json()
            print(json_data)
            user = json_data

        else:
            # Add a visual notification if the API call fails
            ui.notify(f"Error fetching issue: {response.status_code}", type="negative")

    except requests.exceptions.RequestException as e:
        ui.notify(f"Network error: {e}", type="negative")

    # response = requests.get(url=f"{base_url}/api/users/dashboard")
    # # print(response.status_code, response.content)
    # json_data = response.json()
    # print(f"This is the User Data : {json_data}")
    # user = json_data

    with ui.element("main").classes(
        "w-full flex flex-row justify-between items-center"
    ):
        with ui.row().classes("w-[20%]").style(
            'font-family: "Raleway", serif; background-color:#F7FFF7;'
        ):
            show_sidebar()

        with ui.column().classes("w-[80%]"):
            if user:
                with ui.element("div").classes("w-full px-5 py-10"):
                    with ui.row().classes(""):
                        # Header
                        ui.label(f"Welcome back,").classes("text-3xl font-bold mb-6")
                        ui.label(text=user["username"]).classes(
                            "text-3xl font-bold mb-6"
                        )

                    # Top Cards
                    with ui.grid().classes("gap-6 mb-6 flex flex-col sm:flex-row"):
                        with ui.card().classes(
                            "flex-1 p-6 rounded-xl shadow-sm border border-gray-200 bg-white"
                        ):
                            ui.label("Reported Issues").classes("text-gray-500")
                            ui.label(text=user["tasks_reported"]).classes(
                                "text-3xl font-bold mt-2"
                            )
                        with ui.card().classes(
                            "flex-1 p-6 rounded-xl shadow-sm border border-gray-200 bg-white"
                        ):
                            ui.label("Current Points").classes("text-gray-500")
                            ui.label(text=user["points"]).classes(
                                "text-3xl font-bold mt-2"
                            )

                        with ui.card().classes(
                            "flex-1 p-6 rounded-xl shadow-sm border border-gray-200 bg-white"
                        ):
                            ui.label("Tasks Completed").classes("text-gray-500")
                            ui.label(text=user["tasks_completed"]).classes(
                                "text-3xl font-bold mt-2"
                            )
                        with ui.card().classes(
                            "flex-1 p-6 rounded-xl shadow-sm border border-gray-200 bg-white"
                        ):
                            ui.label("Areas Cleaned").classes("text-gray-500")
                            ui.label(text=user["areas_cleaned"]).classes(
                                "text-3xl font-bold mt-2"
                            )

                    # Buttons
                    with ui.row().classes("w-full gap-4 mb-8 flex flex-row justify-between items-center sm:flex-row"):
                        ui.button(
                            "Report a New Issue",
                            on_click=lambda: ui.navigate.to("/post_issue"),
                        ).classes("w-1/2 text-white font-semibold rounded-full py-3").style(
                            "background-color: #007F7C;"
                        ).props('flat dense no-caps')
                        ui.button("Volunteer Now", on_click=lambda: ui.navigate.to("/volunteer")).classes(
                            "w-1/2 text-white font-semibold rounded-full py-3"
                        ).props('flat dense no-caps').style('background-color: #007F7C;')

                    # Progress Section
                    with ui.card().classes(
                        "p-6 rounded-xl shadow-sm border border-gray-200 bg-white mb-8"
                    ):
                        with ui.row().classes("justify-between mb-2"):
                            ui.label("Level 5").classes("font-semibold")
                            ui.label("Next Reward: Eco–Warrior Badge").classes(
                                "text-gray-600 text-sm"
                            )
                        ui.linear_progress(value=0.45).props("color=teal-7").classes(
                            "h-2 rounded-full"
                        )
                        ui.label("450 / 1000 XP").classes(
                            "text-right text-gray-500 text-sm mt-2"
                        )

                    # Recent Activity
                    ui.label("Recent Activity").classes("text-xl font-bold mb-4")
                    activities = [
                        ("You reported a clogged drain on Main Street.", "2 hours ago"),
                        ("You volunteered for the park cleanup event.", "1 day ago"),
                        (
                            "Issue 'Broken Streetlight' was resolved. +50 points!",
                            "3 days ago",
                        ),
                    ]
                    for text, time in activities:
                        with ui.card().classes(
                            "p-4 mb-3 rounded-xl border border-gray-200 bg-white flex flex-col gap-1"
                        ):
                            with ui.row().classes("gap-2 items-center"):
                                ui.icon("info").style("color: #007F7C;")
                                ui.label(text).classes("text-gray-800")
                            ui.label(time).classes("text-gray-500 text-sm ml-6")
            else:
                # 4. Fallback UI if the issue data failed to load
                with ui.element("main").classes(
                    "w-full flex justify-center items-center"
                ):
                    ui.label("User details not found.").classes(
                        "text-center text-xl text-red-600"
                    )
