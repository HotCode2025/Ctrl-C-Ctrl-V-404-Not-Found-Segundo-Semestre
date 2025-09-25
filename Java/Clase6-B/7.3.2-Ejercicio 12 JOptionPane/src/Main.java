import javax.swing.*;

/*Ejercicio 12: Pedir un número y calcular su factorial
 * Hacerlo con clase Scanner y JOptionPane*/
public class Main {
    public static void main(String[] args) {
        String input = JOptionPane.showInputDialog("Digite un número:");
        int num = Integer.parseInt(input);
        long factorial = 1;

        for (int i = 1; i <= num; i++) {
            factorial *= i;
        }

        JOptionPane.showMessageDialog(null, "El factorial de " + num + " es: " + factorial);
    }
}