import flet as ft

def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0

    header = ft.Container(
        width=page.width,        # ocupa todo el ancho
        height=220,              # altura definida
        content=ft.Image(
            src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
            fit=ft.ImageFit.COVER,  # cubre todo el espacio sin deformarse
            expand=True
        )
    )

    page.add(header)

ft.app(target=main)