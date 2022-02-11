class Vehiculo:

    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Color del vehiculo:{self.color}, ruedas del vehiculo:{self.ruedas}'



class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    def __str__(self):

        return f'{super().__str__()}, velocidad :{self.velocidad}'


class Bicicleta(Vehiculo):

    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo


    def __str__(self):
        return f'{super().__str__()}, Tipo:{self.tipo}'


vehiculo1 = Vehiculo('Rojo',2)
print(vehiculo1)

coche1 = Coche('ROJO',2,150)
print(coche1)

bici1 = Bicicleta('Azul marino',2,'Montaña')
print(bici1)


