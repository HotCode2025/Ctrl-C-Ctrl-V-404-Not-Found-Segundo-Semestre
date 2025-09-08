def imprimir_descendente(numero):
    # Si es negativo, no imprime nada
    if numero < 1:
        return

    # Imprime el número actual
    print(numero)

    # Llama recursivamente con el número anterior
    imprimir_descendente(numero - 1)


# Ejemplos:
print("Ejemplo con 5:")
imprimir_descendente(5)

print("\nEjemplo con 3:")
imprimir_descendente(3)

print("\nEjemplo con número negativo (-2):")
imprimir_descendente(-2)  # No imprime nada