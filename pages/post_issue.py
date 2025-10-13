from nicegui import ui


@ui.page("/post_issue")
def show_warrior():
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
        ui.label("Report a New Issue").classes("text-3xl font-semibold mb-4")

        with ui.card().classes(
            "w-[30%] flex flex-col justify-center items-center mt-8 mb-8"
        ):
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
                        slider,
                        "value",
                        lambda v: f"Priority: {priority_map.get(int(v), 'Unknown')}",
                    )

                with ui.element("div"):
                    # ui.label("Difficulty:")
                    slider = ui.slider(min=1, max=3, value=1, step=1).props(
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
                        slider,
                        "value",
                        lambda v: f"Difficulty: {difficulty_map.get(int(v), 'Unknown')}",
                    )
            ui.upload(label="Upload photos", auto_upload=True, multiple=True).props(
                "color=teal-7"
            ).classes("w-full")
            ui.button(text="Submit Report").props("flat dense no-caps").style(
                "background-color:#007F7C"
            ).classes("w-full text-white py-2")
