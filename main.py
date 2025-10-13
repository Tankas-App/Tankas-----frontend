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

app.add_static_files("/assets", "assets")

ui.run(title="TankasApp", storage_secret="qrackhydrarionsydnorhannah")
