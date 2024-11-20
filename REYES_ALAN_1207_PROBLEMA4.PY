print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        print(self.nombre + " " + self.apellido)  # corregido el uso de las comillas y el espacio

class Estudiante(Persona):
    def __init__(self, nom, ape, carr):
        super().__init__(nom, ape)  # llamada correcta al constructor de la clase base (Persona)
        self.carrera = carr

    def mostrar_carrera(self):
        print(self.carrera)  # muestra la carrera del estudiante

# Crear una info de Estudiante
estudiante = Estudiante("Alan", "Reyes", "Programacion")
estudiante.nombre_completo()  # Imprime el nombre completo
estudiante.mostrar_carrera()  # Imprime la carrera
