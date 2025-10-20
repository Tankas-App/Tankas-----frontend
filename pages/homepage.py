from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page('/')
def homepage():
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')
    
    show_navbar()

    with ui.element('main').classes('w-full h-screen flex flex-col justify-center items-center bg-[url("/assets/wom.jpg")] bg-cover bg-center').classes('').style('font-family: "Raleway", serif; color: #2E86AB'):
        with ui.element('div').classes('text-white bg-black/50 w-full h-full flex flex-col justify-center items-center'):
            ui.label("Clean Together, Thrive Together").style('font-family: "Archivo Black", sans-serif;').classes('text-6xl mb-8')
            ui.label("Join Tankas, the gamified sanitation app that turns community improvement into a fun, rewarding adventure. Earn points, badges, and recognition for making your neighborhood cleaner and greener.").classes('w-[40%] text-lg text-gray-300 mb-8')
            ui.button(text="Get Started", on_click=lambda: ui.navigate.to('/tutorial1')).props('flat dense no-caps').classes('text-white px-12 py-3 rounded-lg shadow-sm font-bold text-lg').style('background-color: #007F7C')

    # HOW IT WORKS
    with ui.element('section').classes('w-full justify-center items-center py-20 text-center px-6').style('font-family: "Raleway", serif; background-color:#F7FFF7;').props('id="about"'):
        ui.label('HOW IT WORKS').classes('text-teal font-bold text-lg mb-2')
        ui.label('Tankas makes cleanup engaging').classes('font-bold text-3xl mb-3')
        ui.label('Here’s how you can get involved and make a real difference in your community.').classes('text-gray-500 text-lg max-w-2xl mx-auto mb-10')

        with ui.element('div').classes('grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto'):
            def card(title, desc, icon):
                with ui.element('div').classes('bg-white p-6 rounded-lg shadow hover:shadow-lg transition text-center'):
                    ui.icon(icon).classes('text-teal text-3xl mb-3')
                    ui.label(title).classes('font-semibold text-night mb-2')
                    ui.label(desc).classes('text-night text-sm opacity-80')
            card('Join Challenges', 'Participate in local cleanup events. Earn points and badges for your contributions.', 'emoji_events')
            card('Connect with Neighbors', 'Collaborate with fellow community members, share tips, and celebrate achievements together.', 'groups')
            card('Improve Your Community', 'Make a tangible difference in your neighborhood’s cleanliness and well-being.', 'place')


    # FEATURES
    with ui.element('section').classes('w-full justify-center items-center bg-white py-20 text-center px-6').style('font-family: "Raleway", serif;').props('id="features"'):
        ui.label('FEATURES').classes('text-teal font-bold text-lg mb-2')
        ui.label('Everything you need to get involved').classes('font-bold text-3xl mb-3')
        ui.label('Tankas offers a range of features designed to make community improvement fun and effective.').classes('text-lg text-gray-500 max-w-2xl mx-auto mb-10')

        with ui.element('div').classes('grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto'):
            def feature_card(img, title, desc):
                with ui.element('div').classes('bg-mint rounded-lg overflow-hidden shadow hover:shadow-lg transition'):
                    ui.image(img).classes('w-full h-48 object-cover')
                    with ui.element('div').classes('p-5 text-left'):
                        ui.label(title).classes('text-night font-semibold mb-2')
                        ui.label(desc).classes('text-night text-sm opacity-80')
            feature_card('/assets/bg1.png',
                        'Gamified Challenges',
                        'Earn points, badges, and climb leaderboards by participating in cleanup events and completing tasks.')
            feature_card('/assets/bg2.png',
                        'Community Engagement',
                        'Connect with neighbors, share your progress, and collaborate on community projects.')
            feature_card('/assets/bg3.png',
                        'Progress Tracking',
                        'Track your contributions, see the impact of your efforts, and celebrate collective achievements.')


    # CTA SECTION
    with ui.element('section').classes('w-full py-16 text-center').style('font-family: "Raleway", serif; background-color:#F7FFF7;'):
        ui.label('Ready to Make a Difference?').classes('text-black font-bold text-2xl mb-3')
        ui.label('Download Tankas now and start your journey towards a cleaner, more vibrant community.').classes('text-lg mb-6 text-gray-600')
        ui.button('Join Tankas Today', on_click=lambda: ui.navigate.to('/signup')).classes('bg-teal text-white px-6 py-3 rounded-full font-semibold text-lg hover:opacity-90').props('flat dense no-caps')
 

    show_footer()