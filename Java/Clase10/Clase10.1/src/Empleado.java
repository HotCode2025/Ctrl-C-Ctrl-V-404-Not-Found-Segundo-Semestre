public class Empleado extends Persona {
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados;

    public Empleado() {
        this.idEmpleado = ++Empleado.contadorEmpleados;
    }

    public Empleado(String nombre, double sueldo) {
        //super(nombre); // si utilizamos super, no podemos usar this en el mismo constructor
        this(); //Estamos llamando al constructor vacio de Empleado
        this.nombre = nombre; // atributo heredado de la clase Persona 
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return idEmpleado;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public double getSueldo() {
        return sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado[");
        sb.append("idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());
        sb.append("]");
        return sb.toString();
    }
}
