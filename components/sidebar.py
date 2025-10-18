from nicegui import ui

def show_sidebar():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    # Sidebar container
    with ui.column().classes('w-full h-screen z-50').style('background-color: #F7FFF7'):
        # Logo/Brand section
        with ui.row().classes('items-center mb-8'):
            ui.label('TankasApp').classes('text-2xl font-bold text-teal-600 dark:text-blue-400')
        
        # Navigation menu
        with ui.column().classes('gap-1 w-full'):
            ui.button('Dashboard', 
                     on_click=lambda: ui.navigate.to('/dashboard')).classes('w-full text-white py-3 px-4').style('background-color: #007F7C; border: none;').props("flat dense no-caps")
            ui.button('Issues', 
                     on_click=lambda: ui.navigate.to('/issues')).classes('w-full text-white py-3 px-4').style('background-color: #007F7C; border: none;').props("flat dense no-caps")
            
            ui.button('Post Issue', 
                     on_click=lambda: ui.navigate.to('/post_issue')).classes('w-full text-white py-3 px-4').style('background-color: #007F7C; border: none;').props("flat dense no-caps")
            
            ui.button('Warriors', 
                     on_click=lambda: ui.navigate.to('/warrior')).classes('w-full text-white py-3 px-4').style('background-color: #007F7C; border: none;').props("flat dense no-caps")
            
            ui.button('Tutorials', 
                     on_click=lambda: ui.navigate.to('/tutorial1')).classes('w-full text-white py-3 px-4').style('background-color: #007F7C; border: none;').props("flat dense no-caps")
            
            ui.button('Suggest Reward', 
                     on_click=lambda: ui.navigate.to('/suggest_reward')).classes('w-full text-white py-3 px-4').style('background-color: #007F7C; border: none;').props("flat dense no-caps")
            
            ui.button('Profile', 
                     on_click=lambda: ui.navigate.to('/profile')).classes('w-full text-white py-3 px-4').style('background-color: #007F7C; border: none;').props("flat dense no-caps")
        
        # User profile section at bottom
        with ui.column().classes('w-full mt-8'):
            with ui.row().classes('items-center space-x-3 cursor-pointer p-2 rounded-lg hover:bg-gray-200').on('click', lambda: ui.navigate.to('/profile')):
                ui.avatar('SC').classes('text-white').style('background-color: #007F7C')
                 
                # User info
                with ui.column().classes('flex-1'):
                    ui.label('Sophia Clark').classes('font-medium text-gray-900')
                    ui.label('Level 5 • 1200 pts').classes('text-sm').style('color: #007F7C')
            
            # Sign out button
            ui.button('Sign Out', 
                     on_click=lambda: ui.navigate.to('/signin')).classes('w-full mt-3 py-3').props("flat dense no-caps").style('background-color: #ade6e5ff; border: none;')
            