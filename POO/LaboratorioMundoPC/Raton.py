from DispositivosEntrada import DispositivosEntrada
class Raton(DispositivosEntrada):
    contadorRatones=0
    def __init__(self,tipoEntrada,marca):
        Raton.contadorRatones+=1

        self._idRaton = Raton.contadorRatones
        super().__init__(tipoEntrada,marca)
    def __str__(self):
        return f'Raton:[ID:{self._idRaton},Marca:{self._marca},tipo Entrada:{self._tipoEntrada}'

