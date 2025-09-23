class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura

rectangulos = []  # lista para guardarlos

for i in range(3):
    print(f"\nRectángulo {i + 1}")
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))

    rect = Rectangulo(base, altura)  # se crea el objeto
    rectangulos.append(rect)  # se guarda en la lista

print("\nÁreas de los rectángulos:")
for i, rect in enumerate(rectangulos, start=1):
    print(f"Rectángulo {i}: {rect.calcular_area()}")
