class FiguraGeometrica:
    def __init__(self,ancho,alto):
        self._ancho = ancho
        self._alto = alto

    def ancho(self,ancho):
        self._ancho = ancho

    def ancho(self):
        return self._ancho

    def alto(self,alto):
        self._alto = alto

    def alto(self):
        return self._alto


    def __str__(self):
        return f'El alto es de :{self._alto} y el ancho es de :{self._ancho}'

