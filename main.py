from nicegui import ui,app
from pages.homepage import *
from pages.signin import *
from pages.signup import *
from pages.profile_simple import *
from components.sidebar import show_sidebar
from components.user_profile import *
from pages.profile import *
from pages.dashboard import *

app.add_static_files("/assets", "assets")

# Simple test page
# @ui.page('/test')
# def test_page():
#     ui.label('Test Page Works!').classes('text-2xl')
#     ui.button('Go to Profile', on_click=lambda: ui.navigate.to('/profile'))

# # Test page with sidebar
# @ui.page('/sidebar_test')
# def sidebar_test_page():
#     with ui.row().classes('w-full h-screen'):
#         show_sidebar()
#         with ui.column().classes('flex-1 p-8'):
#             ui.label('Main Content Area').classes('text-3xl font-bold mb-4')
#             ui.label('This is a test page showing the sidebar in action.').classes('text-gray-600')
#             ui.button('Go to Profile', on_click=lambda: ui.navigate.to('/profile')).classes('mt-4 px-4 py-2 text-white rounded').style('background-color: #007F7C')

ui.run(title="TankasApp", storage_secret="qrackhydrarionsydnorhannah")
