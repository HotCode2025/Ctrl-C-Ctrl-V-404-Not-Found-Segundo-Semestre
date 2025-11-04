package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 20000.00);
        Producto producto3 = new Producto("Gemelos", 300000.00);
        Producto producto4 = new Producto("Camisa", 15000.00);
        Producto producto5 = new Producto("Chaleco", 10500.00);
        Producto producto6 = new Producto("Medias", 4000.00);
        Producto producto7 = new Producto("Boina", 19000.00);
        Producto producto8 = new Producto("Gabardina", 11500.00);
        Producto producto9 = new Producto("Parka", 95000.00);
        Producto producto10 = new Producto("Zapatos",80000.00);

        Orden orden1 = new Orden();
        Orden orden2 = new Orden();
        Orden orden3 = new Orden();
        //Mas Productos
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto9);
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden3.agregarProducto(producto6);
        orden3.agregarProducto(producto7);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto10);
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        orden3.mostrarOrden();
    }
    
}
