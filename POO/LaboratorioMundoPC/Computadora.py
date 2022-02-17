from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora():
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'ID:{self._id_computadora},\nnombre:{self._nombre},monitor:{self._monitor},teclado:{self._teclado},raton:{self._raton}'



