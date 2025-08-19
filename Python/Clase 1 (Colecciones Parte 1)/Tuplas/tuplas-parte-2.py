#Definimos una tupla
frutas = ('frutilla', 'manzana', 'mandarina', 'pera') #A diferencia de las listas esta se declara con parentesis
print(frutas)
print(len(frutas)) #Al igual que las listas, len muestra cuantos elementos tiene esta

# Acceder a un elemento, para eso utilizamos corchetes, no parentesis
print(frutas[0])

# Acceder a un rango
print(frutas[0:3])

# Recorremos los elementos de la tupla
for fruta in frutas:
    print(fruta, end=' ') #usamos end= para eliminar los saltos de linea


# frutas[0] = 'naranja'
# print(frutas) #No se puede hacer una modificacion de esta manera en una tupla
# Solo se puede haciendo una conversion de tupla a lista y de lista a tupla

frutasLista = list(frutas)
frutasLista[0] = 'naranja'
frutas = tuple(frutasLista)
print('\n', frutas) #esta conversion no es una buena practica

# En las tuplas no se pueden usar las funciones append, remove y insert

del frutas # Eliminamos la tupla
