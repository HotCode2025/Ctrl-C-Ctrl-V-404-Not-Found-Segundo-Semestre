import javax.swing.JOptionPane;

public class CicloJOptionPane {
    public static void main(String[] args) {
        int numero;
        int suma = 0;
        int contador = 0;
        
        JOptionPane.showMessageDialog(null, "Introduce números (introduce un negativo para terminar)");
        
        do {
            String input = JOptionPane.showInputDialog("Introduce un número:");
            
            // Verificar si el usuario hizo clic en Cancelar
            if (input == null) {
                break;
            }
            
            try {
                numero = Integer.parseInt(input);
                
                if (numero >= 0) {
                    suma += numero;
                    contador++;
                }
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Por favor, introduce un número válido.");
                numero = 0; // Continuar el bucle
            }
            
        } while (numero >= 0);
        
        if (contador > 0) {
            double media = (double) suma / contador;
            String resultado = "Cantidad de números: " + contador + 
                             "\nSuma total: " + suma + 
                             "\nMedia: " + String.format("%.2f", media);
            JOptionPane.showMessageDialog(null, resultado);
        } else {
            JOptionPane.showMessageDialog(null, "No se introdujeron números válidos.");
        }
    }
}