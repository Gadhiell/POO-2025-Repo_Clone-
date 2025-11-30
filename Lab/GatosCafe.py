#supongamos que el numero de hambre y energia son porcentajes
#ejemplo = 9=9%...80=80%...25=25%...etc,etc.


class Gato:
    def __init__ (self, nombre, genero, peso, edad, hambre, energia):
        self.nombre = nombre
        self.genero = genero
        self.peso = float(peso)
        self.edad = int(edad)
        self.hambre = int(hambre)
        self.energia = int (energia)
        
    def jugar(self, tiempo):
        if self.energia >= tiempo * 10:
            self.energia -= tiempo * 10
            self.hambre += tiempo * 5
            print(f"{self.nombre} jugó por {tiempo} minutos... Energía:{self.energia}%, Hambre:{self.hambre}%")
            print("fEnergía : {self.energia}%, Hambre ahora: {self.hambre}%")
        else:
            print(f"{self.nombre} está demasiado cansado para jugar.")



gato1 = Gato("mish", "M", 4, 6, 30, 2)
gato2 = Gato("juanito", "M", 1, 2, 60, 60)
gato3 = Gato("NoName", "F", 8, 7, 0, 100)
gato4 =  Gato("mishi", "F", 3, 4, 20, 5)
gato5 = Gato("pedrito", "M", 8, 7, 0, 100)




#Condicionales con varias elecciones
    Opcion = input ("¿quieres dejar jugar a {nombre}? (S/N)")
    if Opcion == "N":
        print("Gracias por la eleccion")
    elif Opcion == "S":
        Tiempo = input("Cuanto tiempo quieres dejarlo?")


#mostrar informacion del gato


def __str__(self):
    return f"nombre:{nombre}|genero:{genero}|edad:{edad}|hambre:{hambre}%|energia:{energia}%"






def Comer (self,stamina,tipo,):
        self.stamina = stamina
        self.tipo = tipo




#Altura se refiere al numero de piso en la cafeteria
class Espacio:
    def __init__ (self, nombre, Capacidad, altura):
        self.nombre = nombre
        self.Capacidad = int(Capacidad)
        self.altura = int(altura)


lugar1 = Espacio ("terraza", 5, 2 )
lugar2 = Espacio ("salon2", 5, 2 )
lugar3 = Espacio ("salon1", 9 , 1)
lugar4 = Espacio ("entrada", 6, 1 )


#Mostrar datos del espacio
    def __str__(self):
        return f"Espacio: {self.nombre} | Capacidad: {self.Capacidad} gatos | Piso: {self.altura}"





#Finalizador
def __del__ (self):


    print("--------Bienvenido al Cafe De Gatos--------")