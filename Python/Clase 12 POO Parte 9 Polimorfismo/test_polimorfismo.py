from empleado import Empleado
from gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado("Ariel", 40000)
imprimir_detalles(empleado)


gerente = Gerente("Sistemas", "Natalia", 80000)
imprimir_detalles(gerente)

