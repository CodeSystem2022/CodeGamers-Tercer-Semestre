package test;


public class TestAutoboxingUnboxing {
    public static void main(String[] args) {
        //Clases envolventes o wrapper
        /*
          Clases envolventes de tipo primitivos
          int = clase envolvente es integer
          long = clase envolvente Long
          float = clase envolvente Float
          double = clase envolcente Double
          boolean = clase envolvente Boolean
          byte = clase envolvente Byte
          char = clase envolvente Charter
          short = clase envolvente Short
        */
        
        int enteroPrim = 10;//Tipo primitivo
        System.out.println("enteroPrim = "+ enteroPrim);
        Integer entero= 10;//Tipo object con la clase Integer
        System.out.println("entero = "+entero.doubleValue());//Autobixing
        
        int entero2 = entero;//Unboxing
        System.out.println("entero2 = "+ entero2);
    }
}
