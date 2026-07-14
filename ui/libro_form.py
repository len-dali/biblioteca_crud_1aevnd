import flet as ft

def libro_form():
    titulo_input = ft.TextField(
        label = "Título del libro: ",
        width = 400
    )
    autor_input = ft.TextField(
        label = "Autor: ",
        witdh = 400
    )
    isbn_input = ft.TextField(
        label = "ISBN: ",
        witdh = 400
    )

    mensaje = ft.Text(
        "",
        coor = ft.Colors.GREEN
    )