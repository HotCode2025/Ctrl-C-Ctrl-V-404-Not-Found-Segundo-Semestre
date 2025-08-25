seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': '35', 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    7: {'Nombre': 'Angel Di Maria', 'Edad': '34', 'Altura': 1.80, 'Precio': '20 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': '28', 'Altura': 1.77, 'Precio': '33 Millones', 'Posicion': 'Media Punta'},
    17: {'Nombre': 'Nicolas Otamendi', 'Edad': '34', 'Altura': 1.70, 'Precio': '3 Millones', 'Posicion': 'Defensor Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': '35', 'Altura': 1.70, 'Precio': '3 Millones', 'Posicion': 'Arquero'},
}

seleccionArgentina[5]= {'Nombre': 'Leandro Paredes', 'Edad': '31', 'Altura': 1.80, 'Precio': '5 Pesos', 'Posicion': 'Mediocampista central'}
seleccionArgentina[13]= {'Nombre': 'Cuti Romero', 'Edad': '27', 'Altura': 1.85, 'Precio': '50 Millones', 'Posicion': 'Defensor Central'}
seleccionArgentina[3]= {'Nombre': 'Marcos Acuña', 'Edad': '33', 'Altura': 1.72, 'Precio': '2 Millones', 'Posicion': 'Defensor Izquierdo'}
seleccionArgentina[8]= {'Nombre': 'Enzo Fernandez', 'Edad': '24', 'Altura': 1.78, 'Precio': '75 Millones', 'Posicion': 'Mediocampista central'}


for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print(len(seleccionArgentina))