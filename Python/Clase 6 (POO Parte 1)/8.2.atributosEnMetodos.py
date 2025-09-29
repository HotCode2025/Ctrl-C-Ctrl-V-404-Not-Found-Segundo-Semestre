# Atributos en métodos y creación de un objeto

class Persona: # Creacion de la clase
    def __init__(self): # Método constructor de atributos, self es el parametro por default
        self.nombre = "Juan" # Atributo nombre
        self.apellido = "Perez" # Atributo apellido
        self.edad = 30 # Atributo edad 

persona1 = Persona() # Creacion del objeto persona1 de la clase Persona
print(persona1.nombre) # Acceso al atributo nombre del objeto persona1
print(persona1.apellido) # Acceso al atributo apellido del objeto persona1
print(persona1.edad) # Acceso al atributo edad del objeto persona1