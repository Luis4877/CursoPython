from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(obj):
    print(obj)
    print(type(obj))

empleado1= Empleado('Luis Valdez','5000')
imprimir_detalles(empleado1)

gerente=Gerente('Luis Valdez',1000,'Sistemas')

imprimir_detalles(gerente)