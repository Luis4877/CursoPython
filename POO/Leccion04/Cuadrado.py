from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica,Color):

    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)


    def calcularArea(self):
     return self.alto * self.ancho




cuadro1 = Cuadrado(5,'Rojo')

print(cuadro1.calcularArea())

print(Cuadrado.mro())

