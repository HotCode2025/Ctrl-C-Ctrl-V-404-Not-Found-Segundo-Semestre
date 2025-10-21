class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self,other):    
        return self.nombre + other.nombre

    def __sub__(self, other):  
        return self.edad - other.edad


persona1 = Persona("Hugo", 29)
persona2 = Persona("Dolo", 19)

#imprime la suma de los nombres
print(persona1 + persona2)

#imprime la resta de los años
print(persona1 - persona2)