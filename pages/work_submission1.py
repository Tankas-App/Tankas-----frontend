from nicegui import ui, app
import requests
from utils.api import base_url
import io

_issue_image = None


async def _handle_image_upload(issue):
    global _issue_image

    # Get the file path
    file = issue.file
    if hasattr(file, "_path") and file._path:

        with open(file._path, "rb") as f:
            file_bytes = f.read()
    elif hasattr(file, "_data"):
        file_bytes = file._data

    _issue_image = (issue.file.name, io.BytesIO(file_bytes), issue.file.content_type)
    print(
        f"Uploaded: {issue.file.name}, type: {issue.file.content_type}, size: {len(file_bytes)} bytes"
    )


# function to create a post issue
def _submit_issue(files):
    print(files)
    response = requests.post(
        url=f"{base_url}/api/issues",
        files=files,
        headers={"Authorization": f"Bearer {app.storage.user.get("access_token")}"},
    )
    print(response.status_code, response.content)
    if response.status_code == 200:
        # json_data = response.json()
        # print(json_data)
        ui.notify(message="Work submitted successfully!", type="positive")
        return ui.navigate.to("/review_submission")
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

    # Tailwind custom colors (inline style overrides)


MINT_CREAM = "#F7FFF7"
TEAL = "#007F7C"
LIGHT_TEAL = "#ade6e5ff"
BLUE = "#2E86AB"
NIGHT = "#0A0A0A"
GOLD = "#f8d50eff"


