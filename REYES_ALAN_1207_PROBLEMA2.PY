print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1

# crear una instancia de Persona con los datos de entrada
p = Persona(input("Ingrese su nombre: "), int(input("Ingrese su edad: ")))
p.cumpleaños()  # aumentamos la edad una vez
p.cumpleaños()  # aumentamos la edad otra vez

# mostrar el resultado
print(f"{p.nombre} cumple {p.edad} años")
