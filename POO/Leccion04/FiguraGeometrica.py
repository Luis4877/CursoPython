from abc import ABC,abstractmethod
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self.alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'El alto es de :{self._alto} y el ancho es de :{self._ancho}'
