import math
num = int(input("Ingrese un numero entero positivo para calcular su raiz cuadrada"))

while num < 0:
    print("Error, ingrese un numero positivo")
    num = int(input("Ingrese un numero entero positivo para calcular su raiz cuadrada"))
print(f'\nLa raiz cuadrada es: {math.sqrt(num):.2f}')