package test;

import test.domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDNI = 38108388;
        System.out.println("DNI: " + miDNI);
        //miDNI = 12345678; No se puede modificar una variable final

        //Persona.CONSTANTE_AQUI = 20; // No se puede modificar una constante final   
        System.out.println("Constante: " + Persona.CONSTANTE_AQUI);

        final Persona persona1 = new Persona();
        //persona1 = new Persona(); // No se puede reasignar una referencia final
        persona1.setNombre("Stefano Aymar");
        System.out.println("Nombre: " + persona1.getNombre());
        persona1.setNombre("Liliana Gomez");
        System.out.println("Nombre2: " + persona1.getNombre());
    }
}
