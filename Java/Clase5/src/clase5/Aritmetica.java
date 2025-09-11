package clase5;

public class Aritmetica {
    int a;
    int b;

    public void sumar() {
        int resultado = a + b;
        System.out.println("El resultado de la suma es: " + resultado);
    }

    public int sumarConRetorno() {
        return a + b;
    }

    public int sumarConArgumentos(int a, int b) {
        this.a = a; 
        this.b = b; 
        return sumarConRetorno();
    }
}
