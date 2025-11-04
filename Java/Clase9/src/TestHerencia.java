import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado emp = new Empleado("Stefano", 75000);
        System.out.println(emp);
        testClientes();
    }

    public static void testClientes() {

        Date fecha1 = new Date();

        Cliente cliente1 = new Cliente("Ana Gomez", fecha1, true);
        System.out.println(cliente1);
    }
}
