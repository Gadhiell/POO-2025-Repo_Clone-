from datetime import datetime #herramienta para trabajar con fechas y horas

class ReservaHostal:
    def __init__ (self, Nombre_Cliente, entrada, salida, NHabitaciones):
        self.Nombre_Cliente = Nombre_Cliente
        self.entrada = datetime.strptime(entrada, "%Y-%m-%d")#Strptime transforma un string en un objeto con el formato de fecha (DATETIME)
        self.salida = datetime.strptime(salida, "%Y-%m-%d")
        self.NHabitaciones = int(NHabitaciones)
        
        
    def calcular_duracion(self):
        return (self.salida - self.entrada).days


    def cambiar(self, nueva_salida):
        nueva_salida_dt = datetime.strptime(nueva_salida, "%Y-%m-%d")
        if nueva_salida_dt <= self.entrada:
            print("La nueva fecha de salida no puede ser anterior o igual a la fecha de entrada.")
        else:
            self.salida = nueva_salida_dt
            print("Fecha de salida actualizada.")


#Metodo para desplegar la informacion
    def __str__ (self):
        return (
            f"Reserva de Hostal:\n"
            f"Cliente: {self.Nombre_Cliente}\n"
            f"Fecha de entrada: {self.entrada.strftime('%Y-%m-%d')}\n"
            f"Fecha de salida: {self.salida.strftime('%Y-%m-%d')}\n"
            f"Número de habitación: {self.NHabitaciones}\n"
            f"Duración de estadía: {self.calcular_duracion()} dias\n"
            f"---------------------------------------------------------------------------------------------------------------------------\n"
        )
reserva = ReservaHostal("Test Name", "2025-09-20", "2025-09-25", 2)
print(reserva)

#interacciones y opciones para la reserva
while True:
    print("Presiona 0 para cancelar la reserva.")
    print("Presiona 1 para cambiar la fecha de salida.")
    print("Presiona 2 para salir del menú.")
    opcion = input("Elige Una Opcion: ")

    if opcion == "0":
        reserva.cancelar()
        
    elif opcion == "1":
        nueva_fecha = input("Ingresa la nueva fecha de salida (YYYY-MM-DD): ")
        reserva.cambiar(nueva_fecha)
    
    elif opcion == "2":
        print("Saliendo del menú.")
        break
    else:
        print("opcion no valida.")
        exit()
    print(reserva)