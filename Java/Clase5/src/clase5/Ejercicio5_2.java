package clase5;

public class Ejercicio5_2 {
    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 5;
        aritmetica1.b = 10;
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("El resultado de la suma con retorno es: " + resultado);
    }
}
