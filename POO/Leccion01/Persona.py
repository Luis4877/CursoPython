class Persona:

    def __init__(self,nombre,apellidos,edad):
        self._nombre = nombre
        self._apellidos=apellidos
        self._edad=edad


    @property
    def nombre(self):
        return self._nombre
    @property
    def apellidos(self):
        return self._apellidos
    @property
    def edad(self):
        return self._edad

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @apellidos.setter
    def apellidos(self,apellidos):
        self._apellidos = apellidos
    @edad.setter
    def edad(self,edad):
        self._edad = edad
    def mostrarDetalle(self):
        print(f'Nombre:{self.nombre}')
        print(f'Apellidos:{self.apellidos}')
        print(f'Edad:{self.edad}')

    def __del__(self):
        print('Objeto eliminado',self.nombre,self.edad)

