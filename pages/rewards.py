from nicegui import ui

@ui.page('/rewards')
def show_rewards():
    ui.query(".nicegui-row").classes("flex-nowrap")
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )
    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">'
    )

    with ui.element('main').classes('w-full h-full').style('font-family: "Raleway", serif; background-color:#F7FFF7;'):
        # Top Navigation Bar
        with ui.element('header').classes('w-full flex justify-between items-center px-8 py-4 bg-white shadow-sm fixed top-0 left-0 z-50'):
            with ui.row().classes('items-center gap-2'):
                ui.image('https://img.icons8.com/ios-filled/50/recycle.png').classes('w-8 h-8')
                ui.label('TankasApp').classes('text-sm font-semibold')
            with ui.row().classes('gap-8  md:flex'):
                ui.link('Dashboard', '/dashboard').classes('text-gray-600 hover:text-black no-underline')
                ui.link('Leaderboard', '#').classes('text-yellow-500 font-semibold no-underline')
                ui.link('Rewards', '#').classes('text-gray-600 hover:text-black no-underline')
                ui.link('Profile', '#').classes('text-gray-600 hover:text-black no-underline')
            with ui.row().classes('gap-4 items-center'):
                ui.icon('notifications_none').classes('text-gray-600 text-xl')
                ui.avatar().props('size=40 color=teal-7').classes('border border-gray-300')

        # Title & Subtitle
        with ui.column().classes('w-full items-center mt-10 mb-10 py-20'):
            with ui.row().classes('gap-2'):
                ui.label('Leaderboard').classes('text-3xl font-bold')
                ui.label('&').classes('text-3xl font-bold')
                ui.label('Rewards').classes('text-3xl font-bold text-yellow-500')
            ui.label('Top volunteers and their accumulated points. Keep up the great work!').classes('text-gray-500 text-center text-lg')

        # Main Section
        with ui.row().classes('w-full max-w-6xl mx-auto mt-6 gap-8 flex flex-col md:flex-row'):
            # Leaderboard
            with ui.column().classes('flex-1'):
                ui.label('Top Volunteers').classes('text-xl font-bold mt-4')
                with ui.card().classes('w-full shadow-sm rounded-lg p-0 overflow-hidden'):
                    with ui.row().classes('w-full flex flex-row justify-between items-center px-6 py-3 bg-gray-50 font-semibold text-gray-600'):
                        ui.label('Rank').classes('')
                        ui.label('Volunteer').classes('')
                        ui.label('Points').classes('')
                    volunteers = [
                        (1, 'Sydnor Afrifa', 'https://randomuser.me/api/portraits/women/44.jpg', 1500),
                        (2, 'Hannah Bonsrah', 'https://randomuser.me/api/portraits/men/41.jpg', 1450),
                        (3, 'Bismark Kasongo', 'https://randomuser.me/api/portraits/women/21.jpg', 1400),
                        (4, 'Marion Nkrumah', 'https://randomuser.me/api/portraits/men/25.jpg', 1350),
                        (5, 'Kofi Takyi', 'https://randomuser.me/api/portraits/women/30.jpg', 1300),
                    ]
                    for rank, name, img, pts in volunteers:
                        with ui.row().classes('w-full flex flex-row justify-between items-center px-6 py-3 items-center border-t border-gray-100'):
                            ui.label(str(rank)).classes('')
                            with ui.row().classes('justify-center items-center'):
                                ui.avatar(img).props('size=35 color=teal-7')
                                ui.label(name)
                            ui.label(str(pts)).classes('w-1/4 text-right text-yellow-500 font-semibold')

            # Rewards Section
            with ui.column().classes('w-full md:w-1/3'):
                ui.label('Available Rewards').classes('text-xl font-bold mt-4')
                rewards = [
                    ('Netflix Subscription', '5000 Points'),
                    ('Smart TV', '25000 Points'),
                    ('Vacation Trip', '100000 Points'),
                ]
                for title, pts in rewards:
                    with ui.card().classes('w-full mb-4 p-5 rounded-lg shadow-sm flex flex-col gap-2'):
                        ui.label(title).classes('font-semibold text-lg')
                        ui.label(pts).classes('text-gray-500 text-sm')
                        ui.button('Redeem').classes('bg-yellow-400 text-black font-semibold rounded-lg hover:bg-yellow-500 w-full').props('flat dense no-caps')
