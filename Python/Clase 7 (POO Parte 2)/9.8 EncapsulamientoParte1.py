class Persona:

    # Todos estos atributos son publicos, quiere decir que se pueden usar fuera de nuestro objeto
    # El encapsulamiento es para que nuestros atributos no puedan ser usar publicamente fuera de nuestra clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): 
        self.nombre = nombre
        self._apellido = apellido
        self._dni = dni # Este atributo esta encapsulado, de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
        # El _ antes del nombre del atributo, es el metodo mas comun de encapsulamiento en python

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self._apellido}, DNI: {self._dni} ,{self.edad} Años, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona("Santiago", "Capitani", 95517828 , 20, 'Telefono', '2615590611', 'Calle Mariano Boedo', 2273, 'Manzana', 'E', 'Casa', 8, Altura=1.73, Peso=70, ColorFavorito='Verde')
# Para acceder al DNI, un atributo encapsulado, necesitamos usar esto
persona1.mostrar_detalle() 
print(persona1._dni)
# Esto va a funcionar igual, porque es una sugerencia en python 
# Pero te das cuenta de que el que usa esto es porque no sabe de la sintaxis de python
# Ese atributo no se deberia ver fuera del objeto