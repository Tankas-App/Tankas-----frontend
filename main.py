from nicegui import ui, app
from pages.homepage import *
from pages.dashboard import *
from pages.signin import *
from pages.signup import *
from pages.issues import *
from pages.issue_detail import *
from pages.issue_confirmation import *
from pages.warrior import *
from pages.post_issue import *
from pages.tutorial1 import *
from pages.tutorial2 import *
from pages.tutorial3 import *
from pages.tutorial4 import *
from pages.suggest_reward import *
from pages.update_issue import *

app.add_static_files("/assets", "assets")

# Test page with sidebar
# @ui.page('/sidebar_test')
# def sidebar_test_page():
#     with ui.row().classes('w-full h-screen'):
#         show_sidebar()
#         with ui.column().classes('flex-1 p-8'):
#             ui.label('Main Content Area').classes('text-3xl font-bold mb-4')
#             ui.label('This is a test page showing the sidebar in action.').classes('text-gray-600')

ui.run(title="TankasApp", storage_secret="qrackhydrarionsydnorhannah")
