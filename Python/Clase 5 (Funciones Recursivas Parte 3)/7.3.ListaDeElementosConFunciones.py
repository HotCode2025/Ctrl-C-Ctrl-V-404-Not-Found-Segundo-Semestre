# Lista de elementos con funciones (convertir)
# Función que convierte una lista de elementos aplicando una función a cada elemento    

def desplegarNombres (nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Ana', 'Pedro']
desplegarNombres(nombres)
desplegarNombres('Carla') # También funciona con strings
#desplegarNombres(10) # Error, int no es iterable
desplegarNombres((10, 11)) # Funciona con tuplas, si es un solo elemeto poner una coma (10,)
desplegarNombres([12, 13]) # Funciona con listas