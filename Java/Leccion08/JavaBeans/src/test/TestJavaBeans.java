
package test;

import domain.Persona;

class TestJavaBeans {
    public static void main(String[] args) {
        Persona persona = new Persona();
        persona.setNombre("juan");
        persona.setApellido("perez");
        System.out.println("persona = "+persona.getNombre());
        System.out.println("Persona apellido: "+persona.getApellido());
    }
}
