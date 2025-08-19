nombres = ['Santiago', 'Pablo', 'Rocio', 'Hugo']
print(nombres)
print(nombres[0:2]) #Solo muestra el indice 0 y 1. Solo 2.
print(nombres[ :3]) #Solo muestra los 3 primeros indices
print(nombres[1: ]) #Empiezo desde el indice 1 hasta el final

#Modificar un valor de una lista
nombres[2] = 'Delfina'
nombres[0] = 'Guido'
print(nombres)

#Iterar una lista, recorre los elementos de la lista
for nombre in nombres: 
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Para ver cuantos elementos tiene una lista, le pasamos el parametro len
print(len(nombres))

# Agregamos un elemento
nombres.append('Dolores')
print(nombres)

# Insertamos un elemento en un indice especifico
# El parametro insert necesita 2 valores, un numero entero del indice y un elemento
nombres.insert(1, 'Stefano')
print(nombres)
nombres.insert(3, 'Gonzalo')
print(nombres)

# Eliminamos el elemento
nombres.remove('Pablo')
print(nombres)

# Eliminar el ultimo elemento (default last)
nombres.pop()
print(nombres)

# Eliminamos un indice especifico
del nombres[2]
print(nombres)

# Eliminar todos los elementos
nombres.clear()
print(nombres)

# Eliminar una lista
del nombres
print(nombres) #Error, nombres no esta definida            