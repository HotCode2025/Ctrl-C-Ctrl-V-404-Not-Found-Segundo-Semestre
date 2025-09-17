class Persona: 
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre 
        self.apellido = apellido 
        self.edad = edad 

persona1 = Persona("Gustavo", "Martinez", 30) 
print(f'El objeto persona1 se llama {persona1.nombre} {persona1.apellido} y tiene {persona1.edad} años.')

persona2 = Persona("Hugo", "Capi", 40)
print(f'El objeto persona2 se llama {persona2.nombre} {persona2.apellido} y tiene {persona2.edad} años.') 