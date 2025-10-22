from nicegui import ui, app
from components.sidebar import show_sidebar
import requests
from utils.api import base_url


@ui.page("/user_profile")
def show_profile():
    ui.query(".nicegui-content").classes("p-0 m-0 gap-0")
    ui.query(".nicegui-row").classes("flex-nowrap")
    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">'
    )
    

    # === FETCH USER DATA FROM BACKEND ===
    try:
        response = requests.get(
            url=f"{base_url}/api/users/dashboard",
            headers={"Authorization": f"Bearer {app.storage.user.get('access_token')}"},
        )
        response.raise_for_status()
        user = response.json()
    except Exception as e:
        ui.notify(f"Failed to load user profile: {e}", color="red")
        return

    # === Extract user info ===
    name = user.get("display_name", "Anonymous User")
    avatar = user.get("avatar", None)
    username = user.get("username", "")
    email = user.get("email", "")
    points = user.get("points", 0)
    tasks_completed = user.get("tasks_completed", 0)
    tasks_reported = user.get("tasks_reported", 0)
    areas_cleaned = user.get("areas_cleaned", 0)
    created_at = user.get("created_at", "")

    # Build full avatar URL if needed
    if avatar:
        avatar_url = avatar if avatar.startswith("http") else f"{base_url}/{avatar}"
    else:
        avatar_url = None

    # === Layout ===
    with ui.element("main").classes(
        "w-full flex flex-row justify-between items-center"
    ):
        with ui.row().classes("w-[20%]").style(
            'font-family: "Raleway", serif; background-color:#F7FFF7;'
        ):
            show_sidebar()
        with ui.column().classes("w-[80%] py-10"):   
            # HEADER CARD
            with ui.card().classes("w-full max-w-4xl mx-auto p-8 mb-6").style(
                ""
            ):
                with ui.row().classes("w-full items-center justify-between"):

                    # === Profile Info Section ===
                    with ui.row().classes("items-center gap-6"):
                        if avatar_url:
                            ui.image(avatar_url).classes(
                                "w-24 h-24 rounded-full object-cover border-2 border-teal-700"
                            )
                        else:
                            ui.avatar(name[:2].upper()).classes(
                                "w-24 h-24 text-white text-2xl"
                            ).style("background-color: #007F7C")

                        with ui.column().classes("gap-2"):
                            ui.label(name).classes("text-3xl font-bold text-black")
                            ui.label(f"@{username}").classes("text-md text-gray-700 italic")
                            ui.label(email).classes("text-sm text-gray-600")
                            ui.label(f"Joined: {created_at}").classes(
                                "text-sm text-gray-600"
                            )

                            # Points Progress
                            with ui.column().classes("w-80"):
                                ui.linear_progress(value=min(points / 1000, 1.0)).classes(
                                    "h-2"
                                ).props("color=teal-7")
                                ui.label(f"{points}/1000 points to next level").classes(
                                    "text-sm text-gray-500"
                                )

                    # === Edit Profile Button ===
                    ui.button(
                        "Edit Profile", on_click=lambda: ui.navigate.to("/edit_profile")
                    ).props("flat dense no-caps").classes(
                        "px-6 py-3 rounded-lg text-white"
                    ).style(
                        "background-color: #007F7C"
                    )

            # === STATS SECTION ===
            with ui.row().classes("w-full max-w-4xl mx-auto gap-6 mb-8"):
                with ui.card().classes("flex-1 p-6 text-center"):
                    ui.label(points).classes("text-4xl font-bold").style("color: #007F7C")
                    ui.label("Total Points").classes("text-gray-600")

                with ui.card().classes("flex-1 p-6 text-center"):
                    ui.label(tasks_completed).classes("text-4xl font-bold").style(
                        "color: #007F7C"
                    )
                    ui.label("Tasks Completed").classes("text-gray-600")

                with ui.card().classes("flex-1 p-6 text-center"):
                    ui.label(tasks_reported).classes("text-4xl font-bold").style(
                        "color: #007F7C"
                    )
                    ui.label("Tasks Reported").classes("text-gray-600")

                with ui.card().classes("flex-1 p-6 text-center"):
                    ui.label(areas_cleaned).classes("text-4xl font-bold").style(
                        "color: #007F7C"
                    )
                    ui.label("Areas Cleaned").classes("text-gray-600")
