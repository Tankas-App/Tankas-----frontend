from nicegui import ui

def show_footer():
    ui.add_head_html(
        "<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>"
    )
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Raleway:ital,wght@0,100..900;1,100..900&family=Stoke:wght@300;400&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">')

    with ui.element('footer').classes('w-full bg-white py-6 border-t text-night px-15 text-lg mt-10 justify-center items-center').style('font-family: "Raleway", serif; color: #2E86AB'):
        with ui.element('div').classes('w-full flex flex-col md:flex-row justify-between items-center  space-y-4'):
            with ui.element('div').classes('flex space-x-6 text-sm'):
                for item in ['About', 'Contact', 'Privacy Policy', 'Terms of Service']:
                    ui.link(item, '#').classes('no-underline text-gray-600')
            
            with ui.element('div').classes('flex space-x-4 text-gray-600'):
                ui.html('<i class="fa-brands fa-facebook"></i>', sanitize=False).classes('text-xl  cursor-pointer')
                ui.html('<i class="fa-brands fa-x-twitter"></i>', sanitize=False).classes('text-xl  cursor-pointer')
                ui.html('<i class="fa-brands fa-instagram"></i>', sanitize=False).classes('text-xl  cursor-pointer')
                ui.html('<i class="fa-brands fa-whatsapp"></i>', sanitize=False).classes('text-xl  cursor-pointer')
            
        with ui.element('div').classes('w-full flex justify-center items-center mt-4'):
            ui.label('© 2025 Tankas. All rights reserved.').classes('text-sm text-gray-500')