import java.util.Scanner;

/*Ejercicio 12: Pedir un número y calcular su factorial
* Hacerlo con clase Scanner y JOptionPane*/
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite un número: ");
        int num = scan.nextInt();
        long factorial = 1;
        for (int i = 1; i <= num ; i++) {
            factorial *= i;
        }
        System.out.println("El factorial de " + num + " Es: " + factorial);
    }
}