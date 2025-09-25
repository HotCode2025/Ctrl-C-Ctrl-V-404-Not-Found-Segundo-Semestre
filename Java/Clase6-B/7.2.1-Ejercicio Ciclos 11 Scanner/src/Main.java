import java.util.Scanner;

/*Diseñar un programa que muestre el producto de los 10
     primeros números impares*/
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int producto = 1;
        for (int i = 0; i < 10; i++) {
            while(true) {
                System.out.printf("Digite el %d° numero impar: ", i+1);
                int num = scan.nextInt();
                if (num % 2 != 0) {
                    producto *= num;
                    break;
                }else{
                    System.out.println("Debe ser un número impar");
                }
            }
        }
        System.out.println("El producto de tus numeros es: " + producto);
    }
}