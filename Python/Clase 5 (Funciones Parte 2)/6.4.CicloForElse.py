numbers = [1, 2, 3, 4, 5]

for nunmber in numbers:
    print(nunmber)
    if nunmber == 3:
        print('Se encontro el 3!')
        break # Sale del ciclo for
else:
    print('Esto se termina cuando se acaban los elementos de la lista')