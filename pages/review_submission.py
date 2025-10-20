from nicegui import ui

# Custom Tailwind classes (in your Tailwind config file, ensure these colors are extended or override Tailwind defaults)
# Tailwind custom colors (inline style overrides)
MINT_CREAM = '#F7FFF7'
TEAL = '#007F7C'
LIGHT_TEAL = '#ade6e5ff'
BLUE = '#2E86AB'
NIGHT = '#0A0A0A'
GOLD = '#f8d50eff'


@ui.page("/review_submission")
def review_submission():
    ui.query("nicegui-content").classes("m-0 p-0 gap-0")

    # Page background
    ui.add_head_html(f"""
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
    """)

    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    with ui.element("div").classes(
        "w-full h-screen justfify-center items-center px-10 py-10"
    ).style('font-family: "Raleway", serif; background-color:#F7FFF7;'):
        with ui.column().classes("w-full justify-center items-center mt-8"):
            # Title
            ui.label("Review Your Submission").classes(
                "text-3xl font-bold text-[#2E86AB] mb-6"
            )
        # STEPS
        with ui.row().classes('w-full justify-center space-x-8 mb-8'):
            with ui.column().classes('items-center'):
                ui.label('1').classes('step-inactive rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold')
                ui.label('Upload Photos').classes('text-sm text-gray-600')
            ui.separator().props('vertical=false').classes('w-10 bg-gray-300 h-0.5 mt-5')
            with ui.column().classes('items-center'):
                ui.label('2').classes('step-inactive rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold')
                ui.label('Add Details').classes('text-sm text-gray-600')
            ui.separator().props('vertical=false').classes('w-10 bg-gray-300 h-0.5 mt-5')
            with ui.column().classes('items-center'):
                ui.label('3').classes('step-active rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold')
                ui.label('Review & Submit').classes('text-sm text-gray-600')

        # Photos Section
        ui.label("Your Photos").classes("text-xl font-semibold text-[#0A0A0A] mb-4")

        with ui.row().classes("grid grid-cols-3 gap-4 mb-8"):
            ui.image(
                "/assets/cleanway.png"
            ).classes("rounded shadow")
            ui.image(
                "/assets/bag.png"
            ).classes("rounded shadow")
            ui.image(
                "/assets/volunteers.png"
            ).classes("rounded shadow")

        # Details Section
        ui.label("Your Details").classes("text-xl font-semibold text-[#0A0A0A] mb-4")

        with ui.card().classes("w-full bg-white rounded-lg shadow p-6 mb-6"):
            with ui.grid(columns=2).classes("gap-4 mb-4"):
                with ui.column():
                    ui.label("Location").classes("text-sm font-medium text-gray-500")
                    ui.label("Greenwood Park, Springfield").classes(
                        "text-base font-semibold"
                    )
                with ui.column():
                    ui.label("Date & Time").classes("text-sm font-medium text-gray-500")
                    ui.label("October 26, 2025, 10:30 AM").classes(
                        "text-base font-semibold"
                    )

            with ui.column():
                ui.label("Work Type").classes("text-sm font-medium text-gray-500")
                ui.label("Litter Picking").classes("text-base font-semibold")

                ui.label("Notes").classes("text-sm font-medium text-gray-500 mt-4")
                ui.label(
                    "Team of 4 volunteers. Focused on the area near the playground. Filled 3 large bags of trash."
                ).classes("text-base")
        with ui.row().classes('w-full justify-around mt-8 px-20 py-10'):
            ui.button('Go Back & Edit', on_click=lambda: ui.navigate.back()).props('flat dense no-caps').classes('text-lg font-semibold px-10 py-2 rounded-lg').style('background-color: #ade6e5ff;')
            ui.button('Confirm & Submit', on_click=lambda: ui.navigate.to('#')).props('flat dense no-caps').classes('text-white text-lg font-semibold px-10 py-2 rounded-lg').style('background-color: #007F7C')
