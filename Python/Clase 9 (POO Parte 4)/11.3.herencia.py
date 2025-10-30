# Tarea: encapsular los atributos y agregar los metodos getters and setters.
# Crear otro objeto, pasar los datos para nombre, edad y sueldo,
# Mostrar estos datos, luego modificar y mostrar nuevamente.

class Persona: #Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self._nombre = nombre # Atributos encapsulados (guion bajo)
        self._edad = edad

    # Getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    # Setters
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @edad.setter
    def edad(self, edad):
        self._edad = edad

class Empleado(Persona): #Esta clase hereda de la clase Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) #Llamamos al constructor de la clase padre
        self._sueldo = sueldo
    
    # Getter y Setter para sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

empleado1 = Empleado("Santiago", 20, 150000)
# Se accede como atributos, sin get_()
print(f'El empleado1 se llama {empleado1.nombre}, tiene {empleado1.edad} años y cobra {empleado1.sueldo} pesos.')

empleado2 = Empleado("Lucía", 25, 200000)
print(f'\nEl empleado2 se llama {empleado2.nombre}, tiene {empleado2.edad} años y cobra {empleado2.sueldo} pesos.')

# Modificamos los datos usando la asignación simple (esto llama a los setters)
print(f'\n--- Modificando datos de empleado2 ---')
empleado2.nombre = "Lucía González"
empleado2.edad = 26
empleado2.sueldo = 220000

# Mostramos nuevamente los datos modificados
print(f'El empleado2 (datos actualizados) se llama {empleado2.nombre}, tiene {empleado2.edad} años y cobra {empleado2.sueldo} pesos.')