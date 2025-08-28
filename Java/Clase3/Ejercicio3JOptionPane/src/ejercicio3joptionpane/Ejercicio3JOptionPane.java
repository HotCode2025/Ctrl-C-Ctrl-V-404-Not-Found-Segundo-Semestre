package ejercicio3joptionpane;

import java.util.Random;
import javax.swing.JOptionPane;

/**
 *
 * @author Gustavo Martinez Trejo
 */
public class Ejercicio3JOptionPane {

    public static void main(String[] args) {
        Random random = new Random();

        int numSecreto = random.nextInt(101); // 0-100
        String input;
        int num;
        int cont = 0;
        
        do {
            input = JOptionPane.showInputDialog("¡Adivina el número entre 0 y 100!\nIngrese su número:");
            num = Integer.parseInt(input);
            cont++;
            
            if (num > numSecreto) {
                JOptionPane.showMessageDialog(null, "Es menor");
            } else if (num < numSecreto) {
                JOptionPane.showMessageDialog(null, "Es mayor");
            } else {
                JOptionPane.showMessageDialog(null, "¡Correcto! El número era " + numSecreto + 
                                                  "\nNúmero de intentos: " + cont);
            }
        } while (num != numSecreto);    }
    
}
