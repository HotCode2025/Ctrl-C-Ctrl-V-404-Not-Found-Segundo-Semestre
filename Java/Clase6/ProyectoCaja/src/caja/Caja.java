package caja;

/**
 * Clase Caja que representa una caja con dimensiones
 */

public class Caja {
    // Atributos de la clase
    public double ancho;
    public double alto;
    public double profundidad;
    
    // Constructor vacío
    public Caja() {
        this.ancho = 0.0;
        this.alto = 0.0;
        this.profundidad = 0.0;
    }
    
    // Constructor con argumentos
    public Caja(double ancho, double alto, double profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    
    // Método para calcular el volumen
    public double calcularVolumen() {
        return ancho * alto * profundidad;
    }
}