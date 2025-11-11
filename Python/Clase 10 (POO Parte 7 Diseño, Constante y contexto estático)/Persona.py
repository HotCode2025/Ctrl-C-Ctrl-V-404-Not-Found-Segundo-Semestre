class Persona:
    contador_personas = 0 # Variable de clase
    
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas+= 1
        return cls.contador_personas
    
    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad
    
    def _str__(self):
        return f'Persona [{self.id_persona}{self.nombre}{self.edad}]'
      
persona1 = Persona('Santiago', 20)
print(persona1)
persona2 = Persona('Juan', 30)        
print(persona2)
persona3 = Persona('Pepe', 18)     
print(persona3)
Persona.generar_siguiente_valor()
persona4= Persona('Rodrigo', 24)
print(persona4)
print(f'Valor del contador de personas: {Persona.contador_personas}')
        
