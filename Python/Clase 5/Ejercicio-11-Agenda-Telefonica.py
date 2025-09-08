def agenda_telefonica():
    contactos = {}
    
    while True:
        print("\n" + "=" * 30)
        print("      AGENDA TELEFÓNICA")
        print("=" * 30)
        print("1. Nuevo contacto")
        print("2. Borrar contacto")
        print("3. Ver contactos existentes")
        print("4. Salir")
        print("=" * 30)
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        # Opción 1: Nuevo contacto
        if opcion == "1":
            print("\n--- NUEVO CONTACTO ---")
            nombre = input("Ingrese el nombre: ").strip()
            
            if not nombre:
                print("Error: El nombre no puede estar vacío.")
                continue
                
            if nombre in contactos:
                print(f"Error: El contacto '{nombre}' ya existe.")
                continue
                
            telefono = input("Ingrese el teléfono: ").strip()
            if not telefono:
                print("Error: El teléfono no puede estar vacío.")
                continue
                
            contactos[nombre] = telefono
            print(f"✓ Contacto '{nombre}' agregado exitosamente.")
        
        # Opción 2: Borrar contacto
        elif opcion == "2":
            print("\n--- BORRAR CONTACTO ---")
            
            if not contactos:
                print("La agenda está vacía.")
                continue
                
            nombre = input("Ingrese el nombre del contacto a borrar: ").strip()
            
            if nombre in contactos:
                confirmar = input(f"¿Está seguro de borrar a '{nombre}'? (s/n): ").lower()
                if confirmar == 's':
                    del contactos[nombre]
                    print(f"✓ Contacto '{nombre}' eliminado exitosamente.")
                else:
                    print("Operación cancelada.")
            else:
                print(f"Error: El contacto '{nombre}' no existe.")
        
        # Opción 3: Ver contactos existentes
        elif opcion == "3":
            print("\n--- CONTACTOS EXISTENTES ---")
            
            if not contactos:
                print("No hay contactos en la agenda.")
            else:
                print(f"{'Nombre':<20} {'Teléfono':<15}")
                print("-" * 35)
                for nombre, telefono in sorted(contactos.items()):
                    print(f"{nombre:<20} {telefono:<15}")
                print(f"\nTotal de contactos: {len(contactos)}")
        
        # Opción 4: Salir
        elif opcion == "4":
            print("¡Gracias por usar la agenda telefónica! ")
            break
        
        else:
            print("Error: Opción no válida. Por favor elija 1-4.")

# Ejecutar el programa
if __name__ == "__main__":
    agenda_telefonica()