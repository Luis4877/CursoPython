class Empleado:
    def __init__(self,nombre,sueldo):
        self._nombre = nombre
        self._sueldo = sueldo


    @property

    def nombre(self):
        return self._nombre

    @nombre.setter

    def nombre(self,nuevo):
        self._nombre = nuevo


    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self,nuevo):
        self._sueldo = nuevo


    def __str__(self):
        return f'Empleado:[Nombre:{self.nombre},Sueldo:{self.sueldo}]'



