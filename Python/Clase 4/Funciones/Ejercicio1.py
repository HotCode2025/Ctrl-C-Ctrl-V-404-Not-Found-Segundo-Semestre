# Sumar números pares dentro de un rango
def sumar_pares(inicio, fin):
    """
    Suma todos los números pares dentro de un rango
    Ejemplo: sumar números pares del 2 al 30 = 240
    """
    suma = 0
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:  # Si es par
            suma += numero
    return suma


print(f"Suma de números pares del 2 al 30: {sumar_pares(2, 30)}")