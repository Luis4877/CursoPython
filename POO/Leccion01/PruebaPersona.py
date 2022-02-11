from Persona import Persona


print('Creacion Objetos'.center(50,'*'))
persona1 = Persona('Karla','GOMEZ',30)

persona1.mostrarDetalle()

print('Eliminacion de Objetos'.center(50,'x'))
persona1.__del__()