from Color import Color
from FiguraGeometrica import FiguraGeometrica
from Cuadrado import Cuadrado


class Rectangulo(FiguraGeometrica, Color):

    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def CalcularArea(self):
        return f'El Area del Rectangulo es de :{self._alto * self._ancho}'

    def __str__(self):
        return f'Los datos del rectangulo es de :{FiguraGeometrica.__str__(self)},{Color.__str__(self)}'


cuadrado1 = Cuadrado(5, 'rojo')

print(cuadrado1)
print(cuadrado1.calcularArea())
rectangulo1 = Rectangulo(3, 8, 'Rojo')
print(rectangulo1)
print(rectangulo1.CalcularArea())
