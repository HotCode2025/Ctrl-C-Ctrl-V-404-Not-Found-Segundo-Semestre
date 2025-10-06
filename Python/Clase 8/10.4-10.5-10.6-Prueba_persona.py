# Importar usando importlib para archivos con nombres especiales
import importlib.util
import sys

# Cargar el módulo
spec = importlib.util.spec_from_file_location("persona2_module", "10.1-10.2-Persona2.py")
persona2_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(persona2_module)

# Obtener la clase
Persona2 = persona2_module.Persona2

print('Creacion de objetos'.center(30, '-'))

if __name__ == "__main__":

    persona2 = Persona2("Juan", "Perez", 30)
    persona2.mostrar_detalles()

    print(__name__)

print('Eliminacion de objetos'.center(30, '-'))

del persona2