
package paquete1;


public class Clase1 {
    public String atributoPublic = " Valor atributo public";
    protected String atributoProtected = "Valor atributo protected";
    
    public Clase1(){
        System.out.println("constructor public");
    }
    
    protected Clase1(String atributoPublic){
        System.out.println("Constructor protected");
    }
    public void metodoPublico(){
        System.out.println("Método publico");
    }
    protected void metodoProtected(){
        System.out.println("Metodo protected");
    }
}
