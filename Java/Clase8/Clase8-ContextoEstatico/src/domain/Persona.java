package domain;

public class Persona {
    // Atributos
    private int idPersona;
    private static int contadorPersona = 0;
    private String nombre;

    // Constructor con parámetros
    public Persona(String nombre) {
        contadorPersona++;
        this.idPersona = contadorPersona;
        this.nombre = nombre;
    }

    // Métodos getter
    public int getIdPersona() {
        return this.idPersona;
    }

    public static int getContadorPersona() {
        return contadorPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    // Métodos setter
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    // Método toString
    @Override
    public String toString() {
        return "Persona{" +
                "idPersona=" + idPersona +
                ", nombre='" + nombre + '\'' +
                '}';
    }
}