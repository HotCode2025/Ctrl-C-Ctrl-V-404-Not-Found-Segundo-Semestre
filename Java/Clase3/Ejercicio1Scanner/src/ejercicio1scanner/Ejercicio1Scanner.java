package ejercicio1scanner;
import java.util.Scanner;

/**
 *
 * @author Rocio Lucero
 */
public class Ejercicio1Scanner {

    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int num;
        
        do {
            System.out.print("Ingrese un número (0 para terminar): ");
            num = entrada.nextInt();
            if (num != 0) {
                if (num % 2 == 0) {
                    System.out.println("Es un número par");
                } else {
                    System.out.println("Es un número impar");
                }
            }

        } while (num != 0);
    }
    
}
