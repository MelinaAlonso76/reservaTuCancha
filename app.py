import flet as ft

def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "white"
    
    #HEADER
    header = ft.Container(
                height=220,
                width=float("inf"),
                content=ft.Image(
                    src="imgcabecera.jpeg",
                    fit="cover",
                    width=float("inf")
                ),
            )

    #UBICACION
    location_section=ft.Container(
        padding=15,
        content=ft.Column(
            spacing=5,
            controls=[
                ft.Text(
                    "Complejo Zamudio",
                    size=36,
                    weight=ft.FontWeight.BOLD,
                    color = ft.Colors.BLACK,
                ),
                ft.Text(
                    "📍General Bartolome Mitre 765",
                    size=20,
                    color = ft.Colors.BLACK,
                    weight=ft.FontWeight.NORMAL,
                ),
            ],
        ),
    )

    #PESTAÑA CON BOTONES #RESERVAR E #INFORMACION
    #CONTENIDO RESERVAR
    reservar_view = ft.Column(
        visible=True,
        controls=[
            ft.Text(
                "Amigo reservaaaa",
                size=20,
                weight=ft.FontWeight.BOLD,
            )
        ],
    )

    #CONTENIDO INFO
    info_view = ft.Column(
        visible=False,
        controls=[
            ft.Text(
                "Lee antes de reservar papuuu",
                size=20,
                weight=ft.FontWeight.BOLD,
            )
        ],
    )

    #FUNCIONES BOTONES
    def show_reservar(e):
        reservar_view.visible=True
        info_view.visible=False
        page.update()

    def show_info(e):
        reservar_view.visible=False
        info_view.visible=True
        page.update()

    #BOTONES
    botones = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton("RESERVAR",on_click=show_reservar),
            ft.ElevatedButton("INFO GENERAL",on_click=show_info),
        ],
    )

    page.add(
        ft.Column(
            spacing=0,
            controls=[
                header,
                location_section,
                botones,
                reservar_view,
                info_view,
            ],
        )
    )

ft.app(target=main, assets_dir="assets")