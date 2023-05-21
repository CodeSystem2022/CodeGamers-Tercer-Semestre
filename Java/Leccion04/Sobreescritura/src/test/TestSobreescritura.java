
package test;

import domain.*;


public class TestSobreescritura {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan", 5000);
        imprimir(empleado1);
        //System.out.println("empleado1 = " + empleado1.obtenerDetalles());
        Gerente gerente1 = new Gerente("Diego", 10000, "System");
        imprimir(gerente1);
        //System.out.println("gerente1 = " + gerente1.obtenerDetalles());
    }
    
    public static void imprimir (Empleado empleado) {
        System.out.println("empleado = " + empleado.obtenerDetalles());
    }
    
}
