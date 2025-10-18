from nicegui import ui
import requests
from utils.api import base_url


@ui.page("/issue_detail")
def show_issue_detail():
    ui.query(".nicegui-row").classes("flex-nowrap")
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )
    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">'
    )

    issue = None

    issue_id = ui.context.client.request.query_params.get("id")
    try:
        response = requests.get(url=f"{base_url}/api/issues/{issue_id}")
        # print(response.st atus_code, response.content)
        if response.status_code == 200:
            json_data = response.json()
            print(json_data)
            issue = json_data

        else:
                # Add a visual notification if the API call fails
                ui.notify(f'Error fetching issue: {response.status_code}', type='negative')

    except requests.exceptions.RequestException as e:
        ui.notify(f'Network error: {e}', type='negative')

    with ui.element().classes(
        "w-full h-full flex flex-col justify-center items-center rounded py-20"
    ).style('font-family: "Raleway", serif; background-color:#F7FFF7;'):
        # ui.label("Issue details").classes("text-2xl")
        # with ui.card().classes(
        #     "w-[50%] h-full flex flex-col justify-center items-center rounded-2xl"
        # ):
        if issue:
            with ui.element("div").classes(
                f"w-[70%] h-96 flex flex-col  items-center bg-[url({issue["picture_url"]})] bg-cover bg-center rounded-xl"
            ):
                with ui.element('div').classes('w-full p-2'):
                    ui.button("Back", on_click=lambda: ui.navigate.back()).props(
                        "flat dense no-caps"
                    ).classes('bg-gray-700 text-white text-sm font-semibold px-4')
                # ui.image("/assets/litter.png").classes(
                #     "w-full h-full object-cover rounded"
                # )
            with ui.element("div").classes("w-[70%] h-[50%] flex flex-col px-5 py-10"):
                with ui.column():
                    ui.label(text=issue["title"]).classes("text-3xl  mt-4 font-bold").style(
                        "color: #2E86AB"
                    )
                    ui.label(text=issue["description"]).classes("text-lg")
                    ui.label(text=issue["difficulty"]).classes("text-lg font-semibold")
                    ui.label(text=issue["priority"]).classes("text-lg font-semibold ")
                with ui.row().classes(
                    "w-full flex flex-row justify-between items-center py-5 mt-8"
                ):
                    ui.button("Volunteer").props("flat dense no-caps").classes(
                        "w-[50%] font-semibold text-white text-lg rounded-xl py-3"
                    ).style("background-color:#007F7C")
                    ui.button("Submit Fix", on_click=lambda: ui.navigate.to('/work_submission1')).props("flat dense no-caps").classes(
                        "w-[50%] font-semibold text-lg rounded-xl py-3"
                    ).style("background-color:#ade6e5ff; color: #2E86AB")

        else:
            # 4. Fallback UI if the issue data failed to load
            ui.label("Issue details could not be loaded.").classes("text-xl text-red-600")
