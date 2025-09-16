package com.mycompany.mavenproject1;

// Clase principal
public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); // llamamos al constructor
        persona1.nombre = "Delfina";
        persona1.apellido = "Mulinetti";
        persona1.obtenerinformacion();

        Persona persona2 = new Persona();
        System.out.println ("persona2 = "+ persona2);
        System.out.println ("persona1 = "+ persona1);
        persona2.obtenerinformacion();
        persona2.nombre = "Hector";
        persona2.apellido = "Mulinetti";
        persona2.obtenerinformacion();
    }
}
