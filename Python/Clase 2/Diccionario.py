# "Maradona" : 10 un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    "IDE":"Integrated Devalopment Enviroment",
    "POO":"Programación Orientada a Objetos",
    "SABD":"Sistema de Administración de Base de Datos"
}
#Verificamos la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave (key)
print(diccionario["SABD"])

#otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("IDE"))

#Modificamos el elemento
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)

#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#   Otras maneras de acceder a nnuestro diccionario
for termino in diccionario.keys(): # EStamos usando una funcion
    print(termino) #Muestra solo las llaves


for valor in diccionario.values(): #Usamos una fucion para acceder al valor
    print(valor) #vemos solamente los valores

#Comprobamos la existencia de algun elemento
print("IDE" in diccionario) #Devuelve un booleano

#Agregar un elemento al diccioario
diccionario["PK"] = "Primary key"
print(diccionario)

#Eliminamos un elemento
diccionario.pop("SABD")
print(diccionario)

#   Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar el diccionario
#del diccionario
print(diccionario)