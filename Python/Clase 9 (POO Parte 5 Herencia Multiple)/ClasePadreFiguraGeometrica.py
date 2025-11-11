class FiguraGeometrica:
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho):
            self._ancho = ancho
        if self._validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print("Valor de alto no válido, se asigna 0")

    # Getter Ancho
    @property
    def ancho(self):
        return self._ancho
    # Setter Ancho
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho

    # Getter Alto
    @property
    def alto(self):
        return self._alto
    
    # Setter Alto
    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):
            self._alto = alto

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self.ancho}, Alto: {self.alto}]'
    
    def _validar_valores(self, valor): # Metodo encapsulado
        return True if 0 < valor < 10 else False