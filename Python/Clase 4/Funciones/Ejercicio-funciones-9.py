def eliminar_espacios(frase):
#Elimina todos los espacios de una frase
    return frase.replace(" ", "")


def contar_caracteres_sin_espacios(frase):
#     Cuenta los caracteres excluyendo espacios
    frase_sin_espacios = eliminar_espacios(frase)
    return len(frase_sin_espacios)


def main():
    # Solicitar frase al usuario
    frase = input("Ingresa una frase: ")

    # Procesar con las funciones
    frase_final = eliminar_espacios(frase)
    cantidad = contar_caracteres_sin_espacios(frase)

    # Mostrar resultados
    print(f"Frase original: '{frase}'")
    print(f"Frase final: {frase_final}")
    print(f"N° de caracteres (sin espacios): {cantidad}")


# Ejecutar el programa
if __name__ == "__main__":
    main()