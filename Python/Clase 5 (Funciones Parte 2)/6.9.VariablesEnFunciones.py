# Argumentos, Variables en Funciones
# Las variables definidas dentro de una función son locales a esa función.

def listarNombres(*args): # El asterisco permite recibir un numero variable de argumentos
    for nombre in args:
        print(nombre)

listarNombres('Juan', 'Ana', 'Pedro') # Llamada a la función con 3 argumentos