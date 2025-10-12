from nicegui import ui


@ui.page("/suggest_reward")
def show_suggest_reward():
    with ui.element().classes(
        "w-full min-h-screen flex flex-col justify-center items-center bg-gray-100 rounded"
    ):
        ui.label("Suggest a Reward").classes("text-4xl font-bold mt-10")
        ui.label("Got a great idea for a new reward? Let us know").classes("mb-5")
        with ui.card().classes(
            "w-[40%] bg-gray-200 flex flex-col justify-center items-center rounded-3xl mb-8"
        ):
            ui.label("Reward Name").classes("self-start text-left w-full ml-1")
            ui.input(placeholder="e.g. trash bins").props("borderless").classes(
                "w-full bg-gray-100 rounded-2xl border-none outline-none focus:ring-0"
            )
            ui.label("Description").classes("self-start text-left w-full ml-1")
            ui.textarea(
                placeholder="A brief description of what makes this reward special",
            ).props("borderless").classes(
                "w-full bg-gray-100 rounded-2xl border-none outline-none focus:ring-0"
            )
            ui.label("Estimated Point Value").classes(
                "self-start text-left w-full ml-1"
            )
            ui.input(placeholder="e.g. 5000").props("borderless").classes(
                "w-full bg-gray-100 rounded-2xl border-none outline-none focus:ring-0"
            )
            ui.label("Category").classes("self-start text-left w-full ml-1")
            ui.select(
                label="Choose event type",
                options=[
                    "Community Upgrades",
                    "Local Business Voucher",
                    "Public Recognition",
                    "Event Access",
                    "Health & Wellness",
                ],
                value=None,
            ).props("borderless").classes(
                "w-full bg-gray-100 rounded-2xl border-none outline-none focus:ring-0"
            )
            ui.button("Submit Suggestion").props("flat dense no-caps").classes(
                "w-full bg-green-400 text-black text-lg  rounded-xl"
            )
