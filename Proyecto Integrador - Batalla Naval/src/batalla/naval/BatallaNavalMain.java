package batalla.naval;
import Servicio.ServicioBatallaNaval;

public class BatallaNavalMain {

    /**
     * Se importa la clase servicio.
     * Ahora llama al método mostrarMenu, que gestiona todo el ciclo de vida de la aplicación.
     */
    public static void main(String[] args) {
        ServicioBatallaNaval sn = new ServicioBatallaNaval();
        
        // Llamada al método que inicia y gestiona el Menú Interactivo
        sn.mostrarMenu(); 
    }
}
