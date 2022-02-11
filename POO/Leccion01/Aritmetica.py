# class Rectangulo:
#
#     def __init__(self,Base,Altura):
#         self.Base = Base
#         self.Altura = Altura
#
#     def calcularArea(self):
#
#         return self.Base * self.Altura
#
#
# base = int(input('Inserta la base del rectangulo:'))
# altura = int(input('Inserta la altura del rectangulo:'))
# triangulo1 = Rectangulo(base,altura)
#
# print(triangulo1.calcularArea())



class Cubo:


    def __init__(self,ancho,altura,profundidad):
        self.ancho=ancho
        self.altura=altura
        self.profundidad=profundidad

    def calcularVolumen(self):

        return self.altura*self.profundidad*self.ancho


ancho = int(input('Inserta el ancho del cubo:'))
altura = int(input('Inserta la altura del cubo:'))
profundidad = int(input('Inserta la profunidad del cubo'))

cubo = Cubo(ancho,altura,profundidad)


print(cubo.calcularVolumen())