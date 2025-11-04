
package clase11arreglos;

import clase11arreglosDomain.Persona;

public class Matrices {
    public static void main(String[] args) {
        int edades [][] = new int[3] [2];
        System.out.println("edades = " + edades);
        edades[0] [0] = 5; //Llenado manual
        edades[0] [1] = 7; //Diferente columna
        edades[1] [0] = 8;
        edades[1] [1] = 4;
        edades[2] [0] = 1;
        edades[2] [1] = 3;
        System.out.println("edades 0-0 = " + edades [0][0]);
        System.out.println("edades 0-1 = " + edades [0][1]);
        System.out.println("edades 1-0 = " + edades [1][0]);
        System.out.println("edades 1-1 = " + edades [1][1]);
        System.out.println("edades 2-0 = " + edades [2][0]);
        System.out.println("edades 2-1 = " + edades [2][1]);
        
        System.out.println("Recorremos Matriz con for: ");        
        for (int fila = 0; fila < edades.length; fila++) {
            for (int col = 0; col < edades[fila].length; col++) {
                System.out.println("Edades " +fila+"-"+col+": "+edades[fila][col]);                               
            }            
        }
        
        //Sintaxis clásica
        //String frutas[][] = new String[3][2]
        
        //Sintaxis simplificada
        String frutas[][] = {{"Limon", "Pomelo"},{"Ciruelas", "Kiwi"},{"Banana","Manzana"}};
        imprimir(frutas);
//        for (int i = 0; i < frutas.length; i++) {
//            for (int j = 0; j < frutas[i].length; j++) {
//                System.out.println("Frutas " +i+"-"+j+": "+frutas[i][j]);                               
//            }            
//        }
        
        //Creamos Matriz de OBJETOS
        Persona personas[][] = new Persona[2][3];
        //Valores de la matriz
        personas[0][0] = new Persona("Hugo");
        personas[0][1] = new Persona("Jesus");
        personas[0][2] = new Persona("Javier");
        personas[1][0] = new Persona("Guillermo");
        personas[1][1] = new Persona("Kirlo");
        personas[1][2] = new Persona("Landro");
        System.out.println("Matriz de Personas: ");
        imprimir(personas);
    }    
    public static void imprimir(Object matriz[][]){
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.println("Matriz " +i+"-"+j+": "+matriz[i][j]);                               
            }            
        }
    }
}
