from dao.libro_dao import LibroDAO
from models.libro import Libro

def main():
    try: 
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_libros()

        print("LIBROS EN LA BBIBLIOTECA: ")
        if len(libros) == 0: 
            print("No hay libros registrados")
        else:
            for libro in libros:
                print(f"{libro.titulo} - {libro.autor} - {libro.disponible}")

        print("\n Conexion exitosa a la base de datos")
    except Exception as e:
        print(f"Error al conectar la base de datos: {e}")

if __name__ == "__main__":
    main()