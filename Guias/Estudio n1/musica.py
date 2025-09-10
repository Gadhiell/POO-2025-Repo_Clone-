class cancion:
    def __init__ (self, titulo, artista, duracionS):
        self.titulo = titulo
        self.artista = artista
        self.duracionS = int(duracionS)


#transformar el formato de la duracion del tema en mm:ss (3:45)
    def milisegundos (self):
        m, s = divmod(max(self.duracionS, 0), 60)
        return f"{m}:{s:02}"


    def __str__ (self):
        return f"{self.titulo} - {self.artista} - ({self.milisegundos()})"

   

class playlist:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.canciones = []


        #añadir temas a la playlist
    def agregar(self, cancion):
            self.canciones.append(cancion)

        #mostrar la duracion de la playlist
    def duracion_total(self):
            #iteracion cancion por cancion
            return sum(c.duracionS for c in self.canciones)
    def milisegundos_total(self):
            total = self.duracion_total()
            m, s = divmod(max(total, 0), 60)
            return f"{m}:{s:02}"
       
    def __len__(self):
            return len (self.canciones)

        #Combinar playlist
    def __add__ (self, otra):
            nueva = playlist(f"{self.nombre} + {otra.nombre}")
            #Guardar en las playlist combinadas
            nueva.canciones = self.canciones + otra.canciones
            return nueva
       
    def __str__(self):
            encabezado = f"Playlist {self.nombre} | {len(self)} canciones | Duración total: {self.milisegundos_total()}"
            #lanzar mensaje en caso de que la lista esta vacia
            if not self.canciones:
                return encabezado , "Lista vacia"
            lineas = [encabezado]
            for i, c in enumerate(self.canciones, start=1):
                lineas.append(f"{i}: {c}")
            return "\n".join(lineas)


#Lista de canciones con sus datos
cancion1 = cancion("Now or never", "Kendrick lamar", "256")
cancion2 = cancion("Ring Ring", "De La Soul" ,"306")
cancion3 = cancion("Your Type", "Carly Rae Jepsen" ,"200")
cancion4 = cancion("Hallucinate", "Dua Lipa" ,"209")
cancion5 = cancion("Doomsday", "MF Doom" ,"299")
cancion6 = cancion("Classic", "The Knocks" ,"249")

#Creacion de las playlist junto con añadir canciones
playlist1 = playlist("Rap")
playlist1.agregar(cancion1)
playlist1.agregar(cancion2)
playlist1.agregar(cancion5)

playlist2 = playlist("Pop")
playlist2.agregar(cancion3)
playlist2.agregar(cancion4)
playlist2.agregar(cancion6)
 
 

# impresion de las playlist
print(playlist1)

print(playlist2)

# Combinar las playlist
combinado = playlist1 + playlist2
print("Playlist Combinada:\n", combinado) 

# Mostrar el numero de canciones de la nueva playlis
print("\n Total de canciones en Playlist Combinada:", len(combinado))