package test;

import domain.Persona;

public class PersonaPrueba {

    private int contador = 0;
    public static void main(String[] args) {
        System.out.println("=== Pruebas de la clase Persona ===");

        // Mostrar contador inicial
        System.out.println("Contador inicial de personas: " + Persona.getContadorPersona());

        // Crear primera persona
        Persona persona1 = new Persona("Juan");
        System.out.println("\nSe creó: " + persona1);
        System.out.println("Contador después de crear persona1: " + Persona.getContadorPersona());

        // Crear segunda persona
        Persona persona2 = new Persona("María");
        System.out.println("\nSe creó: " + persona2);
        System.out.println("Contador después de crear persona2: " + Persona.getContadorPersona());

        // Crear tercera persona
        Persona persona3 = new Persona("Carlos");
        System.out.println("\nSe creó: " + persona3);
        System.out.println("Contador después de crear persona3: " + Persona.getContadorPersona());

        PersonaPrueba prueba = new PersonaPrueba();
        System.out.println("Contador desde instancia de prueba: " + prueba.getContador());
       
    }

    public void imprimir (Persona persona) {
        System.out.println("Persona: " + persona);
    }

    public int getContador() {
        imprimir(new Persona("Liliana"));
        return this.contador;
    }
}