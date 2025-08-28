package ejercicio2scanner;
import java.util.Scanner;

/**
 *
 * @author Gustavo Martinez Trejo
 */
public class Ejercicio2Scanner {


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numero;
        int contador = 0;

        do {
            System.out.print("Ingrese un número (negativo para terminar): ");
            numero = sc.nextInt();

            if (numero >= 0) {
                contador++;
            }
        } while (numero >= 0);

        System.out.println("Se introdujeron " + contador + " números");

    }
    
}
