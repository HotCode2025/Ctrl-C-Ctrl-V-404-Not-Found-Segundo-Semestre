# Las tuplas, al igual que las listas, permite almacenar elementos
# y modificarlos en ella, pero no se pueden eliminar elementos, es inmutable

#Definimos una tupla
frutas = ('frutilla', 'manzana', 'mandarina', 'pera') #A diferencia de las listas esta se declara con parentesis
print(frutas)
print(len(frutas)) #Al igual que las listas, len muestra cuantos elementos tiene esta

# Acceder a un elemento, para eso utilizamos corchetes, no parentesis
print(frutas[0])

# Acceder a un rango
print(frutas[0:3])