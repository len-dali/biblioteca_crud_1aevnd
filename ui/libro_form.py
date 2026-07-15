import flet as ft

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
        else:
            mensaje.value = f"Libro '{titulo}' guardado correctamente "
            mensaje.color = ft.Colors.GREEN
            print(f"Título: {titulo}, Autor: {autor}, ISBN: {isbn}")
            titulo_input.value = ""
            autor_input.value = ""
            isbn_input.value = ""

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