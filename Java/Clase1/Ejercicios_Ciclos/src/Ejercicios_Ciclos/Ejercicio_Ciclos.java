
package Ejercicios_Ciclos;

public class Ejercicio_Ciclos {
     public static void main(String[] args) {
        
        var conteo = 0;
        while (conteo < 7) {
            System.out.println("conteo = " + conteo);
            conteo++;
        }
        
        var contador = 7;
        do {
            System.out.println("contador = " + contador);
            contador++;
        } while(contador < 7);
        
        inicio: //Etiqueta
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando); 
                break inicio;
            }               

        }
        
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 != 0){
                continue;
            }               
            System.out.println("contando = " + contando);
        }
        
    }
}

