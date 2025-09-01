# Factorial de un número positivo
def factorial(numero):
    """
    Calcula el factorial de un número positivo
    """
    if numero == 0 or numero == 1:
        return 1

    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado


print(f" Factorial de 5: {factorial(5)}")