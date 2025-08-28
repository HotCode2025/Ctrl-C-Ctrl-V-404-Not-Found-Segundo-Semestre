package ejercicio3scanner;
import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author Gustavo Martinez Trejo
 */
public class Ejercicio3Scanner {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();
        
        int numeroSecreto = random.nextInt(101); // 0-100
        int intento;
        int intentos = 0;
        
        System.out.println("¡Adivina el número entre 0 y 100!");
        
        do {
            System.out.print("Ingrese su número: ");
            intento = sc.nextInt();
            intentos++;
            
            if (intento > numeroSecreto) {
                System.out.println("Es menor");
            } else if (intento < numeroSecreto) {
                System.out.println("Es mayor");
            } else {
                System.out.println("¡Correcto! El número era " + numeroSecreto);
                System.out.println("Número de intentos: " + intentos);
            }
        } while (intento != numeroSecreto);    }
    
}
