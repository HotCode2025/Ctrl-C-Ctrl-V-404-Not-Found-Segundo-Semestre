#Tipo Set o conjunto
planetas = {"Marte", "Júpiter", "Venus"}
print(len(planetas)) #Usamos la funcio len = length significa largo

#Revisamos si un elemento existe dentro de set
print("Júpiter" in planetas)

#Agregar un elemento
planetas.add("Tierra")# add es una función
print(planetas)

#Eliminar un elemento, puede arrojar un error si el elemento no existe
planetas.remove("Júpiter")#esta funcion ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard("Tierra")#esta funcion no nos presenta ningun error
print(planetas)

#Limpiar set o conjunto
planetas.clear()
print(planetas)

#Eliminar set o conjunto
#del planetas
print(planetas)