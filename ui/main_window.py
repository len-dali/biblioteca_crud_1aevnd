import flet as ft

def main_window(page: ft.Page):
    #definir configuracion de la pagina principal
    page.title = "Sistema de Gestion de Biblioteca"
    page.window_width = 1100
    page.windown_height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_50

    #Widget etiqueta o Text
    titulo = ft.Text(
        "Sistema de Gestion de Bibliotea",
        size = 24,
        weight = ft.Weight.BOLD
    )

    subtitulo = ft.Text(
        "Seleccione una opcion del menú",
        size = 16,
        color = ft.Colors.BLUE_GREY_600
    )

    #Contenedor central
    contenido = ft.Container(
        content = ft.Column(
            controls = [titulo, subtitulo],
            spacing = 10
        ),
        padding = 30,
        expand = True
    )

    #Menu lateral
    menu_lateral = ft.Container(
        width = 220,
        bgcolor = ft.Colors.BLUE_GREY_900,
        padding = 20,
        content = ft.Column(
            controls = [
                ft.text(
                    "Biblioteca",
                    size = 22,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.WHITE
                ),
                ft.Text(
                    "Sistema de Gestion",
                    size = 12,
                    color = ft.Colors.BLUE_GREY_100
                ),
                ft.Divider(color = ft.Colors.BLUE_GREY_700),
                #botones
                ft.ElevatedButton(
                    text = "Libros",
                    icon = ft.Icons.BOOK,
                    width = 180
                ),
                ft.ElevatedButton(
                    text = "Usuarios",
                    icon = ft.Icons.PERSON,
                    width = 180
                ),
                ft.ElevatedButton(
                    text = "Prestamos",
                    icon = ft.Icons.SWAP_HORIZ,
                    width = 180
                ),
                ft.ElevatedButton(
                    text = "Devoluciones",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    width = 180
                ),                               
            ],
            spacing = 15
        )
    )

    #definicion del layout de la pagina
    layout = ft.Row(
        controls = [
            menu_lateral,
            contenido
        ],
        expand = True 
    )

    #agregar el layout a la pagina
    page.add(layout)