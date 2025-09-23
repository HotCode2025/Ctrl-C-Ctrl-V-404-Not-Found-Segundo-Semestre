def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

# Ejemplos:
print(multiplicar(5, 2))           # 10
print(multiplicar(1, 2, 3, 4, 5))  # 120
print(multiplicar(10))             # 10