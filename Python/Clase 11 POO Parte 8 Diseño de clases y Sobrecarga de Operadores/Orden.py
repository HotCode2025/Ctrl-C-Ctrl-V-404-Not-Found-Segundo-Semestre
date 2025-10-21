from Producto import Producto

class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_productos(self, producto):
        self._productos.append(producto) #Agrega nuevo producto

    #caculamos el total
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    #imprimimos
    def __str__(self):
        productos_str = ""
        for producto in self._productos:
            productos_str += producto.__str__() + "|"
        return f"Orden: {self._id_orden}, \nProducto: {productos_str}"

if __name__ == "__main__":
    producto1 = Producto("Camisa", 40000)
    producto2 = Producto("Pantalon", 10000)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)
    producto3 = Producto("Camiseta", 4800)
    producto4 = Producto("Pollera", 1000)
    productos2 = [producto3, producto4]
    orden2 = Orden(productos2)
    print(orden2)