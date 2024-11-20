print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO


class preparatoria:
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carrera:
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(preparatoria, Carrera):
    def __init__(self, Nombre):
        # Inicializamos la clase preparatoria
        preparatoria.__init__(self, Nombre)

    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Preparatoria {self.Nombre}")

# Crear una instancia de Estudiante
persona = Estudiante("Cbtis #128")
persona.carrera("Programacion")
persona.datos("Alan Reyes", 16)
