# Data Access Object (DAO)
# Se encarga de acceder a la base de datos y realizar operaciones CRUD

from database.conexion import Conexion
from models.usuario import Usuario


class UsuarioDAO:

    # SELECT
    def obtener_usuarios(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM usuario")
        registros = cursor.fetchall()

        usuarios = []

        for registro in registros:
            usuario = Usuario(
                id=registro[0],
                nombre=registro[1],
                matricula=registro[2],
                carrera=registro[3],
                correo=registro[4],
                activo=registro[5]
            )
            usuarios.append(usuario)

        cursor.close()
        conexion.close()

        return usuarios

    # INSERT
    def insertar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO usuario (nombre, matricula, carrera, correo, activo)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (
                usuario.nombre,
                usuario.matricula,
                usuario.carrera,
                usuario.correo,
                usuario.activo
            )
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    # UPDATE
    def actualizar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuario
        SET nombre = %s,
            matricula = %s,
            carrera = %s,
            correo = %s,
            activo = %s
        WHERE id = %s
        """

        cursor.execute(
            sql,
            (
                usuario.nombre,
                usuario.matricula,
                usuario.carrera,
                usuario.correo,
                usuario.activo,
                usuario.id
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
            "DELETE FROM usuario WHERE id = %s",
            (id,)
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    # OBTENER ÚLTIMO ID
    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM usuario ORDER BY id DESC")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado