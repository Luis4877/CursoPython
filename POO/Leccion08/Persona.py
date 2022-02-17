class Persona:

    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def __add__(self, otro):
        return self.nombre + otro.nombre

    def __sub__(self, otro):
        return self.edad-otro.edad
persona1=Persona('Juan',15)
persona2 =Persona('Carlos',25)

print(persona1-persona2)