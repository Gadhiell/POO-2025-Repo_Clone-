class Trabajador:
    def __init__(self, nombre):
        self.nombre = nombre

    def tarea(self):
        print(self.nombre, "está trabajando")


class Chef(Trabajador):
    def __init__(self, nombre, especialidad):
        Trabajador.__init__(self, nombre)
        self.especialidad = especialidad

    def tarea(self):
        print(self.nombre, "está cocinando", self.especialidad)


class Mesero(Trabajador):
    def __init__(self, nombre, seccion):
        Trabajador.__init__(self, nombre)
        self.seccion = seccion

    def tarea(self):
        print(self.nombre, "está sirviendo comida en la sección", self.seccion)


class AyudanteChefMesero(Chef, Mesero):
    def __init__(self, nombre, especialidad, seccion):
        Trabajador.__init__(self, nombre)
        self.especialidad = especialidad
        self.seccion = seccion

    def tarea(self):
        print(self.nombre, "está ayudando en cocina de", self.especialidad, "y en la sección", self.seccion)


# Creación de objetos
Trabajador1 = Trabajador("Sujeto")
Chef1 = Chef("ChefPro", "Pizza")
Mesero1 = Mesero("Cualquiera", "Área 67")
Ayudante1 = AyudanteChefMesero("Dante", "Fideos", "Área 08")

# Llamadas a métodos
Trabajador1.tarea()
Chef1.tarea()
Mesero1.tarea()
Ayudante1.tarea()