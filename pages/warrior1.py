from nicegui import ui


@ui.page("/warrior1")
def main_page():
    ui.query("nicegui-content").classes("p-0 m-0 gap-0")
    with ui.element().classes(
        "w-full min-h-screen bg-[#F7FFF7] flex flex-col items-center justify-start py-10"
    ):

        # ====== WARRIOR OF THE WEEK ======
        with ui.card().classes(
            "w-[80%] mx-auto bg-green-50 rounded-2xl p-6 flex flex-col md:flex-row items-center justify-between"
        ):
            with ui.row().classes("items-center gap-6"):
                ui.avatar("https://randomuser.me/api/portraits/women/20.jpg").classes(
                    "w-35 h-35"
                )
                with ui.column():
                    ui.label("🏅 Warrior of the Week").classes(
                        "text-green-700 text-2xl font-large"
                    )
                    ui.label("Jane D.").classes("text-2xl font-bold")
                    ui.label(
                        "For her outstanding contribution to the Park Cleanup at Sunrise, achieving 1,250 impact points!"
                    ).classes("text-gray-600 text-sm max-w-xl")
            with ui.row().classes("gap-4 mt-4 md:mt-0"):
                ui.button("Send Kudos", color="teal-600").classes("rounded-full px-4")
                ui.button("View Profile", color="teal-600").classes("rounded-full px-4")

        # ====== DATA ======
        issues = [
            {
                "title": "Park Cleanup at Sunrise",
                "status": "In Progress",
                "details": "75% Complete",
                "user": "Jane D.",
                "image": "https://images.unsplash.com/photo-1508873696983-2dfd5898f375?w=400",
                "user_image": "https://randomuser.me/api/portraits/women/20.jpg",
            },
            {
                "title": "Riverbank Restoration",
                "status": "Completed",
                "details": "150 lbs collected",
                "user": "John A.",
                "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=400",
                "user_image": "https://randomuser.me/api/portraits/men/32.jpg",
            },
            {
                "title": "Coastal Cleanup Drive",
                "status": "Completed",
                "details": "300 lbs collected",
                "user": "Mike T.",
                "image": "https://images.unsplash.com/photo-1534683979012-9f9a0f0c4d09?w=400",
                "user_image": "https://randomuser.me/api/portraits/men/45.jpg",
            },
        ]

        # ====== COMMUNITY IN ACTION ======
        with ui.element().classes("w-[80%] mx-auto p-8 "):
            with ui.row():
                with ui.column().classes("gap-1"):
                    ui.label("Community in Action").classes(
                        "text-2xl font-bold text-gray-900 mt-10 text-end"
                    )
                    ui.label(
                        "See the incredible impact our warriors are making together!"
                    ).classes("text-green-600 text-md text-center")

            current_filter = "All"

        def set_filter(value):
            nonlocal current_filter
            current_filter = value
            render_cards.refresh()

        @ui.refreshable
        def render_cards():
            with ui.row().classes("gap-3 justify-items-end items-end mb-4"):
                for label in ["All", "In Progress", "Completed"]:
                    active = (
                        "text-white" if label == current_filter else "text-gray-700"
                    )
                    ui.button(label, on_click=lambda l=label: set_filter(l)).classes(
                        f"rounded-full px-4 py-1 border border-gray-300 {active}"
                    )

            with ui.row().classes("flex-wrap justify-center w-[80%] mx-auto mb-10"):
                for issue in issues:
                    if current_filter != "All" and issue["status"] != current_filter:
                        continue
                    with ui.card().classes(
                        "flex flex-col bg-white shadow-sm rounded-2xl p-4 w-full md:w-[30%]"
                    ):
                        ui.image(issue["image"]).classes(
                            "w-full h-40 object-cover rounded-xl"
                        )
                        with ui.column().classes("mt-3"):
                            ui.label(issue["title"]).classes("text-md font-semibold")
                            ui.label(issue["status"]).classes(
                                f"text-sm text-{'green' if issue['status']=='In Progress' else 'blue'}-600"
                            )
                            ui.label(issue["details"]).classes("text-xs text-gray-600")
                        with ui.row().classes("items-center gap-2 mt-2"):
                            ui.avatar(issue["user_image"])
                            ui.label(issue["user"]).classes("text-sm")
                            ui.button("Kudos", color="teal-600").classes(
                                "mt-2 rounded-full px-3 py-1 text-sm self-start"
                            )

        render_cards()

        # ====== BEFORE & AFTER SECTION ======
        with ui.card().classes("w-[80%] mx-auto bg-white rounded-2xl p-6 mb-10"):
            ui.label("Before & After: Community Trail").classes(
                "text-lg font-semibold mb-4"
            )
            with ui.element().classes("flex no-wrap"):
                with ui.row().classes("justify-between gap-4"):
                    with ui.column().classes("w-[50%] md:w-[48%]"):
                        ui.label("Before").classes(
                            "text-sm font-semibold text-gray-500 mb-2"
                        )
                        ui.image(
                            "https://images.unsplash.com/photo-1597262975002-c5c3b14bbd62?w=800"
                        ).classes("w-2/3 h-60 object-cover rounded-xl")
                with ui.row().classes("w-full md:w-[48%]"):
                    ui.label("After").classes(
                        "text-sm font-semibold text-gray-500 mb-2"
                    )
                    ui.image(
                        "https://images.unsplash.com/photo-1593642634367-d91a135587b5?w=800"
                    ).classes("w-full h-60 object-cover rounded-xl")

        # ====== FOOTER ======

    with ui.footer().classes("w-full bg-gray-100 text-center py-6 mt-10"):
        ui.label(
            "© 2025 Tankas App. Let’s make our community cleaner, together."
        ).classes("text-sm text-gray-600")
        ui.label("Report an Issue  •  Share on Social").classes(
            "text-xs text-gray-500 mt-1"
        )
