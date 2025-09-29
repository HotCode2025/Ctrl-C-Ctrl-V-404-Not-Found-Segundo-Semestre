#Creamos más objetos en una clase

class Persona: # Creacion de la clase
    def __init__(self, nombre, apellido, edad): # Método constructor de atributos con argumentos
        self.nombre = nombre 
        self.apellido = apellido 
        self.edad = edad 

persona1 = Persona("Santiago", "Capitani", 20) # Creacion del objeto persona1 de la clase Persona con argumentos
print(f'El objeto persona1 se llama {persona1.nombre} {persona1.apellido} y tiene {persona1.edad} años.')

persona2 = Persona("Juan", "Perez", 30)
print(f'El objeto persona2 se llama {persona2.nombre} {persona2.apellido} y tiene {persona2.edad} años.') #Acceso a todos los atributos con interpolacion de cadenas 