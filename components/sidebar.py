from nicegui import ui

def show_sidebar():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    # Sidebar container
    with ui.column().classes('w-full h-screen z-50 flex justify-between items-center').style('background-color: #F7FFF7'):
        
        # Navigation menu
        with ui.column().classes('gap-1 w-full justify-center items-center'):
            # Logo/Brand section
            with ui.row().classes('items-center px-4'):
                ui.label('TankasApp').classes('text-xl font-bold text-teal-600 dark:text-blue-400 py-4')
            ui.button('Dashboard', 
                     on_click=lambda: ui.navigate.to('/dashboard'), icon='grid_view').classes('w-full text-balck py-3 px-4 hover:text-lg').props("flat dense no-caps")
            ui.button('Issue Feed', 
                     on_click=lambda: ui.navigate.to('/issues'), icon='list').classes('w-full text-balck py-3 px-4 hover:text-lg').props("flat dense no-caps")
            
            ui.button('Post Issue', 
                     on_click=lambda: ui.navigate.to('/post_issue')).classes('w-full text-balck py-3 px-4 hover:text-lg').props("flat dense no-caps")
            
            ui.button('Warriors', 
                     on_click=lambda: ui.navigate.to('/warrior')).classes('w-full text-balck py-3 px-4 hover:text-lg').props("flat dense no-caps")
            
            ui.button('Leaderboard', 
                     on_click=lambda: ui.navigate.to('/rewards'), icon='leaderboard').classes('w-full text-balck py-3 px-4 hover:text-lg').props("flat dense no-caps")
            
            ui.button('Suggest Reward', 
                     on_click=lambda: ui.navigate.to('/suggest_reward'), icon='emoji_events').classes('w-full text-balck py-3 px-4 hover:text-lg').props("flat dense no-caps")
        
        # User profile section at bottom
        with ui.column().classes('w-full py-2 px-4'):
            with ui.row().classes('items-center gap-1'):
                ui.avatar('U').classes(' text-white').props('color=teal-7')
                 
                # User info
                with ui.column().classes('gap-1'):
                    ui.label('User Name').classes('font-medium text-gray-900 dark:text-gray-100')
                    ui.label('user@email.com').classes('text-sm text-gray-500 dark:text-gray-400')
            
            # Sign out button
            ui.button('Sign Out', 
                     on_click=lambda: ui.navigate.to('/signin')).classes('w-full py-3').props("flat dense no-caps").style('background-color: #ade6e5ff; border: none;')
            