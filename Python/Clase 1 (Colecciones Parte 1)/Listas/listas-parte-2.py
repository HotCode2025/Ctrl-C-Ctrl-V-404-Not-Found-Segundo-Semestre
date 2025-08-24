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