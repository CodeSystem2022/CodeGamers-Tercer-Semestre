import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //definimos la lista fuera del ciclo while
        List<Persona> personas = new ArrayList<>();
        //empezamos con el menu
        var salir = false;
        while(!salir){
            mostrarMenu();
            try{
                salir = ejecutarOperacion(entrada, personas);
            }catch (Exception e){
                System.out.println("Ocurrió un error: "+e.getMessage());
            }
            System.out.println();
        }// fin ciclo while
    }//fin metodo main

    private static void  mostrarMenu(){
        //mostrar las opciones
        System.out.print("""
                ******Listado de Personas*****
                1. Agregar
                2. Listar
                3. Salir
                """);
        System.out.print("Digite una de las opcines: ");
    }//fin de metodo mostrarmenu

    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas){
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        //revisamos la opcion digitada con un switch
        switch (opcion){
            case 1 -> {//agrega una persona a la lista
                System.out.print("Digite el nombre: ");
                var nombre = entrada.nextLine();
                System.out.print("Digite el telefono: ");
                var tel = entrada.nextLine();
                System.out.print("Digite el correo: ");
                var email = entrada.nextLine();
                //crear objeto persona
                var persona = new Persona(nombre, tel, email);
                //agregamos la persona a la lista
                personas.add(persona);
                System.out.println("La lista tiene: "+personas.size()+" elementos");
            }//fin caso 1
            case 2 -> {//listar las personas
                System.out.println("Listado de personas: ");
                //mejoras con lamba y el metodo de referencia
                //personas.forEach((persona) -> System.out.println(persona));
                personas.forEach(System.out::println);
            }//fin caso 2
            case 3 -> {//salir del ciclo
                System.out.println("Hasta pronto...");
                salir = true;
            }//fin del caso 3
            default -> System.out.println("Opcion incorrecta: "+opcion);
        }//fin del switch
        return salir;
    } //fin del metodo ejecutarOperacion
}//fin de la clase listado de personasApp
