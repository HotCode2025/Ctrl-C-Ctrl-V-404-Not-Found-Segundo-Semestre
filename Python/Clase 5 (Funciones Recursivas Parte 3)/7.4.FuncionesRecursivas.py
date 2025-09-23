# Funciones Recursivas en Python
# Una función recursiva es una función que se llama a sí misma para resolver un problema

def factorial(n):
    if n == 1: #Caso Base
        return 1
    else: #Caso Recursivo
        return n * factorial(n - 1) # Llamada recursiva

print(factorial(5)) # 120
print(factorial(3)) # 6