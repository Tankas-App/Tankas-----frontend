from nicegui import ui

@ui.page('/issue_detail')
def show_issue_detail():
    ui.label("The details of this issue")