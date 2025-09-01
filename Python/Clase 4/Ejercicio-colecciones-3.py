
personajes = []

aragorn = {
    "Nombre": "Aragon",
    "Clase": "Guerrero", 
    "Raza": "Dunadan del norte"
}
personajes.append(aragorn)

gandalf = {
    "Nombre": "Gandalf",
    "Clase": "Mago",
    "Raza": "Istar"
}
personajes.append(gandalf)

legolas = {
    "Nombre": "Legolas",
    "Clase": "Arquero", 
    "Raza": "Elfo Sindar"
}
personajes.append(legolas)

# Mostrar todos los personajes
print("=== PERSONAJES DEL SEÑOR DE LOS ANILLOS ===")
print(f"Total de personajes: {len(personajes)}")
print("-" * 40)

for i, personaje in enumerate(personajes, 1):
    print(f"Personaje #{i}:")
    print(f"  Nombre: {personaje['Nombre']}")
    print(f"  Clase:  {personaje['Clase']}")
    print(f"  Raza:   {personaje['Raza']}")
    print()