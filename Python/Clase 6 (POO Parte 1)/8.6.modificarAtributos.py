# Modificar atributos de un objeto

class Persona: # Creacion de la clase
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre 
        self.apellido = apellido 
        self.edad = edad 

persona1 = Persona("Santiago", "Capitani", 20) 
print(f'El objeto persona1 se llama {persona1.nombre} {persona1.apellido} y tiene {persona1.edad} años.')

persona1.nombre = "Juan" # Modificamos el atributo nombre del objeto persona1
persona1.apellido = "Perez" # Modificamos el atributo apellido del objeto persona1
persona1.edad = 30 # Modificamos el atributo edad del objeto persona1
print(f'El objeto persona1 se llama {persona1.nombre} {persona1.apellido} y tiene {persona1.edad} años.') 