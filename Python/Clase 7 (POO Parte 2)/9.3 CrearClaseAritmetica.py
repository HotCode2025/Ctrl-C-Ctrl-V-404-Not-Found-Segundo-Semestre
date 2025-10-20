# Crear clase Aritmetica (sumar)

class Aritmetica:
    """
    
    El nombre de este tipo de comentario es : DocString
    esot es documentacion de la clase en python
    En esta clase vamos a hacer algunas operaciones de suma, resta, multiplicacion y mas
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB
    
    # Método para restar
    def resta(self):
        return self.operandoA - self.operandoB
    
    # Método para multiplicar
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    # Método para dividir
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(10, 4)
print(f'La suma de los números es: {aritmetica1.sumar()}')
print(f'La resta de los números es: {aritmetica1.resta()}')
print(f'La multiplicacion de los números es: {aritmetica1.multiplicar()}')
print(f'La division de los números es: {aritmetica1.dividir():.2f}')

