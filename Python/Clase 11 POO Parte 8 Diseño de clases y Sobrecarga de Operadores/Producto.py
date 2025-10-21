class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, Nombre):
        self._nombre = Nombre

    @property
    def precio(self):
         return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}"


#pruebas
if __name__ == "__main__":
    producto1 = Producto("Camisa", 40000)
    producto2 = Producto("Pantalon", 10000)
    print(producto1.__str__())
    print(producto2.__str__())