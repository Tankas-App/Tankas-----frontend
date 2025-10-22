from nicegui import ui

@ui.page("/all_volunteers")
def all_volunteers():
    ui.query(".nicegui-content").classes("p-0 m-0 gap-0")
    # Tailwind CDN
    ui.add_head_html('''
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
    ''')

    with ui.element('div').classes('w-full min-h-screen bg-mint p-6 flex justify-center'):
        with ui.element('div').classes('w-full max-w-6xl grid grid-cols-1 lg:grid-cols-2 gap-8'):
            
            # LEFT SIDE — Volunteer Info
            with ui.element('div').classes('flex flex-col space-y-6'):
                ui.label("You're a Volunteer!").classes('text-teal font-bold text-3xl')
                ui.label("You've successfully signed up to help with the 'Clean Up Drive at City Park' issue. Welcome to the team!").classes('text-night')

                # Fellow Volunteers
                with ui.element('div').classes('space-y-2'):
                    ui.label('Your Fellow Volunteers').classes('text-night font-semibold text-lg')
                    with ui.element('div').classes('flex items-center space-x-3'):
                        for i in range(3):
                            ui.image('https://via.placeholder.com/50').classes('w-10 h-10 rounded-full border-2 border-teal')
                    ui.button('Join Group Chat', on_click=lambda: None).classes('bg-teal text-white px-4 py-2 rounded-lg')

                # Task List
                with ui.element('div').classes('space-y-2'):
                    ui.label('Tasks').classes('text-night font-semibold text-lg')
                    
                    def task_item(label, due, members, done=False):
                        with ui.element('div').classes(f'flex justify-between items-center p-3 bg-white rounded-lg shadow-sm border { "opacity-60" if done else ""}'):
                            with ui.element('div').classes('flex items-center space-x-2'):
                                ui.checkbox(value=done).props('color=teal-4')
                                with ui.element('div'):
                                    ui.label(label).classes('text-night font-semibold')
                                    ui.label(f'Due: {due}').classes('text-sm text-night opacity-70')
                            with ui.element('div').classes('flex -space-x-2'):
                                for _ in range(members):
                                    ui.image('https://via.placeholder.com/40').classes('w-8 h-8 rounded-full border-2 border-white')
                    
                    task_item('Distribute flyers in the neighborhood', '25th Oct', 1)
                    task_item('Coordinate with the local waste management', '26th Oct', 3, done=True)
                    task_item('Arrange for garbage bags and gloves', '27th Oct', 1)

                    ui.button('+ Add a Task').classes('bg-lightteal text-teal rounded-lg px-4 py-2 mt-2 font-medium').props('flat dense no-caps')

                # Progress bar
                with ui.element('div').classes('mt-4 space-y-2'):
                    ui.label('Progress').classes('text-night font-semibold text-lg')
                    with ui.element('div').classes('w-full bg-gray-200 rounded-full h-2'):
                        ui.element('div').classes('bg-teal h-2 rounded-full w-1/3')
                    ui.label('1 of 3 tasks completed').classes('text-sm text-night opacity-70')

            # RIGHT SIDE — Schedule
            with ui.element('div').classes('flex flex-col space-y-6'):
                ui.label('Schedule').classes('text-night font-semibold text-lg')

                # Calendar Mockup
                with ui.element('div').classes('bg-white p-4 rounded-xl shadow space-y-4'):
                    ui.label('October 2024').classes('font-semibold text-teal text-center')
                    
                    # Calendar grid (Static)
                    days = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
                    with ui.element('div').classes('grid grid-cols-7 text-center font-medium text-night'):
                        for d in days:
                            ui.label(d)
                    # Just display days (not functional)
                    for row in range(5):
                        with ui.element('div').classes('grid grid-cols-7 text-center'):
                            for col in range(7):
                                day = row*7+col -1
                                if day > 0 and day <= 31:
                                    ui.label(str(day)).classes(
                                        f'py-1 rounded-full hover:bg-lightteal hover:cursor-pointer {"bg-teal text-white" if day==25 else ""}'
                                    )
                                else:
                                    ui.label('')

                # Proposed Times
                with ui.element('div').classes('bg-white rounded-xl shadow p-4 space-y-3'):
                    ui.label('Proposed Times for October 25th').classes('font-semibold text-night')
                    with ui.element('div').classes('flex justify-between items-center border p-3 rounded-lg'):
                        ui.label('9:00 AM - 11:00 AM\n3/5 Volunteers available').classes('text-night')
                        ui.button('Available').classes('bg-teal text-white px-4 py-2 rounded-lg')
                    with ui.element('div').classes('flex justify-between items-center border p-3 rounded-lg'):
                        ui.label('1:00 PM - 3:00 PM\n1/5 Volunteers available').classes('text-night')
                        ui.button('Mark as available').classes('bg-lightteal text-teal px-4 py-2 rounded-lg').props('flat dense no-caps')
                    ui.button('+ Suggest New Time').classes('w-full bg-lightteal text-teal py-2 rounded-lg font-medium').props('flat dense no-caps')
