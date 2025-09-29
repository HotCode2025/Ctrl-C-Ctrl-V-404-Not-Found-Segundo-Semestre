# Metodos de instancia, definimos un metodo

class Persona: # Creacion de la clase
    def __init__(self, nombre, apellido, edad): 
        self.nombre = nombre 
        self.apellido = apellido 
        self.edad = edad 
    
    def mostrar_detalle(self): # Metodo de instancia
        print(f"La clase Persona tiene los siguientes atributos: {self.nombre} {self.apellido} {self.edad}") 
        # El metodo de instancia siempre debe tener el parametro self        

persona1 = Persona("Santiago", "Capitani", 20)
print(f'El objeto persona1 se llama {persona1.nombre} {persona1.apellido} y tiene {persona1.edad} años.')

persona1.mostrar_detalle() # Llamado al metodo de instancia