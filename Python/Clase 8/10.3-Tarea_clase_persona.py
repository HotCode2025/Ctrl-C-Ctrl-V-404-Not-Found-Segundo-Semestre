class Animal:
    def __init__(self, nombre, especie, edad):
        self._nombre = nombre
        self._especie = especie
        self._edad = edad
        self._peso = None 

    def mostrar_detalles(self):
        print(f"Nombre: {self._nombre}, Especie: {self._especie}, Edad: {self._edad}, Peso: {self._peso if self._peso is not None else 'No especificado'} kg")

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre   

    @property
    def especie(self):      
        return self._especie    
    
    @especie.setter
    def especie(self, especie): 
        self._especie = especie


    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad       

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

# Crear una instancia de Animal
animal1 = Animal("Firulais", "Perro", 5)    
animal1.mostrar_detalles()
animal1.peso = 20.5
animal1.mostrar_detalles()
print(animal1.nombre)  # Usando el getter
animal1.edad = 6
print(animal1.edad)  # Usando el getter
print(animal1.peso)  # Usando el getter


class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    def mostrar_detalles(self):
        print(f"Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._anio}")

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio

# Crear una instancia de Vehiculo
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo1.mostrar_detalles()    
vehiculo1.anio = 2021
print(vehiculo1.anio)  # Usando el getter
print(vehiculo1.marca)  # Usando el getter
print(vehiculo1.modelo)  # Usando el getter
vehiculo1.modelo = "Camry"
vehiculo1.mostrar_detalles()    
vehiculo1.marca = "Honda"
print(vehiculo1.marca)  # Usando el getter  
vehiculo1.mostrar_detalles()
vehiculo1.modelo = "Civic"
print(vehiculo1.modelo)  # Usando el getter
vehiculo1.mostrar_detalles()
vehiculo1.anio = 2022
print(vehiculo1.anio)  # Usando el getter
vehiculo1.mostrar_detalles()