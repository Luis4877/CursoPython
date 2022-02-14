class MiClase:

    variable_clase = 'Hola mundo xd'

    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia
    #Metodo estatico de clase,no puede acceder a las variables de instancia directamente
    @staticmethod
    def metodo():
        print(MiClase.variable_clase)
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)


MiClase.metodo_clase()
miObjeto1 = MiClase('Variable de instancia')
miObjeto1.metodo_clase()