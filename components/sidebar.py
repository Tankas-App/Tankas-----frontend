from nicegui import ui, app
import requests
from utils.api import base_url  # e.g. "http://localhost:8000"


def show_sidebar():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")

    # ---- Fetch user info from backend ----
    try:
        response = requests.get(
            url=f"{base_url}/api/users/dashboard",
            headers={"Authorization": f"Bearer {app.storage.user.get("access_token")}"},
        )
        if response.status_code == 200:
            user = response.json()
        else:
            user = {"display_name": "Unknown User", "email": "N/A", "avatar": ""}
            ui.notify("Failed to fetch user info", color="red")
    except Exception as e:
        user = {"display_name": "Unknown User", "email": "N/A", "avatar": ""}
        ui.notify(f"Error fetching profile: {e}", color="red")

    # ---- Sidebar container ----
    with ui.column().classes(
        "w-[20%] h-screen bg-gray-200 fixed left-0 top-0 z-50 text-white px-10 py-20 space-y-4"
    ).style('background-color: #F7FFF7; font-family: "Raleway", serif;'):

        # Navigation menu
        with ui.column().classes("gap-1 w-full"):
            # Logo
            with ui.row().classes("justify-center items-center w-full px-4 py-2"):
                ui.image("/assets/Tankas_Brand_Mark@2x.png").classes(
                    "cursor-pointer w-1/7"
                ).on("click", lambda: ui.navigate.to("/"))

            ui.separator().classes("w-full border-t border-gray-300 my-2")

            ui.button(
                "Dashboard",
                on_click=lambda: ui.navigate.to("/dashboard"),
                icon="grid_view",
            ).classes(
                "w-full justify-start items-start text-black py-3 px-4 hover:text-lg"
            ).props(
                "flat dense no-caps"
            )

            ui.button(
                "Issue Feed", on_click=lambda: ui.navigate.to("/issues"), icon="list"
            ).classes(
                "w-full justify-start items-start text-black py-3 px-4 hover:text-lg"
            ).props(
                "flat dense no-caps"
            )

            ui.button(
                "Warriors", on_click=lambda: ui.navigate.to("/warrior"), icon="wc"
            ).classes(
                "w-full justify-start items-start text-black py-3 px-4 hover:text-lg"
            ).props(
                "flat dense no-caps"
            )

            ui.button(
                "Leaderboard",
                on_click=lambda: ui.navigate.to("/rewards"),
                icon="leaderboard",
            ).classes(
                "w-full justify-start items-start text-black py-3 px-4 hover:text-lg"
            ).props(
                "flat dense no-caps"
            )

            ui.button(
                "Suggest Reward",
                on_click=lambda: ui.navigate.to("/suggest_reward"),
                icon="emoji_events",
            ).classes(
                "w-full justify-start items-start text-black py-3 px-4 hover:text-lg"
            ).props(
                "flat dense no-caps"
            )

        # ---- User profile section at bottom ----
        with ui.column().classes("w-full py-2 px-4 mt-auto"):
            with ui.row().classes("items-center gap-2 cursor-pointer").on(
                "click", lambda: ui.navigate.to("/user_profile")
            ):
                # Avatar
                avatar_text = (
                    user["display_name"][0].upper() if user.get("display_name") else "U"
                )
                ui.avatar(avatar_text).classes("text-white").props("color=teal-7")

                # Info
                with ui.column().classes("gap-1"):
                    ui.label(user.get("display_name", "User Name")).classes(
                        "font-medium text-gray-900 dark:text-gray-100"
                    )
                    ui.label(user.get("email", "user@email.com")).classes(
                        "text-sm text-gray-500 dark:text-gray-400"
                    )

            # Sign out
            ui.button("Sign Out", on_click=lambda: ui.navigate.to("/signin")).classes(
                "w-full py-3 mt-2"
            ).props("flat dense no-caps").style(
                "background-color: #ade6e5ff; border: none;"
            )
