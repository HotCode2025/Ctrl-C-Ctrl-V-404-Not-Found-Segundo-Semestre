class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}")

    @property
    def nombre(self): #Metodo getter
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre): #Metodo setter
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    
    # @edad.setter
    # def edad(self, edad):
    #     if edad >= 0:
    #         self._edad = edad
    #     else:
    #         raise ValueError("La edad no puede ser negativa")

    def __del__(self):
        print(f"El objeto {self._nombre} {self._apellido} ha sido eliminado")

if __name__ == "__main__":
    persona1 = Persona2("Juan", "Perez", 30)
    persona1.mostrar_detalles()
    print(persona1.nombre)  # Usando el getter
    persona1.edad = 55

    #Atributo de solo lectura porque no tiene setter
    print(persona1.edad)  # Usando el getter