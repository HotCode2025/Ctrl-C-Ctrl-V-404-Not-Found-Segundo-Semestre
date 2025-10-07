public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("=== Probando la clase Persona ===\n");

        // Crear una persona usando el constructor vacío
        Persona persona1 = new Persona();

        // Establecer valores usando los setters
        persona1.setNombre("Juan Pérez");
        persona1.setSueldo(500.000);
        persona1.setEliminado(false);

        // Mostrar información usando los getters
        System.out.println("Persona 1:");
        System.out.println("Nombre: " + persona1.getNombre());
        System.out.println("Sueldo: $" + persona1.getSueldo());
        System.out.println("Eliminado: " + persona1.isEliminado());
        System.out.println();

        System.out.println("persona1: " + persona1);

        // Crear una segunda persona usando el constructor con parámetros
        Persona persona2 = new Persona("María García", 750.000, false);

        System.out.println("Persona 2:");
        System.out.println("Nombre: " + persona2.getNombre());
        System.out.println("Sueldo: $" + persona2.getSueldo());
        System.out.println("Eliminado: " + persona2.isEliminado());
        System.out.println();

        // Modificar algunos valores de la persona2
        persona2.setSueldo(800.000);
        persona2.setEliminado(true);

        System.out.println("Persona 2 (después de modificaciones):");
        System.out.println("Nombre: " + persona2.getNombre());
        System.out.println("Sueldo: $" + persona2.getSueldo());
        System.out.println("Eliminado: " + persona2.isEliminado());
        System.out.println();

        // Crear una tercera persona para probar diferentes casos
        Persona persona3 = new Persona("Carlos López", 450.000, true);

        System.out.println("Persona 3:");
        System.out.println("Nombre: " + persona3.getNombre());
        System.out.println("Sueldo: $" + persona3.getSueldo());
        System.out.println("¿Está eliminado? " + (persona3.isEliminado() ? "Sí" : "No"));
    }
}
