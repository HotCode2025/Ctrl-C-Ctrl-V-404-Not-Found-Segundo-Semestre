#Ejercicio 4: Juega adivina el código
#Realizar un juego para adivinar un numero. Para ello se debe
#generar un numero aleatorio entre 1-100, y luego ir pidiendo
#numeros indicando "es mayor" o "es menor" según sea mayor o menor
#con respecto a N. El proceso termina cuando el usuario acierta
#y allí se debe mostrar el número de intentos
# Ejercicio realizado por Rocio Lucero

import random

def pedir_numero():
    return int(input("Debe adivinar un código secreto entre 1 y 100.Ingrese un número: "))

def jugar():
    cod = random.randint(1, 100)
    contador = 0
    n = 0

    while n != cod:
        n = pedir_numero()
        contador += 1

        if n < cod:
            print("El código es mayor")
        elif n > cod:
            print("El código es menor")
        else:
            print(f"¡Felicidades! Adivinaste el código secreto {cod} en {contador} intentos.")

jugar()