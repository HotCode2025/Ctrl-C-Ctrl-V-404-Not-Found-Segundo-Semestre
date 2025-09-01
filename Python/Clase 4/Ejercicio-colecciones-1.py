def eliminar_repetidos(lista):
    
    lista_sin_repetidos = []
    for elemento in lista:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)
    return lista_sin_repetidos

mi_lista = [1, 2, 3, 2, 4, 1, 5, 3, 6, 7, 5]

print("Lista original:")
print(mi_lista)

lista_sin_repetidos = eliminar_repetidos(mi_lista)

print("\nLista sin elementos repetidos:")
print(lista_sin_repetidos)