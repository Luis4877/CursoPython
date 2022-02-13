class Vehiculo:

    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Color del vehiculo:{self.color}, ruedas del vehiculo:{self.ruedas}'



class Coche(Vehiculo):

    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad=velocidad


    def __str__(self):
      return   f'Datos:{super().__str__()} , velocidad:{self.velocidad}'

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo


    def __str__(self):
        return f'Datos: {super().__str__()}, tipo de bicicleta:{self.tipo}'


vehiculo1 = Vehiculo('VERDE',2)

coche1 = Coche('Rojo','4 ruedas',150)

bicicleta1 = Bicicleta('Rojo',2,'Montaña')

print(vehiculo1)
print(coche1)
print(bicicleta1)