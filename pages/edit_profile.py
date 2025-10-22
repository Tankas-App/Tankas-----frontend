from nicegui import ui, app
import httpx
import requests
from utils.api import base_url


@ui.page("/edit_profile")
def edit_profile():
    ui.query(".nicegui-content").classes("p-0 m-0 gap-0")

    token = app.storage.user.get("access_token")

    # === Fetch current user info ===
    try:
        response = requests.get(
            f"{base_url}/api/users/dashboard",
            headers={"Authorization": f"Bearer {token}"},
        )
        user = response.json()
    except Exception as e:
        ui.notify(f"Failed to load user data: {e}", color="red")
        return

    display_name = user.get("display_name", "")
    avatar = user.get("avatar", None)
    avatar_url = (
        f"{base_url}/{avatar}" if avatar and not avatar.startswith("http") else avatar
    )

    # === Async Avatar Upload Function ===
    async def upload_avatar(event):
        print(event)
        try:
            file = event.file
            if hasattr(file, "_path") and file._path:
                with open(file._path, "rb") as f:
                    content = f.read()
            elif hasattr(file, "_data"):
                content = file._data

            async with httpx.AsyncClient() as client:
                files = {"file": (file.name, content, file.content_type)}
                response = await client.put(
                    f"{base_url}/api/users/me/avatar",
                    headers={"Authorization": f"Bearer {token}"},
                    files=files,
                )
            if response.status_code == 200:
                ui.notify("Avatar updated!", color="green")
                new_avatar = response.json().get("avatar")
                if new_avatar:
                    new_avatar_url = (
                        f"{base_url}/{new_avatar}"
                        if not new_avatar.startswith("http")
                        else new_avatar
                    )
                    avatar_image.source = new_avatar_url
            else:
                ui.notify(f"Upload failed: {response.text}", color="red")
        except Exception as e:
            ui.notify(f"Error: {e}", color="red")

    # === Save Profile Function ===
    def save_profile():
        payload = {"display_name": name_input.value}
        try:
            response = requests.put(
                f"{base_url}/api/users/me",
                json=payload,
                headers={"Authorization": f"Bearer {token}"},
            )
            if response.status_code == 200:
                ui.notify("Profile updated!", color="green")
                ui.navigate.to("/user_profile")
            else:
                ui.notify(f"Update failed: {response.text}", color="red")
        except Exception as e:
            ui.notify(f"Error: {e}", color="red")

    # === UI Layout ===
    with ui.column().classes(
        "w-full min-h-screen items-center justify-center items-center p-8"
    ).style("background-color:#F7FFF7"):

        with ui.card().classes("w-[30%] p-6 bg-white shadow-lg rounded-xl"):

            ui.label("Edit Profile").classes(
                "w-full text-2xl font-bold mb-4 justify-center items-center flex"
            )

            # Avatar Display
            with ui.row().classes(" w-full justify-center items-center mb-4"):
                if avatar_url:
                    avatar_image = ui.image(avatar_url).classes(
                        "w-24 h-24 rounded-full object-cover border-2 border-teal-700"
                    )
                else:
                    avatar_image = (
                        ui.avatar(display_name[:2].upper())
                        .classes("w-24 h-24 text-white text-2xl")
                        .style("background-color: #007F7C")
                    )

            # Upload Button (binds to async handler)
            ui.upload(
                label="Upload new avatar",
                on_upload=upload_avatar,
                auto_upload=True,
                multiple=False,
            ).props("accept=image/* color=teal-7").classes("mb-4 w-full")

            # Display Name Input
            name_input = (
                ui.input("Display Name", value=display_name)
                .props("outlined color=teal-7")
                .classes("mb-4 w-full")
            )

            # Save Button
            ui.button("Save Changes", on_click=save_profile).classes(
                "text-white rounded-lg px-4 py-2 w-full"
            ).style("background-color: #007F7C").props("flat dense no-caps")
            ui.button("Cancel", on_click=lambda: ui.navigate.back()).classes(
                "text-white rounded-lg px-4 py-2 w-full"
            ).style("background-color: #ade6e5ff").props("flat dense no-caps")
