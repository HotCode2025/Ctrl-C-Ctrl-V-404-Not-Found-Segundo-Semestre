# Argumentos variables para un diccionario

def listarTerminos(**kwargs): # El doble asterisco permite recibir un numero variable de argumentos nombrados (clave=valor)
    for clave, valor in kwargs.items(): # Itera sobre los pares clave-valor del diccionario
        print(f'{clave} : {valor}')

listarTerminos(IDE='Integrated Development Environment', PK='Primary Key', DBMS='Database Management System') # Llamada a la función con argumentos nombrados
