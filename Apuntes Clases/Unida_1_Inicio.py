#Se Empieza creando una clase,dentro de ella esta la categorización para los objetos
#los atributos se comparten para todos


class Especie:
#el __init__ es el constructor de clase,se ejecuta de forma automática
#los atributos se comparten para todos
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero


#Self Permite nombrar al constructor de clase init como si mismo


#Def es para la creacion de metodos
    def mover(self):
        print(f"{self.nombre} se esta moviendo")


    def dormir(self):
        print(f"{self.nombre} esta durmiendo")
   
#instanciando el objeto de la clase persona
#Al momento de crear el objeto,se le tiene que asignar TODOS los atributos
P1 = Especie("Camilo", "Hombre", "19")
P2 = Especie("Ian", "Hombre", "22")


print (f"El Nombre de la primera persona es: {P1.nombre} y tiene {P1.edad} años")
print (f"El Nombre de la segunda persona es: {P2.nombre} y tiene {P2.edad} años")


#Utilizando los metodos
P1.mover()
P2.dormir()