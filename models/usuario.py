class Usuario:

    def __init__(self, id=None, nombre="", matricula="", carrera=0, correo="", activo=True):
        self.id = id
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.correo = correo
        self.activo = activo

    def activar(self):
        self.activo = True
        print(f"El usuario {self.nombre} ha sido activado")

    def desactivar(self):
        self.activo = False
        print(f"El usuario {self.nombre} ha sido desactivado")

    def mostrar_info(self):
        estado = "Activo" if self.activo else "Inactivo"
        return (
            f"ID: {self.id}\n"
            f"Nombre: {self.nombre}\n"
            f"Matrícula: {self.matricula}\n"
            f"Carrera: {self.carrera}\n"
            f"Correo: {self.correo}\n"
            f"Estado: {estado}"
        )