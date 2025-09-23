def caracteres_sin_repetir_set():
    cadena = input("Ingrese una cadena de texto: ")
    
    caracteres_unicos = list(set(cadena))
    
    return caracteres_unicos

resultado = caracteres_sin_repetir_set()
print("Caracteres únicos:", resultado)