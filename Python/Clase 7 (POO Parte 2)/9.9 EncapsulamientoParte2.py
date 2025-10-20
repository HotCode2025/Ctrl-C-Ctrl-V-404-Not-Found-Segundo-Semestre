# Encapsulamiento Parte 2

class Persona:

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): 
        self.__nombre = nombre # Es otra anotacion en python, para evitar que sea modificado
        self._apellido = apellido
        self._dni = dni # Este atributo esta encapsulado, de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
        # El _ antes del nombre del atributo, es el metodo mas comun de encapsulamiento en python
        # El __ antes del nombre del atributo, es para evitar que ese atributo sea modificado
        # es la manera de encapsular estrictamente
    def mostrar_detalle(self):
        print(f'Persona: {self.__nombre} {self._apellido}, DNI: {self._dni} ,{self.edad} Años, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona("Santiago", "Capitani", 95517828 , 20, 'Telefono', '2615590611', 'Calle Mariano Boedo', 2273, 'Manzana', 'E', 'Casa', 8, Altura=1.73, Peso=70, ColorFavorito='Verde')
# Para acceder al DNI, un atributo encapsulado, necesitamos usar esto
persona1.mostrar_detalle() 
# Tampoco se puede motrar porque nombre esta encapsulado con __, es una encapsulación estricta

# persona1.__nombre # Esta totalmente encapsulado