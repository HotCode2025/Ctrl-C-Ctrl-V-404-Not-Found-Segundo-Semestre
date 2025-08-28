package ejercicio2joptionpane;
import javax.swing.JOptionPane;

/**
 *
 * @author Gustavo Martinez Trejo
 */
public class Ejercicio2JOptionPane {

    public static void main(String[] args) {        
        String input;
        int num;
        int cont = 0;
        
        do {
            input = JOptionPane.showInputDialog("Ingrese un número (negativo para terminar):");
            num = Integer.parseInt(input);
            
            if (num >= 0) {
                cont++;
            }
        } while (num >= 0);
        
        JOptionPane.showMessageDialog(null, "Se introdujeron " + cont + " números");    }
    
}
