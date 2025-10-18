from nicegui import ui


@ui.page("/warrior")
def show_warrior():
    ui.query(".nicegui-row").classes("flex no-wrap")
    ui.query(".nicegui-content").classes("p-0 m-0 gap-0")

    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;600;800&display=swap" rel="stylesheet">'
    )

    # ====== HEADER ======
    with ui.header().classes(
        "justify-between items-center px-8 py-6 bg-white shadow-sm"
    ):
        with ui.row().classes("items-center gap-3"):
            ui.image("/assets/Logo.png").classes("h-10 w-auto")
        with ui.row().classes("items-center gap-6"):
            ui.link("Dashboard", "/dashboard").classes("no-underline text-lg")
            ui.link("Report an Issue", "/post_issue").classes("no-underline text-lg")
            ui.button("Volunteer", color="teal-600").props("no-caps").classes(
                "rounded-full px-4"
            )
            ui.button("My Profile", color="teal-600").props("no-caps").classes(
                "rounded-full px-4"
            )
            ui.avatar("https://randomuser.me/api/portraits/men/11.jpg")

    with ui.element().style(
        "font-family: Raleway, serif; background-color:#F7FFF7"
    ).classes("w-full flex flex-col items-center"):

        with ui.column().classes("w-[80%] mx-auto text-left mt-10 mb-6"):
            ui.label("Our Warriors in Action").classes(
                "text-3xl font-bold text-gray-900"
            )
            ui.label(
                "See the incredible impact our community is making together!"
            ).classes("text-green-600 text-md mb-6")
            with ui.row().classes("flex-wrap gap-3 mb-6"):
                ui.button("All", color="teal-600").props("no-outline no-caps")
                ui.button("In Progress", color="teal-400").props("no-outline no-caps")
                ui.button("Recently Completed", color="teal-600").props(
                    "no-outline no-caps"
                )
                ui.button("Highest Impact", color="teal-600").props(
                    "no-outline no-caps"
                )

        # Cards Section
        with ui.row().classes(
            "w-[80%] min-h-screen mx-auto flex-wrap justify-between gap-6 items-start"
        ):
            # LEFT COLUMN
            with ui.column().classes("w-full lg:w-[60%] flex flex-col gap-6"):
                with ui.card().style("background-color:#ade6e5ff;").classes(
                    "w-full flex flex-row items-center gap-4 p-4 rounded-3xl shadow-xl"
                ):
                    ui.image(
                        "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=400"
                    ).classes("w-35 h-45 object-cover rounded-xl")
                    with ui.column().classes("flex-1"):
                        ui.label("In Progress").classes("text-green-600 text-sm")
                        ui.label("Park Cleanup at Sunrise").classes(
                            "text-lg font-semibold"
                        )
                        ui.label("Completion Status").classes(
                            "text-sm text-gray-500 mt-1"
                        )
                        ui.linear_progress(
                            value=0.75, show_value=True, color="teal-600"
                        ).classes("w-full h-3 mt-1 rounded")
                        with ui.row().classes("items-center gap-2 mt-2"):
                            ui.avatar(
                                "https://randomuser.me/api/portraits/women/20.jpg"
                            )
                            ui.label("Jane D.").classes("text-sm")
                        with ui.row():
                            ui.label("Last updated 2 hours ago").classes(
                                "text-xs text-gray-400 mt-1"
                            )
                            ui.button(
                                "Kudos",
                            ).props("flat no-caps").classes(
                                "mt-2 rounded-full px-3 py-1 text-white text-sm bg-teal-600"
                            )

                with ui.card().style("background-color:#ade6e5ff;").classes(
                    "w-full flex flex-row items-center gap-4 p-4 rounded-3xl shadow-xl"
                ):
                    ui.image(
                        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=400"
                    ).classes("w-35 h-45 object-cover rounded-xl")
                    with ui.column().classes("flex-1"):
                        ui.label("Recently Completed").classes("text-blue-600 text-sm")
                        ui.label("Riverbank Restoration").classes(
                            "text-lg font-semibold"
                        )
                        with ui.row().classes("items-center gap-2 mt-2"):
                            ui.avatar("https://randomuser.me/api/portraits/men/32.jpg")
                            ui.label("John A.").classes("text-sm")
                        ui.label("250 sqft   ·   150 lbs").classes(
                            "text-xs text-gray-500 mt-1"
                        )
                        ui.label("Completed on 24th July 2025").classes(
                            "text-xs text-gray-400 mt-1"
                        )
                        ui.button(
                            "Kudos",
                        ).props("flat no-caps").classes(
                            "mt-2 rounded-full px-3 py-1 text-white text-sm bg-teal-600"
                        )

            # RIGHT COLUMN
            with ui.column().classes("w-full lg:w-1/3 flex flex-col gap-6"):
                with ui.card().style("background-color:#ade6e5ff;").classes(
                    "w-full p-4 rounded-3xl shadow-xl"
                ):
                    ui.label("Share the Impact!").classes("font-semibold text-lg mb-2")
                    with ui.row().classes("gap-4 justify-center"):
                        ui.button(icon="facebook", color="blue").props("flat round")
                        ui.button(icon="twitter", color="skyblue").props("flat round")
                        ui.button(icon="instagram", color="pink").props("flat round")

                with ui.card().style("background-color:#ade6e5ff;").classes(
                    "w-full p-4 rounded-3xl shadow-xl"
                ):
                    ui.label("Top Warriors This Week").classes(
                        "font-semibold text-lg mb-3"
                    )
                    with ui.column().classes("gap-3"):
                        with ui.row().classes("items-center gap-3"):
                            ui.label("1").classes("font-bold text-green-600")
                            ui.avatar(
                                "https://randomuser.me/api/portraits/women/20.jpg"
                            )
                            ui.label("Jane D. — 1,250 Impact").classes("text-sm")
                        with ui.row().classes("items-center gap-3"):
                            ui.label("2").classes("font-bold text-gray-700")
                            ui.avatar("https://randomuser.me/api/portraits/men/32.jpg")
                            ui.label("John A. — 980 Impact").classes("text-sm")
                        with ui.row().classes("items-center gap-3"):
                            ui.label("3").classes("font-bold text-orange-600")
                            ui.avatar("https://randomuser.me/api/portraits/men/40.jpg")
                            ui.label("Mike T. — 760 Impact").classes("text-sm")

    #  FOOTER
    with ui.footer().classes(
        "w-full bg-teal-100 text-center justify-center py-6 mt-10"
    ):
        ui.label(
            "© 2025 Tankas App. Let’s make our community cleaner, together."
        ).classes("text-sm text-gray-600")
        ui.label("Report an Issue  •  Share on Social").classes(
            "text-xs text-gray-500 mt-1"
        )
