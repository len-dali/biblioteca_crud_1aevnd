from dao.libro_dao import LibroDAO
from dao.usuario_dao import UsuarioDAO
from models.libro import Libro
from models.usuario import Usuario

def ver_todo(libro_dao):
    try: 
        libros = libro_dao.obtener_libros()

        print("LIBROS EN LA BIBLIOTECA: ")
        if len(libros) == 0: 
            print("No hay libros registrados")
        else:
            for libro in libros:
                print(f"{libro.titulo} - {libro.autor} - {libro.disponible}")

        print("\n Conexion exitosa a la base de datos")

    except Exception as e:
        print(f"Error al conectar la base de datos: {e}")


def insertar_libro(libro_dao):
    try:
        print("--------------------------------------")
        print("Inserccion de un nuevo libro")
        titulo = input("Escribe titulo del libro: ")
        autor = int(input("Escribe el id del autor: "))
        isbn = input("Escribe el ISBN del libro: ")
        disponible = True
        nuevoLibro = Libro(8,titulo,autor,isbn,disponible)
        libro_dao.insertar(nuevoLibro)
    except Exception as e:
        print(f"Error al insertar libro: {e}")

def actualizar_libro(libro_dao):
    ver_todo(libro_dao)

    id = int(input("Escribe el id del libro a editar: "))
    print("Actualiza los datos de este libro")

    titulo = input("Escribe el nuevo titulo del libro: ")
    autor = int(input("Escribe el nuevo id del autor: "))
    isbn = input("Escribe el nuevo isdn del libro: ")

    respuesta = input("Escribe si el libro esta disponible o no (si/no): ")

    if respuesta.lower() == "si":
        disponible = True
    else:
        disponible = False

    libro = Libro(id, titulo, autor, isbn, disponible)
    libro_dao.actualizar(libro)

    print("Libro actualizado correctamente")

def eliminar_libro(libro_dao):
    ver_todo(libro_dao)
    id = input("Escribe el id del libro a eliminar: ")
    libro_dao.eliminar(id)
    print("Libros disponibles")
    ver_todo(libro_dao)


def ver_usuarios(usuario_dao):
    try:
        usuarios = usuario_dao.obtener_usuarios()

        print("USUARIOS REGISTRADOS:")
        if len(usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            for usuario in usuarios:
                print(f"{usuario.nombre} - {usuario.matricula} - {usuario.carrera} - {usuario.correo} - {usuario.activo}")

        print("\nConexión exitosa a la base de datos")

    except Exception as e:
        print(f"Error al conectar la base de datos: {e}")


def insertar_usuario(usuario_dao):
    try:
        print("--------------------------------------")
        print("Inserción de un nuevo usuario")

        nombre = input("Escribe el nombre del usuario: ")
        matricula = input("Escribe la matrícula: ")
        carrera = int(input("Escribe el id de la carrera: "))
        correo = input("Escribe el correo: ")

        respuesta = input("¿El usuario está activo? (si/no): ")

        if respuesta.lower() == "si":
            activo = True
        else:
            activo = False

        nuevoUsuario = Usuario(
            id,
            nombre,
            matricula,
            carrera,
            correo,
            activo
        )

        usuario_dao.insertar(nuevoUsuario)

        print("Usuario insertado correctamente")

    except Exception as e:
        print(f"Error al insertar usuario: {e}")


def actualizar_usuario(usuario_dao):
    ver_usuarios(usuario_dao)

    id = int(input("Escribe el id del usuario a editar: "))

    print("Actualiza los datos del usuario")

    nombre = input("Nuevo nombre: ")
    matricula = input("Nueva matrícula: ")
    carrera = int(input("Nuevo id de la carrera: "))
    correo = input("Nuevo correo: ")

    respuesta = input("¿El usuario está activo? (si/no): ")

    if respuesta.lower() == "si":
        activo = True
    else:
        activo = False

    usuario = Usuario(
        id,
        nombre,
        matricula,
        carrera,
        correo,
        activo
    )

    usuario_dao.actualizar(usuario)

    print("Usuario actualizado correctamente")


def eliminar_usuario(usuario_dao):
    ver_usuarios(usuario_dao)

    id = int(input("Escribe el id del usuario a eliminar: "))

    usuario_dao.eliminar(id)

    print("Usuario eliminado correctamente")

    ver_usuarios(usuario_dao)

def menu_libros():
    libro_dao = LibroDAO()
    
    #IMPRIMIR EL MENU DE OPCIONES
    print("1. Ver todos los libros")
    print("2. Insertar un libro")
    print("3. Actualizar un libro existente")
    print("4. Eliminar un libro existente")

    opcion = int(input("Escribe una opcion (1-4):"))

    match opcion:
        case 1: ver_todo(libro_dao)
        case 2: insertar_libro(libro_dao)
        case 3: actualizar_libro(libro_dao)
        case 4: eliminar_libro(libro_dao)


def menu_usuarios():
    usuario_dao = UsuarioDAO()
    
    #IMPRIMIR EL MENU DE OPCIONES
    print("1. Ver todos los usuarios")
    print("2. Insertar nuevo usuario")
    print("3. Actualizar un usuario existente")
    print("4. Eliminar un usuario existente")

    opcion = int(input("Escribe una opcion (1-4):"))

    match opcion:
        case 1: ver_usuarios(usuario_dao)
        case 2: insertar_usuario(usuario_dao)
        case 3: actualizar_usuario(usuario_dao)
        case 4: eliminar_usuario(usuario_dao)
    
def main():
    print("==BIBLIOTECA UNIVERSITARIA==")
    print("====== MENÚ DE OPCIONES======")
    print("1. Gestión de libros")
    print("2. Gestion de usuarios")

    opcion = int(input("Escribe tu opción: "))

    match opcion:
        case 1: menu_libros()
        case 2: menu_usuarios()

if __name__ == "__main__":
    main()