#Colecciones de Python
# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores
nombres = ["Guido","Vero","Carlos"]
print(nombres)
print(len(nombres))
#agregamos un elemento
nombres.append("Juan")
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)

print(nombres)
print(len(nombres))

#Concatenamos listas
lista1 = [1,2,3]
lista2 = [4,5,6,1]
lista3 = lista1+lista2 #Concatenacion
print(lista3)

lista3.extend([7,8,9,1])#Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(6))#Funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0)) esto daria un error por no ser un elemento que forma parte de la lista

#Como saber cuantos valores hay repetidos en una lista
print(lista3.count(1))#Cuenta cuantos valores iguales hay dentro de la lista

#Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1,2,3] * 2
print(lista)

# Metodos de ordenamiento
lista3.sort()# Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True)
print(lista3)
