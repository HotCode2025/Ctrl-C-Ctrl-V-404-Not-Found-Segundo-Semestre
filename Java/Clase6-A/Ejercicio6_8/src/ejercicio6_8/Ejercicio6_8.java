package ejercicio6_8;

/**
 * Ejercicio 10: Pedir 10 números y escribir la suma total
 * Hacerlo con la clase Scanner y JOptionPane
 */

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio6_8 {

        public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        double suma = 0;
        double numero;
        
        JOptionPane.showMessageDialog(null, 
            "Bienvenido al ejercicio 6.8", 
            "Suma de 10 numeros", 
            JOptionPane.INFORMATION_MESSAGE);
        System.out.println("=== SUMA DE 10 NÚMEROS ===");
        
        // Pido 10 números con Scanner (consola)
        System.out.println("\n--- Ingresando números por consola ---");
        for (int i = 1; i <= 10; i++) {
            System.out.print("Ingrese el número " + i + ": ");
            numero = scanner.nextDouble();
            suma = suma + numero;  // suma += numero;
        }
        
        System.out.println("\nLa suma total de los 10 números es: " + suma);
        
        // Reinicio suma para la segunda parte
        suma = 0;
        
        // Pido 10 números con JOptionPane (ventanas)
        System.out.println("\n--- Ahora ingresando números por ventanas ---");
        for (int i = 1; i <= 10; i++) {
            String numeroStr = JOptionPane.showInputDialog(null, 
                "Ingrese el número " + i + " de 10:", 
                "Suma de Números", 
                JOptionPane.QUESTION_MESSAGE);
            
            numero = Double.parseDouble(numeroStr);
            suma = suma + numero;
        }
        
        // Muestro resultado final con JOptionPane
        JOptionPane.showMessageDialog(null, 
            "La suma total de los 10 números es: " + suma, 
            "Resultado Final", 
            JOptionPane.INFORMATION_MESSAGE);
        
        scanner.close();
    }
    
}
