import javax.swing.JOptionPane;

public class Main {
    public static void main(String[] args) {
        long producto = 1;

        for (int i = 0; i < 10; i++) {
            while (true) {
                try {
                    String input = JOptionPane.showInputDialog(
                            null,
                            String.format("Digite el %d° número impar:", i + 1)
                    );

                    if (input == null) {
                        JOptionPane.showMessageDialog(null, "Programa cancelado.");
                        return;
                    }

                    int num = Integer.parseInt(input);

                    if (num % 2 != 0) {
                        producto *= num;
                        break;
                    } else {
                        JOptionPane.showMessageDialog(null, "Debe ser un número impar");
                    }
                } catch (NumberFormatException e) {
                    JOptionPane.showMessageDialog(null, "Ingrese un número válido");
                }
            }
        }
        JOptionPane.showMessageDialog(null, "El producto de tus números es: " + producto);
    }
}
