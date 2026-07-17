import flet as ft

from models.libro import Libro
from dao.libro_dao import LibroDAO

def libro_form(regresar):
    titulo_input = ft.TextField(
        label = "Título del libro: ",
        width = 400
    )
    autor_input = ft.TextField(
        label = "Autor: ",
        width = 400
    )
    isbn_input = ft.TextField(
        label = "ISBN: ",
        width = 400
    )

    mensaje = ft.Text(
        "",
        color = ft.Colors.GREEN
    )

    def guardar_libro(e):
        #Recuperar los valores de los textfield
        titulo = titulo_input.value    #Nombre_text_field.value
        autor = autor_input.value
        isbn = isbn_input.value

        #validacion
        if titulo == "" or autor == "" or isbn == "":
            mensaje.value = "Todos los campos son obligatorios"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return
        try:
            libro_dao = LibroDAO()
            id = libro_dao.obtener_ultimo_id() + 1

            nuevo_libro = Libro(
                id = id,
                titulo = titulo,
                autor = int(autor),
                isbn = isbn,
                disponible = True
            )

            libro_dao.insertar(nuevo_libro)

            mensaje.value = f"Libro '{titulo}' guardado correctamente "
            mensaje.color = ft.Colors.GREEN
            #limpiar los campos de entrada
            titulo_input.value = ""
            autor_input.value = ""
            isbn_input.value = ""
             
        except ValueError:
            mensaje.value = "El campo 'Autor' debe ser un numero entero"
            mensaje.color = ft.Colors.RED

        except Exception as ex:
            mensaje.value = f"Error al guardar el libro: {ex}"
            mensaje.color = ft.Colors.RED

        e.page.update()

    return ft.Container(
        padding = 30,
        content = ft.Column(
            controls = [
                ft.Text (
                    "Insertar Nuevo Libro",
                    size = 24,
                    weight = ft.FontWeight.BOLD
                ), 
                ft.Text(
                    "Capture los datos básicos del libro",
                    size = 14,
                    color = ft.Colors.BLUE_GREY_600
                ),
                titulo_input,
                autor_input,
                isbn_input,

                ft.ElevatedButton(
                    "Guardar",
                    icon = ft.Icons.SAVE,
                    on_click = guardar_libro
                ),
                
                ft.OutlinedButton (
                    "Regresar",
                    icon = ft.Icons.ARROW_BACK,
                    on_click = lambda e: regresar()
                ),

                mensaje 
            ],
            spacing = 15
        )
    )