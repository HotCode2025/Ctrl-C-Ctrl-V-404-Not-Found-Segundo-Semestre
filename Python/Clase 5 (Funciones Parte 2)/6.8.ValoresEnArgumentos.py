# Valores por defecto en argumentos (funciones)

def sumar(a, b=0): # b tiene un valor por defecto
    return a + b
print(sumar(3)) # 3, b toma el valor por defecto 0
print(sumar(3, 8)) # 11, b toma el valor 8