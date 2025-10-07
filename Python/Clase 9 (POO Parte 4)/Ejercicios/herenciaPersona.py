# Tarea: encapsular los atributos y agragar los metodos getters and setters.
# Crear otro objeto, pasar los datos para nombre, edad y sueldo,
# Mostrar estos datos, luego modificar y mostrar nuevamente.

class Persona:  # Esta clase hereda de la clase Object
    def __init__(self, nomrbre, edad):
        self._nombre = nomrbre  # Atributos encapsulados (guion bajo)
        self._edad = edad

    # Getter
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    # Setter
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_edad(self, edad):
        self._edad = edad

    def __str__(self):
        return "\n"f"Persona: [Nombre: {self._nombre}, Edad: {self._edad} ]"

class Empleado(Persona):  # Esta clase hereda de la clase Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase padre
        self._sueldo = sueldo

    # Getter
    def get_sueldo(self):
        return self._sueldo

    # Setter
    def set_sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f"Empleado: [ Sueldo: {self._sueldo}] {super().__str__()}"

empleado1 = Empleado("Santiago", 20, 150000)
print(
    f'El empleado1 se llama {empleado1.get_nombre()}, tiene {empleado1.get_edad()} años y cobra {empleado1.get_sueldo()} pesos.')

empleado2 = Empleado("Lucía", 25, 200000)
print(
    f'\nEl empleado2 se llama {empleado2.get_nombre()}, tiene {empleado2.get_edad()} años y cobra {empleado2.get_sueldo()} pesos.')

# Modificamos los datos usando los setters
empleado2.set_nombre("Lucía González")
empleado2.set_edad(26)
empleado2.set_sueldo(220000)

# Mostramos nuevamente los datos modificados
print(f'\nDespués de la modificación:')
print(
    f'El empleado2 se llama {empleado2.get_nombre()}, tiene {empleado2.get_edad()} años y cobra {empleado2.get_sueldo()} pesos.')