class PERSONA:

    def __init__(self, nombre, genero, altura, peso, edad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.altura = float(altura)
        self.peso = float(peso)

    def Calcular_IMC(self):
    
        IMC = self.peso / (self.altura ** 2)
        
        if IMC < 18.5:
            rango = "bajo peso"
        elif 18.5 <= IMC < 24.9:
            rango = "peso normal"
        elif 24.9 <= IMC < 30:
            rango = "sobrepeso"
        else:
            rango = "obesidad"
        
        print(f"El índice de masa corporal de {self.nombre} es {IMC} - {rango}")


    def Promedio_Asignatura(self, n1, n2, n3):

        promedio = (n1 + n2 + n3) / 3
        
        if promedio >= 4.0:
            print(f"{self.nombre} aprobó con un promedio de: {promedio}")
        else:
            print(f"{self.nombre} no aprobó asignatura con un Promedio de: {promedio}:")

estudiante1 = PERSONA("Camilo", "Hombre", 1.80, 95, 19)

estudiante1.Calcular_IMC()

estudiante1.Promedio_Asignatura(3.8, 4.2, 4.5)