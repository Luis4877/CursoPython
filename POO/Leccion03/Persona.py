class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f'Persona:{self.nombre}, {self.edad}'

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()}, sueldo es de :{self.sueldo}'
