package caja;

import java.util.Scanner;
import javax.swing.JOptionPane;

/**
 * Clase PruebaCaja para probar la funcionalidad de la clase Caja
 * Utiliza Scanner y JOptionPane para entrada de datos
 */
public class PruebaCaja {
    
    public static void main(String[] args) {
        // Crear objeto Scanner para entrada por consola
        Scanner scanner = new Scanner(System.in);
        
        // Mostrar mensaje de bienvenida
        System.out.println("=== PROGRAMA DE CÁLCULO DE VOLUMEN DE CAJAS ===");
        JOptionPane.showMessageDialog(null, 
            "Bienvenido al programa de cálculo de volumen de cajas", 
            "Cálculo de Volumen", 
            JOptionPane.INFORMATION_MESSAGE);
        
        // OBJETO 1: Usando constructor vacío
        System.out.println("\n--- CAJA 1 (Constructor vacío) ---");
        Caja caja1 = new Caja(); // Constructor vacío
        
        // Solicito datos para la primera caja usando Scanner
        System.out.print("Ingrese el ancho de la caja 1: ");
        double ancho1 = scanner.nextDouble();
        
        System.out.print("Ingrese el alto de la caja 1: ");
        double alto1 = scanner.nextDouble();
        
        System.out.print("Ingrese la profundidad de la caja 1: ");
        double profundidad1 = scanner.nextDouble();
        
        // Asignar valores usando setters
        caja1.ancho=ancho1;
        caja1.alto=alto1;
        caja1.profundidad=profundidad1;
        
        // Información de la caja 1
        System.out.println("Información de la Caja 1:");
        System.out.println("Caja{" +
                "ancho=" + caja1.ancho +
                ", alto=" + caja1.alto +
                ", profundidad=" + caja1.profundidad +
                ", volumen=" + caja1.calcularVolumen() +
                '}');
        
        // OBJETO 2: Usando constructor con argumentos
        System.out.println("\n--- CAJA 2 (Constructor con argumentos) ---");
        
        // Solicito datos para la segunda caja usando JOptionPane
        String anchoStr = JOptionPane.showInputDialog(null, 
            "Ingrese el ancho de la caja 2:", 
            "Dimensiones - Caja 2", 
            JOptionPane.QUESTION_MESSAGE);
        double ancho2 = Double.parseDouble(anchoStr);
        
        String altoStr = JOptionPane.showInputDialog(null, 
            "Ingrese el alto de la caja 2:", 
            "Dimensiones - Caja 2", 
            JOptionPane.QUESTION_MESSAGE);
        double alto2 = Double.parseDouble(altoStr);
        
        String profundidadStr = JOptionPane.showInputDialog(null, 
            "Ingrese la profundidad de la caja 2:", 
            "Dimensiones - Caja 2", 
            JOptionPane.QUESTION_MESSAGE);
        double profundidad2 = Double.parseDouble(profundidadStr);
        
        // Crear caja 2 con constructor con argumentos
        Caja caja2 = new Caja(ancho2, alto2, profundidad2);
        
        // Información de la caja 2
        System.out.println("Información de la Caja 2:");
        System.out.println("Caja{" +
                "ancho=" + caja2.ancho +
                ", alto=" + caja2.alto +
                ", profundidad=" + caja2.profundidad +
                ", volumen=" + caja2.calcularVolumen() +
                '}');
        
        // Calculo de volumenes
        System.out.println("\n=== VOLÚMENES ===");
        double volumen1 = caja1.calcularVolumen();
        double volumen2 = caja2.calcularVolumen();
        
        System.out.printf("Volumen de la Caja 1: %.2f unidades cúbicas\n", volumen1);
        System.out.printf("Volumen de la Caja 2: %.2f unidades cúbicas\n", volumen2);
        
        
        // Mostrar resultado final con JOptionPane
        JOptionPane.showMessageDialog(null, 
            String.format("RESULTADOS FINALES:\n\n" +
                    "Caja 1 (Constructor vacío):\n" +
                    "Dimensiones: %.2f x %.2f x %.2f\n" +
                    "Volumen: %.2f unidades cúbicas\n\n" +
                    "Caja 2 (Constructor con argumentos):\n" +
                    "Dimensiones: %.2f x %.2f x %.2f\n" +
                    "Volumen: %.2f unidades cúbicas\n\n", 
                    caja1.ancho, caja1.alto, caja1.profundidad, volumen1,
                    caja2.ancho, caja2.alto, caja2.profundidad, volumen2
                    ),
            "Resultados Finales", 
            JOptionPane.INFORMATION_MESSAGE);
        
        // Cerrar scanner
        scanner.close();
        
        System.out.println("\n¡Gracias por usar el programa!");
    }
}