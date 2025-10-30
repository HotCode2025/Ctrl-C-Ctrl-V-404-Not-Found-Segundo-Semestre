class Color:
    def __init__(self, color):
        self.color = color

    # Getter Color
    @property
    def color(self):
        return self._color
    
    # Setter Color
    @color.setter       
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'Color: {self.color}'   