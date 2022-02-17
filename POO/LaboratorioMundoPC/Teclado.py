from DispositivosEntrada import  DispositivosEntrada
class Teclado(DispositivosEntrada):
    contadorTeclados =0

    def __init__(self,tipoEntrada,marca):
        Teclado.contadorTeclados+=1
        self._idTeclado=Teclado.contadorTeclados
        super().__init__(tipoEntrada,marca)


    def __str__(self):
        return f'Teclado:ID{self._idTeclado},Tipo Entrada:{self._tipoEntrada},marca:{self._marca}'

