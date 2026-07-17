# Data Access Object (DAO)
# Se encarga de acceder a la base de datos y realizar operaciones CRUD

from database.conexion import Conexion
from models.libro import Libro


class LibroDAO:

    # SELECT
    def obtener_libros(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM vista_libros")
        registros = cursor.fetchall()

        libros = []

        for registro in registros:
            libro = Libro(
                id=registro[0],
                titulo=registro[1],
                autor=registro[2],
                isbn=registro[3],
                disponible=registro[4]
            )
            libros.append(libro)

        cursor.close()
        conexion.close()

        return libros

    # INSERT
    def insertar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO libro (titulo, autor, isbn, disponible)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (
                libro.titulo,
                libro.autor,
                libro.isbn,
                libro.disponible
            )
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    # UPDATE
    def actualizar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE libro
        SET titulo = %s,
            autor = %s,
            isbn = %s,
            disponible = %s
        WHERE id_libro = %s
        """

        cursor.execute(
            sql,
            (
                libro.titulo,
                libro.autor,
                libro.isbn,
                libro.disponible,
                libro.id
            )
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    # DELETE
    def eliminar(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM libro WHERE id_libro = %s",
            (id,)
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    # OBTENER ÚLTIMO ID
    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT id_libro FROM libro ORDER BY id_libro DESC")
        resultado = cursor.fetchone()
        return resultado[0] if resultado and resultado[0] is None else 0

        cursor.close()
        conexion.close()

        return resultado