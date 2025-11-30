#SuperClase
class Animal:
    def __init__(self, nombre, edad, genero, peso):
        self.nombre = nombre
        self.edad = int(edad)
        self.genero = genero
        self.peso = float(peso)
        
    def comer(self):
        print (f"{self.nombre} esta comiendo")
        
    def dormir(self):
        print (f"{self.nombre} esta durmiendo")
        
#IMPRIMIR FICHA
    def mostrar_Ficha(self):
        print (f"nombre:{nombre}|edad:{edad}|peso:{peso}Kg|genero:{genero}")
        
        
        
#Subclases y metodos para cada animal     
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, peso, genero)
        super().mostrar_Ficha() 
        self.raza = raza
    def ladrar(self):
        print(f"{self.nombre} esta ladrando")
        
    def mostrar_Ficha(self):
        print (f"nombre:{self.nombre}|edad:{self.edad}|peso:{self.peso}Kg|genero:{self.genero}|raza:{self.raza}")
        
        
        
class Gato(Animal):
    def __init__(self, nombre, edad, color_pelaje):
        super().__init__(nombre, edad, peso, genero)
        super().mostrar_Ficha() 
        self.color_pelaje = color_pelaje
    def maullar(self):
        print(f"{self.nombre} esta maullando")
        
    def mostrar_Ficha(self):
        print (f"nombre:{self.nombre}|edad:{self.edad}|peso:{self.peso}Kg|genero:{self.genero}|color de pelaje:{self.color_pelaje}")
        
        
class Pajaro(Animal):
    def __init__(self, nombre, edad, color_plumaje):
        super().__init__(nombre, edad)
        super().mostrar_Ficha() 
        self.color_plumaje = color_plumaje
    def volar(self):
        print(f"{self.nombre}esta volando alto")
        
    def mostrar_Ficha(self):
        print (f"nombre:{self.nombre}|edad:{self.edad}|peso:{self.peso}Kg|genero:{self.genero}|color de plumaje:{self.color_plumaje}")
        
        
#Creacion de objetos
perro1 = Perro ("Generico", 3, "bulldog", 4, "macho")
gato1 = Gato ("mishi", 1, "amarillo", 2, "hembra")
Pajaro1 = Pajaro ("Birdy", 2, "verde")


perro1.mostrar_Ficha()
perro1.dormir()#metodo de superclase
perro1.ladrar()#metodo de subclase perro

gato1.mostrar_Ficha()
gato1.maullar()#metodo de subclase gato

Pajaro1.mostrar_Ficha()
Pajaro1.comer()#metodo de superclase
Pajaro1.volar()#metodo de subclase pajaro