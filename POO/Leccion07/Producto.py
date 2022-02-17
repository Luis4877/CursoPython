class Producto:
    contador_productos=0


    def __init__(self,nombre,precio):
        Producto.contador_productos+=1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio=precio

    @property
    def id_producto(self):
        return self._id_producto

    @id_producto.setter
    def id_producto(self,id):
        self.id_producto = id

    @property
    def precio(self):
        return self._precio
    def __str__(self):
        return f'Id producto:{self._id_producto},nombre:{self._nombre},precio:{self._precio}'

if __name__ == '__main__':
    producto1 =Producto('Camisa',100.00)
    print(producto1)
