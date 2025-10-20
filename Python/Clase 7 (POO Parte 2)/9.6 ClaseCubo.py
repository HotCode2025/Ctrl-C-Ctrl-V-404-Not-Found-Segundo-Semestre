# Creamos la clase: Cubo

class Cubo:

    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad
        print(f"Se ha creado un cubo con medidad: {self.ancho}x{self.altura}x{self.profundidad}")

    # Funcion que calcula el volumen
    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad 

print("--- Creacion del Cubo ---")
ancho_input = int(input("Digite el valor del ancho: "))
altura_input = int(input("Digite el valor de la altura: "))
profundidad_input = int(input("Digite el valor de la profundidad: "))

cubo1 = Cubo(ancho_input, altura_input, profundidad_input)

volumen_calculado = cubo1.calcular_volumen()

print(f'El volumen del cubo es {volumen_calculado}')   