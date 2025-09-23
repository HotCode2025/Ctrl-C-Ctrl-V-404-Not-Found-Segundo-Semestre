# Desemoaquetado de listas o list Unpacking

def show(name, lastname):
    print(name + ' ' + lastname)

persona = ['Juan', 'Perez']

show(persona[0], persona[1]) # Forma tradicional de parar los datos de la lista a la funcion
show(*persona) # Desempaquetado de la lista con el asterisco

persona2 = ('Carlos', 'Guiterrez')
show(*persona2) # Funciona igual con tuplas

persona3 = {"lastname": "Gomez", "name": "Ana"}
show(**persona3) # Desempaquetado de diccionarios con doble asterisco

