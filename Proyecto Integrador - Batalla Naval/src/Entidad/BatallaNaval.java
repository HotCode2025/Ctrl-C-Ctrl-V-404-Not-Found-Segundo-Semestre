package Entidad;

/**
 * Este objeto almacena la información necesaria para que los datos del juego funcionen
 * el mismo comprende atributos, setters/getters y metodos de inicializacion del juego en sí.
 */
public class BatallaNaval {
    //Atributos:
    
    private String[][] campoOculto = new String[10][10];
    private String[][] campoBatalla = new String[10][10];
    // Se mantiene el array de barcos para la lógica de hundimiento y conteo
    private final String[] barcos = {"22", "333", "...", "4444", "55555"};
    private String hundidos = ""; // Ahora solo guarda un dígito por barco hundido (ej: "2345")
    private int torpedos;

    //constructores:
    
    public BatallaNaval() {
    }

    public BatallaNaval(int torpedos) {
        this.torpedos = torpedos;
    }

    
    //Getter & Setter: 
    
    public int getTorpedos() {
        return torpedos;
    }

    public void setTorpedos(int torpedos) {
        this.torpedos = torpedos;
    }

    public String getHundidos() {
        return hundidos;
    }

    public void setHundidos(String hundidos) {
        this.hundidos = hundidos;
    }

    public String[][] getCampoOculto() {
        return campoOculto;
    }

    public void setCampoOculto(String[][] campoOculto) {
        this.campoOculto = campoOculto;
    }

    public String[][] getCampoBatalla() {
        return campoBatalla;
    }

    public void setCampoBatalla(String[][] campoBatalla) {
        this.campoBatalla = campoBatalla;
    }

    public String[] getBarcos() {
        return barcos;
    }

    /**
     * Metodos:
     * alineacion: Devuelve un booleano true/false para definir la direccion de los barcos en la matriz
     * asignarbarcos: Recorre el array barcos asignandolos a la matriz campoBatalla en horizontal o vertical
     * agua: llena campoBatalla con espacios vacios donde su valor sea null
     * mostrar: muestra la matriz pasada por parametro, dandole un formato y haciendola legible al usuario.
     */
    private boolean alineacion() {
        int num = (int) Math.floor(Math.random() * 2);
        boolean vh = num == 0;
        return vh;

    }

    public void asignarBarcos() {
        for (String barco : barcos) {
            boolean linea = alineacion();
            boolean check = false;
            int x;
            int y;
            do {

                x = (int) (Math.random() * 10);
                y = (int) (Math.random() * (10 - barco.length()));
                int aux = 0;

                for (int j = y; j < (y + barco.length()); j++) {
                    if (linea == false) {
                        if (campoBatalla[x][j] == null && campoBatalla[j][x] == null) {
                            aux++;
                        }
                    } else {
                        if (campoBatalla[j][x] == null && campoBatalla[x][j] == null) {
                            aux++;
                        }
                    }
                }
                if (aux == barco.length()) {
                    check = true;
                }
            } while (check == false);

            for (int j = y; j < (y + barco.length()); j++) {
                if (linea == true) {
                    campoBatalla[x][j] = barco.substring((j - y), (j - y + 1));
                } else {
                    campoBatalla[j][x] = barco.substring((j - y), (j - y + 1));
                }
            }
        }
        agua();
    }

    private void agua() {
        for (int i = 0; i < campoBatalla.length; i++) {
            for (int j = 0; j < campoBatalla.length; j++) {
                if (campoBatalla[i][j] == null) {
                    campoBatalla[i][j] = " ";
                }
            }
        }
    }

    public void mostrar(String[][] campo) {
        for (int i = 0; i < 10; i++) {
            if (i == 9) {
                System.out.print(String.valueOf(i + 1) + " |");
            } else if (i == 0) {
                System.out.print("    1 2 3 4 5 6 7 8 9 10"
                        + "\n    _ _ _ _ _ _ _ _ _ _\n1  |");
            } else {
                System.out.print(String.valueOf(i + 1) + "  |");
            }
            for (int j = 0; j < 10; j++) {
                System.out.print(campo[i][j] + "|");
            }
            System.out.println("");
        }
        System.out.println("    ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯");
    }
}
