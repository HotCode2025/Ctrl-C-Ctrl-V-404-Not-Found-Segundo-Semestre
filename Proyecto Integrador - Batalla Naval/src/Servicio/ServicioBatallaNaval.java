package Servicio;

import Entidad.BatallaNaval;
import java.util.Scanner;

/**
 * En esta clase se desarrolla la logica de inicialización del objeto devolviendo su valor al main.
 * además controla el desarrollo logico del juego una vez llamado.
 * @author Pablo
 */
public class ServicioBatallaNaval {
    // Se importan objeto y Scanner
    BatallaNaval b1 = new BatallaNaval();
    Scanner scan = new Scanner(System.in);
    
    
    // ==========================================================
    // Menú interactivo
    // ==========================================================
    public void mostrarMenu() {
        int opcion;
        
        do {
            System.out.println("\n====== BATALLA NAVAL ======");
            System.out.println("1. Iniciar Nuevo Juego");
            System.out.println("2. Ver Reglas");
            System.out.println("3. Salir");
            System.out.print("Seleccione una opción: ");
            
            // Manejo de la entrada 
            if (scan.hasNextInt()) {
                opcion = scan.nextInt();
                scan.nextLine(); 
            } else {
                System.out.println("Opción inválida. Intente con un número (1-3).");
                scan.nextLine(); 
                opcion = 0; 
                continue; 
            }

            switch (opcion) {
                case 1:
                    System.out.println("\n--- ¡A la batalla! ---\n");
                    // Se crea e inicia el juego
                    BatallaNaval bn = crearJuego();
                    iniciarJuego(bn);
                    break;
                case 2:
                    // Reglas
                    System.out.println("\n--- REGLAS ---");
                    System.out.println("El objetivo es hundir los 5 navíos enemigos antes de quedarte sin torpedos (40).");
                    System.out.println("Ingresa coordenadas X e Y entre 1 y 10 para lanzar tu ataque.");
                    System.out.println("Los barcos son: 2, 3, 3, 4 y 5 unidades de largo.\n");
                    break;
                case 3:
                    System.out.println("\n¡Gracias por jugar! Hasta pronto.");
                    return; 
                default:
                    System.out.println("Opción no reconocida. Por favor, ingrese 1, 2 o 3.");
            }
            
            if (opcion != 3) {
                System.out.println("\nPresione ENTER para volver al menú principal...");
                scan.nextLine(); 
            }

        } while (opcion != 3);
    }

    
    // Metodo de inicializacion, seteo y devolucion del objeto lleno al main.
    public BatallaNaval crearJuego() {
        System.out.println("Bienvenido! inicializaremos el juego en un instante: ");
        System.out.println("Colocando navíos");
        // Aseguramos que la cadena hundidos se resetee para la nueva partida
        b1.setHundidos(""); 
        b1.asignarBarcos();
        System.out.println("barcos listos!\nPreparando proyectiles y campo de juego");
        b1.setCampoOculto(campoOculto());
        b1.setTorpedos(40);
        System.out.println("Proyectiles y campo listo! tienes 40 intentos!\n\n");
        return b1;
    }
    
    /*Metodo privado inicializa el campoOculto (el que vera el usuario) en espacios vacios donde hay null. 
    Devuelve el campo lleno.*/
    
    private String[][] campoOculto() {
        String[][] campo = new String[10][10];
        for (int i = 0; i < campo.length; i++) {
            for (int j = 0; j < campo.length; j++) {
                campo[i][j] = " ";
            }
        }
        return campo;
    }
    //Metodo privado, es llamado dentro del desarrollo del juego, devuelve coordenada x/y ingresada por usuario.
    
