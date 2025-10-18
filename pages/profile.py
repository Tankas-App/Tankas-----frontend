from nicegui import ui
@ui.page('/profile')
def show_profile():
    # Main container with mint cream background
    with ui.column().classes('w-full min-h-screen p-8').style('background-color: #007F7C'):
        
        # Header section
        with ui.card().classes('w-full max-w-4xl mx-auto p-8 mb-6').style('background-color: #007F7C'):
            with ui.row().classes('w-full items-center justify-between'):
                # User info section
                with ui.row().classes('items-center gap-6'):
                    # Profile avatar
                    ui.avatar('SE').classes('w-24 h-24 text-white text-2xl').style('background-color: #007F7C')
                    
                    # User details
                    with ui.column().classes('gap-2'):
                        ui.label('Sydnor Elikem').classes('text-3xl font-bold text-black')
                        ui.label('Level 5').classes('text-lg font-semibold').style('color: #007F7C')
                        ui.label('Joined 2 months ago').classes('text-gray-600')
                        # Progress bar
                        with ui.column().classes('w-80'):
                            ui.linear_progress(value=0.75).classes('h-2').style('color: #007F7C')
                            ui.label('750/1000 points to Level 6').classes('text-sm text-gray-500')
                
                # Edit profile button
                ui.button('Edit Profile', on_click=lambda: ui.notify('Edit profile clicked')).props("flat dense no-caps").classes('px-6 py-3 rounded-lg text-white').style('background-color: #007F7C')
        
        # Stats cards
        # with ui.row().classes('w-full max-w-4xl mx-auto gap-6 mb-8'):
        #     with ui.card().classes('flex-1 p-6 text-center'):
        #         ui.label('1200').classes('text-4xl font-bold').style('color: #007F7C')
        #         ui.label('Total Points').classes('text-gray-600')
            
        #     with ui.card().classes('flex-1 p-6 text-center'):
        #         ui.label('35').classes('text-4xl font-bold').style('color: #007F7C')
        #         ui.label('Tasks Completed').classes('text-gray-600')
            
        #     with ui.card().classes('flex-1 p-6 text-center'):
        #         ui.label('15').classes('text-4xl font-bold').style('color: #007F7C')
        #         ui.label('Badges Earned').classes('text-gray-600')
        
        # Content area
        with ui.row().classes('w-full max-w-4xl mx-auto gap-6'):
            # Left column
            with ui.column().classes('flex-1'):
                with ui.card().classes('w-full p-6'):
                    ui.label('Reported Issues Status').classes('text-xl font-bold mb-4')
                    
                    with ui.column().classes('gap-4'):
                        # Pending issue
                        with ui.row().classes('w-full items-center p-4 rounded-lg bg-yellow-50'):
                            ui.icon('warning', color='orange').classes('text-2xl')
                            with ui.column().classes('flex-1 ml-4'):
                                ui.label('Broken Streetlight on Elm St.').classes('font-medium')
                                ui.label('Reported on 2023-10-25').classes('text-sm text-gray-500')
                            ui.chip('Pending', color='orange')
                        
                        # In Progress issue
                        with ui.row().classes('w-full items-center p-4 rounded-lg bg-blue-50'):
                            ui.icon('build', color='blue').classes('text-2xl')
                            with ui.column().classes('flex-1 ml-4'):
                                ui.label('Pothole on Main Ave').classes('font-medium')
                                ui.label('Reported on 2023-10-22').classes('text-sm text-gray-500')
                            ui.chip('In Progress', color='blue')
                        
                        # Completed issue
                        with ui.row().classes('w-full items-center p-4 rounded-lg bg-green-50'):
                            ui.icon('check_circle', color='green').classes('text-2xl')
                            with ui.column().classes('flex-1 ml-4'):
                                ui.label('Graffiti on Park Wall').classes('font-medium')
                                ui.label('Reported on 2023-10-18').classes('text-sm text-gray-500')
                            ui.chip('Completed', color='green')
            
            # Right column
            with ui.column().classes('w-80'):
                with ui.card().classes('w-full p-6'):
                    ui.label('Badges').classes('text-xl font-bold mb-4')
                    
                    with ui.column().classes('gap-4'):
                        with ui.column().classes('items-center p-4 rounded-lg bg-gray-50'):
                            ui.icon('eco', color='green').classes('text-4xl')
                            ui.label('Eco Warrior').classes('font-medium text-center')
                        
                        with ui.column().classes('items-center p-4 rounded-lg bg-gray-50'):
                            ui.icon('people', color='blue').classes('text-4xl')
                            ui.label('Community Hero').classes('font-medium text-center')
                        
                        with ui.column().classes('items-center p-4 rounded-lg bg-gray-50'):
                            ui.icon('star', color='gold').classes('text-4xl')
                            ui.label('Cleanliness Champion').classes('font-medium text-center')