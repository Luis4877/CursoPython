

class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        Persona.contador_personas+=1
        return Persona.contador_personas

    def __init__(self,nombre,edad):
        #Contador de Objetos tipo persona

        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona : {self.id_persona},{self.nombre},{self.edad}'


persona = Persona('Juan',24)
print(persona)

persona2 = Persona('Luis',24)
print(persona2)