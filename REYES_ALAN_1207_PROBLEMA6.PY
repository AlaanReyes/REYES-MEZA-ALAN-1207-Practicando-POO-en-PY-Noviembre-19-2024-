print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

class Marino:
    def hablar(self):
        print("Hola soy un animal marino!")

class Pulpo(Marino):
    def hablar(self):
        print("Hola soy un pulpo!")

class Foca(Marino):
    def hablar(self, mensaje):
        print(mensaje)

# Crear instancias de cada clase y llamar al método hablar
marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola soy una foca!")
