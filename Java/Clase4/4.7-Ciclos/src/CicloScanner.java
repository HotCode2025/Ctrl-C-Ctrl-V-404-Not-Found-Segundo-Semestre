import java.util.Scanner;

public class CicloScanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numero;
        int suma = 0;
        int contador = 0;
        
        System.out.println("Introduce números (introduce un negativo para terminar):");
        
        do {
            System.out.print("Número: ");
            numero = scanner.nextInt();
            
            if (numero >= 0) {
                suma += numero;
                contador++;
            }
        } while (numero >= 0);
        
        scanner.close();
        
        if (contador > 0) {
            double media = (double) suma / contador;
            System.out.println("Cantidad de números introducidos: " + contador);
            System.out.println("Suma total: " + suma);
            System.out.println("Media: " + media);
        } else {
            System.out.println("No se introdujeron números válidos.");
        }
    }
}