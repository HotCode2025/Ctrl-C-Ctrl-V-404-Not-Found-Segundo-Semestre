#Ejercicio 8: Menú interactivo - Cajero automático
#Hacer un programa que simule un cajero automático con un saldo
#inicial de $1000 y tendrá el sgte menu de opciones:
#           1.Ingresar dinero en la cuenta
#           2.Retirar dinero de la cuenta
#           3.Mostrar dinero de la cuenta
#           4.Salir

def menu():
    print("Bienvenidos al cajero automático del Banco Program!")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero de la cuenta")
    print("4. Salir")

def cajero():
    saldo = 1000  # saldo inicial
    opcion = 0
    saldo_final = 0

    while opcion != 4:
        menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            aporte = int(input("Importe a ingresar: "))
            saldo_final = saldo + aporte
            print(f"Se ingresaron ${aporte}. Saldo actual: ${saldo_final}")
        elif opcion == 2:
            retiro = int(input("Importe a retirar: "))
            if retiro > saldo_final:
                print("Fondos insuficientes.")
            else:
                saldo_final = saldo_final - retiro
                print(f"Se retiraron ${retiro}. Saldo actual: ${saldo_final}")
        elif opcion == 3:
            print(f"Saldo disponible: ${saldo_final}")
        elif opcion == 4:
            print("Gracias por utilizar los servicios del Banco Program!")
        else:
            print("Opción no válida. Intente nuevamente.")


cajero()