@ui.page("/work_submission1")
def show_work_submission1():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    ui.query(".nicegui-row").classes("flex-nowrap")

    # Page background
    ui.add_head_html(
        f"""
    <style>
    body {{
        background-color: {MINT_CREAM};
        font-family: 'Inter', sans-serif;
    }}
    .step-active {{
        background-color: {TEAL};
        color: white;
    }}
    .step-inactive {{
        background-color: #E5E7EB;
        color: #6B7280;
    }}
    </style>
    """
    )

    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">'
    )

    issue = None

    issue_id = ui.context.client.request.query_params.get("id")
    print(issue)
    try:
        response = requests.get(url=f"{base_url}/api/issues/{issue_id}")
        # print(response.status_code, response.content)
        if response.status_code == 200:
            json_data = response.json()
            print(json_data)
            issue = json_data

        else:
            # Add a visual notification if the API call fails
            ui.notify(f"Error fetching issue: {response.status_code}", type="negative")

    except requests.exceptions.RequestException as e:
        ui.notify(f"Network error: {e}", type="negative")

    # === SAFE IMAGE RENDERING ===
    before_image_url = (
        issue.get("picture_url")
        if issue and isinstance(issue, dict) and issue.get("picture_url")
        else "https://via.placeholder.com/400x300?text=Before+Image"
    )

    with ui.column().classes(
        "w-full h-screen justify-center items-center px-10 py-10"
    ).style('font-family: "Raleway", serif; background-color:#F7FFF7;'):
        ui.label("Submit Your Work").classes(f"text-[{BLUE}] font-bold text-3xl")

        # STEPS
        with ui.row().classes("w-full justify-center space-x-8"):
            with ui.column().classes("items-center"):
                ui.label("1").classes(
                    "step-active rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold"
                )
                ui.label("Upload Photos").classes("text-sm text-gray-600")
            ui.separator().props("vertical=false").classes(
                "w-10 bg-gray-300 h-0.5 mt-5"
            )
            with ui.column().classes("items-center"):
                ui.label("2").classes(
                    f"step-inactive rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold"
                )
                ui.label("Add Details").classes("text-sm text-gray-600")
            ui.separator().props("vertical=false").classes(
                "w-10 bg-gray-300 h-0.5 mt-5"
            )
            with ui.column().classes("items-center"):
                ui.label("3").classes(
                    f"step-inactive rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold"
                )
                ui.label("Review & Submit").classes("text-sm text-gray-600")

        # PHOTO UPLOAD SECTION
        with ui.row().classes("w-[70%] h-[60%] justify-between items-center mt-8"):
            with ui.column().classes("w-1/2 h-full justify-center items-center"):
                ui.label("Before").classes(f"text-[{NIGHT}] font-semibold text-lg")
                ui.image(before_image_url).classes("object-cover w-[70%] h-full")

            with ui.column().classes("w-1/2 h-full justify-center items-center"):
                ui.label("After").classes(f"text-[{NIGHT}] font-semibold text-lg")
                # with ui.card().classes('border-2 border-dashed border-gray-300 rounded-lg text-center hover:border-gray-500 transition'):
                ui.upload(
                    label="Click to upload photo",
                    auto_upload=True,
                    on_upload=_handle_image_upload,
                ).classes("w-[70%] h-full").props("color=teal-7")

    with ui.column().classes(
        "w-full h-screen justfify-center items-center px-10 py-10"
    ).style('font-family: "Raleway", serif; background-color:#F7FFF7;'):
        # # === Step Indicator ===
        # with ui.row().classes('justify-between items-center w-full'):
        #     ui.label('Step 2 of 3').classes(f'text-[{NIGHT}] text-sm font-medium')
        # with ui.row().classes('w-full'):
        #     with ui.element('div').classes('w-full bg-gray-200 h-1 rounded-full'):
        #         ui.element('div').classes('progress-bar rounded-full w-2/3')

        # === Page Title ===
        ui.label("Add Details to Your Submission").classes(
            f"text-[{BLUE}] font-bold text-3xl text-center"
        )

        # STEPS
        with ui.row().classes("w-full justify-center space-x-8"):
            with ui.column().classes("items-center"):
                ui.label("1").classes(
                    "step-inactive rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold"
                )
                ui.label("Upload Photos").classes("text-sm text-gray-600")
            ui.separator().props("vertical=false").classes(
                "w-10 bg-gray-300 h-0.5 mt-5"
            )
            with ui.column().classes("items-center"):
                ui.label("2").classes(
                    "step-active rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold"
                )
                ui.label("Add Details").classes("text-sm text-gray-600")
            ui.separator().props("vertical=false").classes(
                "w-10 bg-gray-300 h-0.5 mt-5"
            )
            with ui.column().classes("items-center"):
                ui.label("3").classes(
                    "step-inactive rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold"
                )
                ui.label("Review & Submit").classes("text-sm text-gray-600")

        # === Content Layout ===
        with ui.row().classes("w-[70%] h-[60%] justify-between items-center mt-8"):
            # Left: Image preview
            with ui.column().classes("w-1/2 h-full justify-center items-center"):
                ui.image(
                    "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=600&q=80"
                ).classes("object-cover w-[70%] h-full")

            # Right: Input fields
            with ui.column().classes("w-1/2 h-full justify-center items-center"):
                # Caption
                # ui.label('Caption').classes(f'text-[{NIGHT}] font-semibold')
                ui.textarea(
                    placeholder="Write a caption or a brief summary of your work..."
                ).classes(
                    "w-full bg-white px-5 rounded-lg border border-gray-300 focus:border-teal-600 focus:ring-0"
                )

                # Effort & Amount Row
                with ui.row().classes("w-full space-x-4"):
                    with ui.column().classes("w-1/2"):
                        ui.label("Effort Summary (Optional)").classes(
                            f"text-[{NIGHT}] text-sm font-medium"
                        )
                        ui.input(placeholder="e.g., 2 hours").classes(
                            "w-full bg-white px-5 rounded-lg border border-gray-300 focus:border-teal-600 focus:ring-0"
                        )
                    with ui.column().classes("w-1/2"):
                        ui.label("Amount of Refuse").classes(
                            f"text-[{NIGHT}] text-sm font-medium"
                        )
                        ui.input(placeholder="e.g., 5 bags").classes(
                            "w-full bg-white px-5 rounded-lg border border-gray-300 focus:border-teal-600 focus:ring-0"
                        )

                # Difficulty Rating
                ui.label("Difficulty Rating").classes(
                    f"text-[{NIGHT}] text-sm font-medium flex items-center space-x-1"
                )
                ui.select(["Easy", "Medium", "Hard"], value="Easy").classes(
                    "w-full bg-white px-5 rounded-lg border border-gray-300 focus:border-teal-600 focus:ring-0"
                )

        # FOOTER BUTTONS
    with ui.row().classes("w-full justify-around mt-8 px-20 py-10"):
        ui.button("Cancel", on_click=lambda: ui.navigate.back()).props(
            "flat dense no-caps"
        ).classes("text-lg font-semibold px-10 py-2 rounded-lg").style(
            "background-color: #ade6e5ff;"
        )
        ui.button(
            "Next",
            on_click=lambda: _submit_issue(
                files={"picture": _issue_image},
            ),
        ).props("flat dense no-caps").classes(
            "text-white text-lg font-semibold px-10 py-2 rounded-lg"
        ).style(
            "background-color: #007F7C"
        )
