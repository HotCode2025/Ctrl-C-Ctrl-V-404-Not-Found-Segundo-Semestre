# Tabla de multiplicar
def tabla_multiplicar(numero):
    """
    Genera la tabla de multiplicar de un número hasta el 10
    y la guarda en una lista
    """
    tabla = []
    for i in range(1, 11):
        resultado = numero * i
        tabla.append(resultado)
    return tabla


# Función para pedir número por teclado
def tabla_multiplicar_interactiva():
    """
    Función que pide un número por teclado y muestra su tabla
    """
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla = tabla_multiplicar(numero)
    print(f"\nTabla del {numero}:")
    for i, resultado in enumerate(tabla, 1):
        print(f"{numero} x {i} = {resultado}")


tabla_multiplicar_interactiva()