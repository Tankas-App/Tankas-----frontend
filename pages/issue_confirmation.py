from nicegui import ui

@ui.page('/issue_confirmation')
def show_issue_confirmation():
    with ui.column().classes('w-full h-screen items-center justify-center gap-8'):
        ui.label('Thank you for your report!').classes('text-4xl font-bold text-green-600 text-center')
        
        ui.label('Your issue has been successfully submitted and will be reviewed by our team.').classes('text-lg text-gray-600 text-center max-w-md')
        
        with ui.row().classes('gap-4 mt-8'):
            # View my report button
            ui.button('View My Report', 
                     on_click=lambda: ui.navigate.to('/issue_detail')).classes('bg-blue-500 hover:bg-blue-600 text-white px-6 py-3 rounded-lg')
            
            # Back to issue feed button
            ui.button('Back to Issue Feed', 
                     on_click=lambda: ui.navigate.to('/issues')).classes('bg-gray-500 hover:bg-gray-600 text-white px-6 py-3 rounded-lg')