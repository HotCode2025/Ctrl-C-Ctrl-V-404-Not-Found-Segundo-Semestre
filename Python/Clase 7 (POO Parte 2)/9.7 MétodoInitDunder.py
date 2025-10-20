class Persona:

    def __init__(self, nombre, apellido, edad, *args, **kwargs): # Se lo llama método Init Dunder
        # *args es para poder pasar tuplas, siempre se pone primero el de
        # **kwargs es para diccionarios
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs


    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} Años, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona("Santiago", "Capitani", 20, 'Telefono', '2615590611', 'Calle Mariano Boedo', 2273, 'Manzana', 'E', 'Casa', 8, Altura=1.73, Peso=70, ColorFavorito='Verde')

persona1.mostrar_detalle() 