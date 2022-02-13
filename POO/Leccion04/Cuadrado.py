from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularArea(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Los datos del cuadrado son:{FiguraGeometrica.__str__(self)},{Color.__str__(self)}'
