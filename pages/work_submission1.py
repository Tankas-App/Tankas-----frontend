from nicegui import ui


    # Tailwind custom colors (inline style overrides)
MINT_CREAM = '#F7FFF7'
TEAL = '#007F7C'
LIGHT_TEAL = '#ade6e5ff'
BLUE = '#2E86AB'
NIGHT = '#0A0A0A'
GOLD = '#f8d50eff'


@ui.page('/work_submission1')
def show_work_submission1():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    ui.query('.nicegui-row').classes('flex-nowrap')

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

    with ui.column().classes('w-full justify-center items-center mt-10 px-10 py-20 space-y-6'):
        ui.label('Submit Your Work').classes(f'text-[{BLUE}] font-bold text-3xl')

        # STEPS
        with ui.row().classes('w-full justify-center space-x-8 mt-4'):
            with ui.column().classes('items-center'):
                ui.label('1').classes(f'step-active rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold')
                ui.label('Upload Photos').classes('text-sm text-gray-600')
            ui.separator().props('vertical=false').classes('w-10 bg-gray-300 h-0.5 mt-5')
            with ui.column().classes('items-center'):
                ui.label('2').classes(f'step-inactive rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold')
                ui.label('Add Details').classes('text-sm text-gray-600')
            ui.separator().props('vertical=false').classes('w-10 bg-gray-300 h-0.5 mt-5')
            with ui.column().classes('items-center'):
                ui.label('3').classes(f'step-inactive rounded-full w-10 h-10 flex items-center justify-center text-lg font-semibold')
                ui.label('Review & Submit').classes('text-sm text-gray-600')

        # PHOTO UPLOAD SECTION
        with ui.row().classes('w-[50%] justify-between mt-8 w-full'):
            with ui.column().classes('w-1/2 space-y-2 justify-center items-center'):
                ui.label('Before').classes(f'text-[{NIGHT}] font-semibold text-lg')
                ui.image('https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=600&q=80')\
                        .classes('object-cover w-full h-full')
                    
            with ui.column().classes('w-1/2 space-y-2 justify-center items-center'):
                    ui.label('After').classes(f'text-[{NIGHT}] font-semibold text-lg')
                    with ui.card().classes('border-2 border-dashed border-gray-300 rounded-lg p-8 text-center hover:border-gray-500 transition'):
                        ui.label("Drag your 'before' photo here, or click to browse.").classes('text-gray-600 text-sm mb-2')
                        ui.button('Browse').props('flat').classes(f'bg-gray-100 text-{NIGHT} px-4 py-2 rounded-lg')

        # FOOTER BUTTONS
        with ui.row().classes('justify-between mt-8 w-[50%]'):
            ui.button('Cancel', on_click=lambda: ui.navigate.back()).props('flat dense no-caps').classes('text-lg font-semibold px-10 py-2 rounded-lg').style('background-color: #ade6e5ff;')
            ui.button('Next', ).props('flat dense no-caps').classes('text-white text-lg font-semibold px-10 py-2 rounded-lg').style('background-color: #007F7C')