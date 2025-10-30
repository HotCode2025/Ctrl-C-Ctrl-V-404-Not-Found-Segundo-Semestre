from ClasePadreColor import Color
from ClasePadreFiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica, Color):
   def __init__(self, ancho, alto, color):
         FiguraGeometrica.__init__(self, ancho, alto) # Llamada explicita a el constructor de la clase padre FiguraGeometrica
         Color.__init__(self, color) # Llamada explicita a el constructor de la clase padre Color
         
   def calcular_area(self): # Calcula el área del rectángulo
         return self.alto * self.ancho

   def __str__(self): # Representación en cadena del rectángulo
         return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'       