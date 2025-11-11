class MiClase:
    
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
    # Metodo static, se asocia a la clase
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
     
    # Metodo de clase    
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
        
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)
        
print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

# Creacion de variables de clase
MiClase.variable_clase2 = "Valor de variable de clase 2"
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

# Muestra el metodo estatico
MiClase.metodo_estatico()

# Muestra el metodo de clase
MiClase.metodo_clase()

miObjeto1 = MiClase('variable de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()