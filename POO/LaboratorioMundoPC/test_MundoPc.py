from Computadora import Computadora
from Monitor import Monitor
from Orden import Orden
from Raton import Raton
from Teclado import Teclado

teclado = Teclado('USB','HP')
raton = Raton('USB','HP')
monitor = Monitor('Samsung',35)

computadora = Computadora('Luis Pc',monitor,teclado,raton)


computadoras1 = [computadora]

orden = Orden(computadoras1)


print(orden)

