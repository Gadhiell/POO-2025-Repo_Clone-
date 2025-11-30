import random
#SuperClase
class Vehiculos:
    def __init__ (self, nombre, velocidad, color, marca):
        self.nombre = nombre
        self.velocidad = float(velocidad)
        self.color = color
        self.marca = marca
        
    
    def __str__(self):
        if self.velocidad <= 0:
            return f"{self.nombre} NO participará en la carrera (velocidad = {self.velocidad} km/h)"
        else:
            return f"{self.nombre} está listo para la carrera a {self.velocidad} km/h"
        
        
class Terrestre:
    def __init__ ():
        super().__init__(nombre, velocidad, color, marca)
class Aereos:
    def __init__ ():
        super().__init__(nombre, velocidad, color, marca)

class Acuatico:
    def __init__ ():
        super().__init__(nombre, velocidad, color, marca)

    
    
#Objetos agrupados en lista segun su tipo
Vehiculos_Tierra = [
    Coche("Coche1", 120, "Rojo", "Ferrari"),
    Moto("Moto1", 100, "Negro", "Yamaha")
]

Vehiculos_Aire = [
    Avioneta("Avioneta1", 200, "Blanco", "Alt"),
    Avion("Avion1", 900, "Gris", "Generic")
]

Vehiculos_Mar = [
    Barco("Barco1", 40, "Azul", "Maersk"),
    Lancha("Lancha1", 80, "Rojo", "Yamaha"),
    Velero("Velero1", 30, "Blanco", "Beneteau")
]

Vehiculos_Hibridos = [
    VehiculoAnfibio("Anfibio1", 60, "Verde", "General Dynamics"),
    Hidroavion("Hidroavion1", 300, "Amarillo", "Bombardier")
]




# Filtrar vehículos válidos
vehiculos_validos = []
print("🔍 Verificando vehículos...\n")
for v in vehiculos:
    print(v)
    if v.velocidad > 0:
        vehiculos_validos.append(v)
print("\n✅ Vehículos listos para la carrera:", len(vehiculos_validos))
print("=" * 50)

# Iniciar carrera solo con los válidos
if vehiculos_validos:
    print("🏁 ¡Comienza la carrera!\n")
    for v in vehiculos_validos:
        print(f"{v.nombre} en movimiento:")
        v.moverse()
        print("-" * 30)
else:
    print("❌ No hay vehículos disponibles para la carrera.")
