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

    avatar = user.get("avatar", None)

    # Build full avatar URL if needed
    if avatar:
        avatar_url = avatar if avatar.startswith("http") else f"{base_url}/{avatar}"
    else:
        avatar_url = None

    # ---- Sidebar container ----
    with ui.column().classes(
        "w-[20%] h-screen bg-gray-200 fixed left-0 top-0 z-50 text-white px-2 py-10 space-y-4"
    ).style('background-color: #F7FFF7; font-family: "Raleway", serif;'):

        # Navigation menu
        with ui.column().classes("gap-1 w-full"):
            # Logo
            with ui.row().classes("justify-center items-center w-full px-4"):
                ui.image("/assets/Logo1.png").classes(
                    "cursor-pointer w-1/4"
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
                if avatar_url:
                            ui.image(avatar_url).classes(
                                "w-16 h-16 rounded-full object-cover border-2 border-teal-700"
                            )
                else:
                    ui.avatar(name[:2].upper()).classes(
                        "w-24 h-24 text-white text-2xl"
                    ).style("background-color: #007F7C")

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
