
package clase11arreglos;


public class Clase11Arreglos {    
    public static void main(String[] args) { //lado de derecho instanciamos un obj. de tipo object
        int edades[] = new int[3]; //el lado izquierdo declaramos variable
        System.out.println("edades = " + edades);
        
        edades[0] = 17;
        System.out.println("edades 0 = " + edades [0]);
        edades [1] = 30;
        System.out.println("edades 1 = " + edades [1]);
        edades [2] = 23;
        System.out.println("edades 2 = " + edades [2]);
        
        //edades [3] = 28; // Fuera de rango, error en RUN
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("edades y sus elementos "+i+": "+edades[i]);            
        }
    }    
    
}