    private int coordenada() {
        // Se corrige la validación para asegurar que esté entre 1 y 10.
        while (!scan.hasNextInt()) {
            System.out.println("Valor invalido. Intenta con un número.");
            scan.next(); // Consumir la entrada no válida
        }
        int coordenada = scan.nextInt();
        while (coordenada < 1 || coordenada > 10) { 
            System.out.println("Valor invalido, intenta de nuevo (1-10)");
            
             while (!scan.hasNextInt()) {
                System.out.println("Valor invalido. Intenta con un número.");
                scan.next();
            }
            coordenada = scan.nextInt();
        }
        return (coordenada - 1);
    }
    /**
     * Metodo privado es llamado desde iniciarJuego, recibe al objeto y las dos coordenadas x/y que ingresa el usuario
     * Valida si en la matriz campoBatalla la coordenada 'golpeo' un barco enemigo.
     * Si es correcto (golpe true) se muestra un mensaje y actualiza el valor en la matriz que ve el usuario campoOculto
     * Si es falso (golpe false) se muestra mensaje 'Agua' descontando en uno el valor torpedos del objeto y actualizando ambas matrices
    
     */
    private void averiadoAgua(BatallaNaval b1, int x, int y) {
        String[][] c1 = b1.getCampoBatalla();
        String[][] c2 = b1.getCampoOculto();
        if (c1[x][y].equalsIgnoreCase(" ")) {
            System.out.println("Agua!! un proyectil menos...");
            c2[x][y] = "a";
            c1[x][y] = "a";
            b1.setTorpedos(b1.getTorpedos() - 1);
        } else {
            System.out.println("Navío averiado! sigue así!!");
            c2[x][y] = c1[x][y];
        }
    }
    /**
     * Esta funcion tiene por objetivo validar cuando gana el usuario:
     * Recibe el valor de las dos matrices del objeto de forma local
     * Las recorre comparando sus elementos.
     * Si ambas son iguales (se da por entendido que el usuario golpeo todos los barcos)
     * devuelve true y el juego termina.
     * sino devuelve false continuando el bucle en iniciarJuego.
     */
    private boolean gano(BatallaNaval b1) {
        String[][] c2 = b1.getCampoOculto();
        String[][] c1 = b1.getCampoBatalla();
        boolean check = true;
        for (int i = 0; i < c2.length; i++) {
            for (int j = 0; j < c2.length; j++) {
                if (!c2[i][j].equalsIgnoreCase(c1[i][j])) {
                    check = false;
                    break;
                }
            }
        }
        return check;
    }

    /**
     * MÉTODO MEJORADO: Ahora solo concatena el primer dígito del barco para contar.
     * Si un barco (ej. 55555) es hundido, concatena '5'.
     */
    private void hundidos(BatallaNaval b1) {
        String[] lista = b1.getBarcos();
        String[][] c1 = b1.getCampoOculto();
        String vertical = "";
        String horizontal = "";
        
        // Recalcular la posición de navíos en cada turno
        for (int i = 0; i < c1.length; i++) {
            for (int j = 0; j < c1.length; j++) {
                vertical += c1[j][i];
                horizontal += c1[i][j];
            }
        }

        for (String navio : lista) {
            // Se verifica si el barco está completamente hundido (vertical u horizontal)
            // Y si AÚN NO ha sido registrado en la cadena 'hundidos' (usando solo su primer dígito)
            String indicador = navio.substring(0, 1);
            
            if ((vertical.contains(navio) || horizontal.contains(navio)) && !b1.getHundidos().contains(indicador)) {
                
                // Si está hundido y es nuevo, se concatena solo el indicador (ej: '5')
                b1.setHundidos(b1.getHundidos() + indicador);
                System.out.println("¡Navío de tamaño " + navio.length() + " hundido!");
                
                // No rompemos el bucle aquí para seguir chequeando los otros barcos
            }
        }
    }
    /**
     * Este metodo una vez llamado, es el principal hilo 'logico' del programa.
     * Se modifica la línea de Navíos hundidos para mostrar el contador (ej: 2 / 5).
     */
    public void iniciarJuego(BatallaNaval b1) {
        do {
            b1.mostrar(b1.getCampoOculto());
            
            // Muestra el contador
            int totalHundidos = b1.getHundidos().length();
            int totalBarcos = b1.getBarcos().length;
            System.out.println("Navíos hundidos: " + totalHundidos + " / " + totalBarcos);
            
            System.out.println("Proyectiles restantes : " + b1.getTorpedos());
            System.out.println("\nIngresa coordenada de ataque en Eje X (1-10)");
            int x = coordenada();
            System.out.println("Ingresa coordenada de ataque en Eje Y (1-10)");
            int y = coordenada();
            scan.nextLine(); // Consumir el salto de línea pendiente
            System.out.println("Lanzando ataque en coordenada " + (x + 1) + ", " + (y + 1));
            averiadoAgua(b1, x, y);
            hundidos(b1);
            
            if (gano(b1)) {
                System.out.println("Ganaste!!");
                break;
            }
        } while (b1.getTorpedos() > 0);

        if (b1.getTorpedos() == 0) {
            System.out.println("Te quedaste sin munición! esta era la posición enemiga");
            b1.mostrar(b1.getCampoBatalla());
            System.out.println("Perdiste, intenta de nuevo!!");
        }
    }
}