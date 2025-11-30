import random

class Contenido:
    def __init__ (self, titulo, anio):
        self.titulo = str(titulo)
        self.anio = anio  (str)
    
    
    def mostrar_detalle(self):
        print (f"Nombre:{self.titulo}|año de lanzamiento:{self.anio}")
        
        
class Reproducible:
    def __init___(self):
        def Reproducir():
            pass
    
class Calificable:
    def __init__ ( rating):
        self.rating = float (rating = 0.0)
    
    def Calificar(puntuacion):
            print (f"Calificacion:{self.rating}")
    
    


#Subclases
class Pelicula(Contenido, Reproducible):
    def __init__(duracion_minutos):
        super().__init__(self, titulo, anio)
        super().mostrar_detalle() 
        self.duracion_minutos = int(duracion_minutos)

            
class Documental(Contenido):
    def __init__(tema):
        super().__init__(self, titulo, anio)
        super().mostrar_detalle() 
        self.tema = str(tema)
        

            
            
class Miniserie(Contenido, Reproducible, Calificable):
    def __init__(num_episodios):
        super().__init__(self, titulo, anio)
        super().mostrar_detalle()
        self.num_episodios = int(num_episodios)
        
            
            
            
#Creacion de Objetos
Peli = Pelicula ("TestPeli", 2009, random.randit(60, 120) )
docum = Documental ("TestDocu", 1985, "Politica")
Serie = Miniserie ("TestSerie", 2017, random.randint(20, 150))

            
            
