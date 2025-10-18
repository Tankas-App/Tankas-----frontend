from nicegui import ui
from components.sidebar import show_sidebar
import requests
from utils.api import base_url

@ui.page('/dashboard')
def show_dashboard():
    ui.query(".nicegui-row").classes("flex-nowrap")
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    user = None

    user_id = ui.context.client.request.query_params.get("id")
    try:
        response = requests.get(url=f"{base_url}/api/users/dashboard/{user_id}")
        # print(response.status_code, response.content)
        if response.status_code == 200:
            json_data = response.json()
            print(json_data)
            user = json_data

        else:
            # Add a visual notification if the API call fails
            ui.notify(f'Error fetching issue: {response.status_code}', type='negative')

    except requests.exceptions.RequestException as e:
        ui.notify(f'Network error: {e}', type='negative')

    # response = requests.get(url=f"{base_url}/api/users/dashboard")
    # # print(response.status_code, response.content)
    # json_data = response.json()
    # print(f"This is the User Data : {json_data}")
    # user = json_data


    with ui.element("main").classes("w-full flex flex-row justify-between items-center"):
        with ui.row().classes('w-[20%]'):
            show_sidebar()
        
        with ui.column().classes('w-[80%]'):
            if user:
                with ui.element('div').classes('w-full px-5'):
                    with ui.row().classes(''):
                    # Header
                        ui.label(f'Welcome back,').classes('text-3xl font-bold mb-6')
                        ui.label(text=user["username"]).classes('text-3xl font-bold mb-6')

                    # Top Cards
                    with ui.row().classes('gap-6 mb-6 flex flex-col sm:flex-row'):
                        with ui.card().classes('flex-1 p-6 rounded-xl shadow-sm border border-gray-200 bg-white'):
                            ui.label('Reported Issues').classes('text-gray-500')
                            ui.label('5').classes('text-3xl font-bold mt-2')
                        with ui.card().classes('flex-1 p-6 rounded-xl shadow-sm border border-gray-200 bg-white'):
                            ui.label('Current Points').classes('text-gray-500')
                            ui.label(text=user["points"]).classes('text-3xl font-bold mt-2')

                    # Buttons
                    with ui.row().classes('gap-4 mb-8 flex flex-col sm:flex-row'):
                        ui.button('Report a New Issue', on_click=lambda: ui.navigate.to('/post_issue')).classes(
                            'text-white font-semibold rounded-full py-3'
                        ).style('background-color: #007F7C;')
                        ui.button('Volunteer Now').classes(
                            'flex-1 bg-[#E6F3E8] text-gray-700 font-semibold rounded-full py-3 hover:bg-[#DDEFE0]'
                        )

                    # Progress Section
                    with ui.card().classes('p-6 rounded-xl shadow-sm border border-gray-200 bg-white mb-8'):
                        with ui.row().classes('justify-between mb-2'):
                            ui.label('Level 5').classes('font-semibold')
                            ui.label('Next Reward: Eco–Warrior Badge').classes('text-gray-600 text-sm')
                        ui.linear_progress(value=0.45).props('color=green').classes('h-2 rounded-full')
                        ui.label('450 / 1000 XP').classes('text-right text-gray-500 text-sm mt-2')

                    # Recent Activity
                    ui.label('Recent Activity').classes('text-xl font-bold mb-4')
                    activities = [
                        ('You reported a clogged drain on Main Street.', '2 hours ago'),
                        ('You volunteered for the park cleanup event.', '1 day ago'),
                        ("Issue 'Broken Streetlight' was resolved. +50 points!", '3 days ago'),
                    ]
                    for text, time in activities:
                        with ui.card().classes('p-4 mb-3 rounded-xl border border-gray-200 bg-white flex flex-col gap-1'):
                            with ui.row().classes('gap-2 items-center'):
                                ui.icon('info').classes('text-[#00C853]')
                                ui.label(text).classes('text-gray-800')
                            ui.label(time).classes('text-gray-500 text-sm ml-6')
            else:
                # 4. Fallback UI if the issue data failed to load
                ui.label("User details not found.").classes("text-xl text-red-600")