# Ejemplo Práctico: Uso del Finally (Manejo de Archivos con biblioteca os)

import os # biblioteca que permite interactuar con el sistema operativo
print("Directorio de trabajo actual:", os.getcwd()) # muestra la ubicación del directorio actual

ruta = 'Python-Ulagos-2025/Data/datos.txt' # esta ruta debe modificarse por la ruta de su directorio donde se ubica su archivo .txt

try:
    archivo = open(ruta, "r") 
    contenido = archivo.read()
    print(f"Contenido del txt: {contenido}")
except FileNotFoundError:
    print("¡El archivo no existe!")
else:
    print("¡Lectura exitosa!")
finally: # El Finally: Ejecuta una acción de limpieza: cerrar el archivo si fue abierto
    try:
        archivo.close()
        print("Archivo cerrado")
    except NameError:
        print("No fue necesario cerrar el archivo")