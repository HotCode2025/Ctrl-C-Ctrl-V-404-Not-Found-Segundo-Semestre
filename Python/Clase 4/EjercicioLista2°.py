# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los número del 1 al 10, luego modificar los
# elementos de la lista multiplicandolos por un valor ingresado por el usuario

numeros = list(range(1, 11))

while True:
    entrada = input("Ingrese un valor para multiplicar los elementos ('No' para salir): ")
    if entrada.lower() == "no" or "No":
        print("Programa terminado.")
        break
    try:
        multiplicador = float(entrada)
    except ValueError:
        print("Entrada inválida, por favor ingrese un número o 'No'.")
        continue
    lista_modificada = [n * multiplicador for n in numeros]
    print("Lista modificada:", lista_modificada)