print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas  # Cambie el nombre de _llantas a llantas para que sea accesible
        self.color = color      # Cambie el nombre de _color a color para que sea accesible
        self.precio = precio    # Cambie el nombre de _precio a precio para que sea accesible

class Moto(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self.llantas, self.color, self.precio))

class Carro(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self.llantas, self.color, self.precio))
        print("OBJETO=carro")

# Crear una instancia de Moto
moto = Moto(2, "Gris", "$200")
moto.cantidad()

# Crear una instancia de Carro
print("OBJETO=carro")
carro = Carro(4, "Negro", "$600")
carro.cantidad()
