
package paquete1;


public class ClaseHija2 extends Clase2{

    String atributoDefault;
    public ClaseHija2(){
        super();
        this.atributoDefault = "Modificación del atributo default";
        System.out.println("Atributo default = " + this.atributoDefault);
        this.metodoDefault();
    }

    void metodoDefault() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
