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
    def Mostrar_Ficha(self):
        print (f"nombre:{nombre}|edad:{edad}|peso:{peso}|genero:{genero}")
        
        
        
#Subclases y metodos para cada animal     
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre,edad,peso,genero)
        super().mostrar_ficha() 
        self.raza = raza
    def ladrar(self):
        print(f"{self.nombre} esta ladrando")
        
    def Mostrar_Ficha(self):
        print (f"nombre:{nombre}|edad:{edad}|peso:{peso}|genero:{genero}|raza:{raza}")
        
        
        
class Gato(Animal):
    def __init__(self, nombre, edad, color_pelaje):
        super().__init__(nombre, edad,peso,genero)
        super().mostrar_ficha() 
        self.color_pelaje = color_pelaje
    def maullar(self):
        print(f"{self.nombre} esta maullando")
        
    def Mostrar_Ficha(self):
        print (f"nombre:{nombre}|edad:{edad}|peso:{peso}|genero:{genero}|color de pelaje:{color_pelaje}")
        
        
class Pajaro(Animal):
    def __init__(self, nombre, edad, color_plumaje):
        super().__init__(nombre, edad)
        super().mostrar_ficha() 
        self.color_plumaje = color_plumaje
    def volar(self):
        print(f"{self.nombre}esta volando alto")
        
    def Mostrar_Ficha(self):
        print (f"nombre:{nombre}|edad:{edad}|peso:{peso}|genero:{genero}|color de plumaje:{color_plumaje}")
        