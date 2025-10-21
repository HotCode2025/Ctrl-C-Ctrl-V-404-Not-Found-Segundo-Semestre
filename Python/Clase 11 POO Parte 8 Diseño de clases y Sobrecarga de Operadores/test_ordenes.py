from Orden import Orden
from Producto import Producto

producto1 = Producto("Camisa", 40000)
producto2 = Producto("Pantalon", 10000)
producto3 = Producto("Camiseta", 4800)
producto4 = Producto("Pollera", 1000)

productos1 = [producto1, producto2]
orden1 = Orden(productos1)
print(orden1)
print(f'Total de la orden 1: {orden1.calcular_total()}')

productos2 = [producto3, producto4]
orden2 = Orden(productos2)
print(orden2)
print(f'Total de la orden 2: {orden2.calcular_total()}')

orden2.agregar_productos(producto1)
print(orden2)
print(f'Total de la orden 2: {orden2.calcular_total()}')
