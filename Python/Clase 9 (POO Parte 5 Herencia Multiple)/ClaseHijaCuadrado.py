from ClasePadreColor import Color
from ClasePadreFiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super.__init__(lado) # super. se refiere a la primera clase padre que es FiguraGeometrica
        FiguraGeometrica.__init__(self, lado, lado)  # Llamada explicita a el constructor de la clase padre FiguraGeometrica
        Color.__init__(self, color)  # Llamada explicita a el constructor de la clase padre Color

    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'