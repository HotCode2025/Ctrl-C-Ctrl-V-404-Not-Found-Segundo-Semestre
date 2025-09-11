//Ejercicio 8: Pedir un numero N, y mostrar todos los numeros, del 1 al N - con Scanner y JOptionPane
package clase5;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Clase5 {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.println("Elija una opción para ejecutar el código:");
        System.out.println("1. Usar Scanner)");
        System.out.println("2. Usar JOptionPane");
        int opcion = teclado.nextInt();

        if (opcion == 1) {
            mostrarConScanner();
        } else if (opcion == 2) {
            mostrarConJOptionPane();
        } else {
            System.out.println("Opción inválida");
        }
    }

    public static void mostrarConScanner() {
        Scanner teclado = new Scanner(System.in);
        System.out.println("Ingrese un número entero:");
        int n = teclado.nextInt();
        int i = 1;

        while (i <= n) {
            System.out.println(i);
            i++;
        }
    }

    public static void mostrarConJOptionPane() {
        int n = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número entero"));
        int i = 1;
        String resultado = "";

        while (i <= n) {
            resultado += i + "\n";
            i++;
        }

        JOptionPane.showMessageDialog(null, resultado);
    }
}
