from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

raton1 = Raton("HP", "USB")
teclado1 = Teclado("HP", "USB")
monitor1 = Monitor("HP", "15 pulgadas")
computadora1 = Computadora("HP", monitor1, teclado1, raton1)

raton2 = Raton("Acer", "Bluetooth")
teclado2 = Teclado("Acer", "USB")
monitor2 = Monitor("Acer", "27 pulgadas")
computadora2 = Computadora("Acer", monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)

raton3 = Raton("Gamer", "USB")
teclado3 = Teclado("Gamer", "USB")
monitor3 = Monitor("Gamer", "25 pulgadas")
computadora3 = Computadora("Gamer", monitor3, teclado3, raton3)

raton4 = Raton("HP", "Bluetooth")
teclado4 = Teclado("HP", "USB")
monitor4 = Monitor("HP", "17 pulgadas")
computadora4 = Computadora("HP", monitor4, teclado4, raton4)

computadoras2 = [computadora3, computadora4]
orden2 = Orden(computadoras1)
print(orden2)