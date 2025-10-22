from nicegui import ui


@ui.page("/volunteer")
def join_movement_page():
    ui.query(".nicegui-content").classes("p-0 m-0 gap-0")
    ui.query(".nicegui-row").classes("flex no-wrap")
    # Tailwind CDN
    ui.add_head_html(
        """
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
    tailwind.config = {
        theme: {
            extend: {
                colors: {
                    mint: '#F7FFF7',
                    teal: '#007F7C',
                    lightteal: '#ade6e5ff',
                    blue: '#2E86AB',
                    night: '#0A0A0A',
                    gold: '#f8d50eff'
                }
            }
        }
    }
    </script>
    """
    )

    with ui.element("main").classes(
        "w-full min-h-screen flex justify-center items-start pt-20 px-5 mb-8"
    ).style('background-color: #F7FFF7; font-family: "Raleway", sans-serif;'):
        with ui.element("div").classes(
            "w-full max-w-3xl bg-mint rounded-xl p-10 shadow-lg flex flex-col space-y-8"
        ):

            # Header Section
            with ui.element("div").classes("flex flex-col space-y-2"):
                ui.label("Tankas Community Clean-Up").classes(
                    "text-night font-semibold text-lg"
                )
                ui.label("Join Our Volunteers").classes("text-2xl font-bold").style(
                    "color: #2E86AB"
                )
                ui.label("Help us make our community cleaner and greener.").classes(
                    "text-night opacity-70"
                )

            # Form Section
            with ui.element("form").classes("flex flex-col space-y-6"):

                # Name & Email
                with ui.row().classes("w-full gap-4"):
                    ui.input(placeholder="Enter your display name").classes(
                        "w-1/2 rounded-lg border border-gray-300 p-3 focus:outline-none focus:ring-2 focus:ring-teal"
                    )
                    ui.input(placeholder="e.g., john.doe@email.com").classes(
                        "w-1/2 rounded-lg border border-gray-300 p-3 focus:outline-none focus:ring-2 focus:ring-teal"
                    )

                # Phone Number
                # ui.input("Phone Number", placeholder="Enter your phone number").classes(
                #     "w-full rounded-lg border border-gray-300 p-3 focus:outline-none focus:ring-2 focus:ring-teal"
                # )

                # Availability Section
                ui.label("Your Availability").classes(
                    "text-night font-semibold text-lg"
                )
                ui.label("Select the days you are generally available.").classes(
                    "text-night opacity-70"
                )

                with ui.row().classes("gap-6 items-center"):
                    with ui.row().classes("items-center gap-2"):
                        ui.checkbox().classes("text-night")  # checkbox itself
                        ui.label("Weekdays").classes(
                            "text-night"
                        )  # label beside checkbox

                    with ui.row().classes("items-center gap-2"):
                        ui.checkbox().classes("text-night")
                        ui.label("Weekends").classes("text-night")

                    with ui.row().classes("items-center gap-2"):
                        ui.checkbox().classes("text-night")
                        ui.label("Flexible").classes("text-night")

                # For the longer checkbox text
                with ui.row().classes("items-start mt-4"):
                    ui.checkbox().classes("text-night")
                    ui.label(
                        "Yes, I'm interested in participating in community cleaning events!"
                    ).classes("text-night")

                ui.button('Submit', on_click=lambda: ui.navigate.to("/all_volunteers")).classes(
                    "bg-teal text-white px-6 py-3 rounded-full font-semibold text-lg hover:bg-teal-700 transition duration-300"
                ).props('flat dense no-caps')
