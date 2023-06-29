package test;

import domain.Persona;


public class TestForEach {
    public static void main(String[] args) {
        int edades[] = {5, 6, 8, 9}; //Sintaxis resumida
        for(int edad:edades){
            System.out.println("Edad = "+edad);
        }
        Persona personas[]= {new Persona("Juan"), new Persona("Carla"), new Persona("Beatriz")};
        
        //For each
        for(Persona persona: personas){
            System.out.println("Persona:"+persona);
        }
    }
}
