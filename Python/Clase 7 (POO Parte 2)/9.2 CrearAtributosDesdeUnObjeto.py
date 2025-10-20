class Persona: 
    def __init__(self, nombre, apellido, edad): 
        self.nombre = nombre 
        self.apellido = apellido 
        self.edad = edad 
    
    def mostrar_detalle(self): 
        print(f"La clase Persona tiene los siguientes atributos: {self.nombre} {self.apellido} {self.edad}")     

persona1 = Persona("Santiago", "Capitani", 20)
print(f'El objeto persona1 se llama {persona1.nombre} {persona1.apellido} y tiene {persona1.edad} años.')

persona1.mostrar_detalle() 

persona1.telefono = '261234534'
print(f'Este es el telefono de {persona1.nombre}: {persona1.telefono}') # Hemos creado un atributo de un objeto