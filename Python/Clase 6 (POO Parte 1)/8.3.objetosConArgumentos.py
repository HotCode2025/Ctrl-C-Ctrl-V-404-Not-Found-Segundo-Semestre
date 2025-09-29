# Como crear un objeto con argumentos en POO

class Persona: # Creacion de la clase
    def __init__(self, nombre, apellido, edad): # Método constructor de atributos con argumentos
        self.nombre = nombre 
        self.apellido = apellido 
        self.edad = edad 

persona1 = Persona("Santiago", "Capitani", 20) # Creacion del objeto persona1 de la clase Persona con argumentos
print(persona1.nombre) 
print(persona1.apellido) 
print(persona1.edad) 

