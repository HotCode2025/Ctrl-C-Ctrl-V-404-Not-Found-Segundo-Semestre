public class Persona {
    // Propiedades protegidas
    protected String nombre;
    protected String direccion;
    protected boolean eliminado;

    // Constructor vacío
    public Persona() {
    }

    // Constructor con parámetros
    public Persona(String nombre) {
        this.nombre = nombre;
    }

    public Persona(String nombre, String direccion, boolean eliminado) {
        this.nombre = nombre;
        this.direccion = direccion;
        this.eliminado = eliminado;
    }

    // Métodos getter y setter para nombre
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    // Métodos getter y setter para sueldo
    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String getDireccion() {
        return direccion;
    }

    // Métodos getter y setter para eliminado
    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Persona[");
        sb.append("nombre=").append(nombre);
        sb.append(", direccion=").append(direccion);
        sb.append(", eliminado=").append(eliminado);
        sb.append(", ").append(super.toString());
        sb.append("]");
        return sb.toString();
    }
}