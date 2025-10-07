public class Persona {
    // Propiedades privadas
    private String nombre;
    private double sueldo;
    private boolean eliminado;

    // Constructor vacío
    public Persona() {
    }

    // Constructor con parámetros
    public Persona(String nombre, double sueldo, boolean eliminado) {
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }

    // Métodos getter y setter para nombre
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    // Métodos getter y setter para sueldo
    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public double getSueldo() {
        return sueldo;
    }

    // Métodos getter y setter para eliminado
    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public String toString() {
        return "Persona[nombre=" + nombre + ", sueldo=" + sueldo + ", eliminado=" + eliminado + "]";
    }
}