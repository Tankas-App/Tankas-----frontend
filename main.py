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

app.add_static_files("/assets", "assets")

ui.run(title="TankasApp", storage_secret="qrackhydrarionsydnorhannah")
