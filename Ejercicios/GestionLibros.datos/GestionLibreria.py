import os

class libros:
    def __init__ (self, titulo, autor, precio):
        self.__titulo = titulo
        self.__autor = autor
        self.__precio = int(cantidad)
        assert precio >= 0, "El precio no puede ser negativo"
        
    def __str__ (self):
        return f"{self.titulo} - {self.autor} ({self.cantidad}) | Precio{self.precio}"
    
    
class socio: 
    def __init__ (self,nombre, rut, historial):
        self.Nombre_Socio = Nombre_Socio
        self.__Rut = Rut
        self.__historial = historial
        
    
        
class Biblioteca:
    def __init__ (self, nombre):
        self.__nombre = nombre
        self.__libros = {}
    
#ingresar datos del libro a agregar
    def agregar_libros(self):
        titulo = input("ingresa el titulo del libro:")


        while True:
            cantidad_input = input("ingresa la cantidad de libros disponibles:")
            
            if cantidad_input.isdigit():
                cantidad = int(cantidad_input)
                if 1 <= cantidad <= 9999:
                    cantidadReal = int(cantidad)
                    break
                else:
                    print("formato invalido,intentalo otra vez")
            else:
                print("error")
            
        libroo = Libro(titulo,autor,fechaCorrecta,cantidad)
        self.libros.append(libroo)
        print(f"Se ha agregado un nuevo libro")

#mostrar todos los libros disponibles de la base de datos
    def mostrar_libros (self):
    
        if not self.libros:
            print("No hay libros")
        else: 
            for i, Libro in enumerate(self.libros, 1):
                print(f"{i}: {Libro}")      
                
    def mostrar_carrito (self):
        if not self.libros:
            print("No hay libros")
        else: 
            for i, Libro in enumerate(self.libros, 1):
                print(f"{i}: {Libro}")  
#Numero total de todos los libros agregados                
    def sumar_libros(self):
        total = sum(libro.cantidad for libro in self.libros)
        print(f"cantidad de libros disponibles:")
        print({total})
        return total
                  
                  
#Modificacion de datos de un libro existente
    def comprar (self, cantidad):
        titulo = input ("ingresa el titulo del libro:")
        print ("compra realizada correctamente {Nombre_Libro}")

        
        print("Libro no encontrado")
        
        
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                nuevo_autor = input("ingresa el nombre del nuevo autor:")
                nuevo_titulo = input("ingresa el nuevo titulo del libro:")
                fecha_nueva = input("ingresa el nuevo año de publicacion:")
                nueva_cantidad = input("actualiza la cantidad de libros disponibles:")
                
                if nuevo_titulo: libro.titulo = nuevo_titulo
                if nuevo_autor: libro.autor = nuevo_autor
                if fecha_nueva: libro.fecha = fecha_nueva
                if nueva_cantidad is not None: libro.cantidad = nueva_cantidad
                
                print("Libro Actualizado")
                libros.mostrar_libros()
                return

#Se busca un libro especifico y lo muestra con todos sus datos 
    def buscar (self):
        buscar = input("escribe el nombre de un libro:")
        print(f"buscando {buscar}")
        encontrado = [libro for libro in self.libros if buscar.lower()in libro.titulo.lower()] 
        if encontrado:
            print("libro encontrado,Desplegando datos...")
            for libro in encontrado:
                  print (libro)
        else:
                print("libro no encontrado,intentalo otra vez")
                
                
libros = Biblioteca("prueba")

libros.sumar_libros()



#Inicializacion del bucle principal del codigo
while True:
    print("----------Libreria Chiloe----------")
    print ("Opcion 1:agregar")
    print ("Opcion 2:Mostrar carrito")
    print ("Opcion 3:Comprar")
    print ("Opcion 4:Ver catalogo disponible")
    opcion = input ("ingresa el numero correspondiente del 1 al 4:")
    if opcion == "1":
        libros.agregar_libros()
    if opcion == "2":
        libros.mostrar_carrito()
    if opcion == "3":
        libros.comprar()
    if opcion == "4":
        libros.mostrar_libros()
    

else:
    print("Opcion invalida,intentalo denuevo")