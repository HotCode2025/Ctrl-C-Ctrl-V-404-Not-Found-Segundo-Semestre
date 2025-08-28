package ejercicio1joptionpane;
import javax.swing.JOptionPane;

/**
 *
 * @author Rocio Lucero
 */
public class Ejercicio1JOptionPane {


    public static void main(String[] args) {
    int num;

        do {
            String input = JOptionPane.showInputDialog("Ingrese un número (0 para terminar):");
            num = Integer.parseInt(input);
            if (num != 0) {
                if (num % 2 == 0) {
                    JOptionPane.showMessageDialog(null, "Es un número par");
                } else {
                    JOptionPane.showMessageDialog(null, "Es un número impar");
                }
            }

        } while (num != 0);
    }
    
}
