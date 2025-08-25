#Colas con listas
#FIFO (first input / first output)

cola = ['Ariel', 'Stefano', ' Hugo', 'Guido']

#Agregamos un elemento al final de la cola

cola.append('Capi')
print(cola)

#Sacamos elementos de la cola

elementoEliminado = cola.pop(0)
print(cola)
print(f'El elemento quitado de la cola es: {elementoEliminado}')