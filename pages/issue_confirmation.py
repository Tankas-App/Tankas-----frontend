from nicegui import ui

@ui.page('/issue_confirmation')
def show_issue_confirmation():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')
    
    with ui.column().classes('w-full h-screen items-center justify-center gap-8').style('font-family: "Raleway", serif;'):
        with ui.card().classes('w-[50%] justify-center items-center px-10 py-10'):
            ui.image('/assets/check_1.png').classes('w-[10%] mb-8')
            ui.label('Thank you for your report!').classes('text-4xl font-bold text-green-600 text-center').style('color: #2E86AB;')
            
            ui.label('Your issue has been successfully submitted and will be reviewed by our team.').classes('text-lg text-gray-600 text-center max-w-md')
            
            with ui.column().classes('flex gap-4 mt-8 w-full px-20'):
                # View my report button
                ui.button('View My Reports', 
                        on_click=lambda: ui.navigate.to('/issue_detail')).classes('text-white px-6 py-3 rounded-lg w-full font-bold').props('flat dense no-caps').style('background-color: #007F7C')
                
                # Back to issue feed button
                ui.button('Back to Issue Feed', 
                        on_click=lambda: ui.navigate.to('/issues')).classes("px-6 py-3 rounded-lg w-full font-bold").props('flat dense no-caps').style('background-color: #ade6e5ff; color: #007F7C;')