from ClaseHijaCuadrado import Cuadrado
from ClaseHijaRectangulo import Rectangulo

print("Creación de la clase Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(8, "Rojo")
cuadrado1.ancho = -10
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Calculo el área del cuadrado: {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
# Indica el orden en el que Python busca los atributos y métodos en una jerarquía de clases con herencia múltiple
print(Cuadrado.mro())  # Muestra el orden de resolución de métodos para la clase Cuadrado
print(cuadrado1)  # Llama al método __str__ de la clase Cuadrado

print("Creación de la clase Rectángulo".center(50, "-"))
rectangulo1 = Rectangulo(3, 9, "Azul")
rectangulo1.ancho = 15
print(f'Calculo el área del rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)  # Llama al método __str__ de la clase Rectangulo