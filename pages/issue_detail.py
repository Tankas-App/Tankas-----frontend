from nicegui import ui


@ui.page("/issue_detail")
def show_issue_detail():
    ui.query(".nicegui-row").classes("flex-nowrap")
    with ui.element().classes(
        "w-full min-h-screen bg-gray-100 flex flex-col justify-center items-center rounded"
    ):
        ui.label("Issue details").classes("text-2xl mt-8 mb-5")
        with ui.card().classes(
            "w-[50%] h-[95%] flex flex-col justify-center items-center rounded-2xl mb-8"
        ):
            with ui.column().classes("items-start w-full h-full"):
                ui.image("image").classes("w-full h-[1/2] object-cover rounded-t")
                ui.label("Title").classes("text-sm  mt-4")
                ui.label("Description").classes(
                    "font-semdbold text-center max-w-xl mt-2"
                )
                ui.label(f"Difficulty").classes("text-sm font-semibold")
                ui.label(f"Priority").classes("text-sm font-semibold ")
                with ui.row().classes("w-full flex flex-row  items-start"):
                    ui.button("Volunteer").props("flat dense no-caps").classes(
                        "w-[50%] bg-green-400  text-white rounded-xl"
                    )
                    ui.button("Submit Fix").props("flat dense no-caps").classes(
                        "w-[50%] bg-green-100 text-black rounded-xl"
                    )
