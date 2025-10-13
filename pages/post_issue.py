from nicegui import ui


@ui.page("/post_issue")
def show_warrior():
    ui.query(".nicegui-row").classes("flex-nowrap")

    with ui.element().classes(
        "w-full min-h-screen flex flex-col justify-center items-center bg-gray-100"
    ):
        with ui.card().classes(
            "w-[30%] bg-green-100 flex flex-col justify-center items-center mt-8 mb-8"
        ):
            ui.label("Report a New Issue").classes("text-2xl")
            ui.input(label="Title", placeholder="enter your issue title").props(
                "outlined"
            ).classes("w-full bg-white")
            ui.textarea(
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
                    slider = ui.slider(min=1, max=3, value=1, step=1).props(
                        "color=green"
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
                        slider,
                        "value",
                        lambda v: f"Priority: {priority_map.get(int(v), 'Unknown')}",
                    )

                with ui.element("div"):
                    # ui.label("Difficulty:")
                    slider = ui.slider(min=1, max=3, value=1, step=1).props(
                        "color=green"
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
                        slider,
                        "value",
                        lambda v: f"Difficulty: {difficulty_map.get(int(v), 'Unknown')}",
                    )
            ui.upload(label="Upload photos", auto_upload=True, multiple=True).props(
                "color=green"
            ).classes("w-full")
            ui.button(text="Submit Report").props("flat dense no-caps").classes(
                "w-full bg-green-500 text-black text-lg"
            )
