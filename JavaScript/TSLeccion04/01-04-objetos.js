let x = 10; //Variable de tipo primitiva
console.log(x.length);
console.log('Tipos Primitivos');
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase(); //Convierte las minusculas en mayusculas
    },
    set lang(lang){
        this.idioma =lang.toUpperCase();
    },
    nombreCompleto: function(){// Metodo o funcion en JavaScript
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){//Este es el Metodo Get
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un Objeto');
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '5432618282821';
console.log(persona2.telefono);
console.log('Creamos un nuevo Objeto');
console.log(persona['apellido']); //Accedemos como si fuera un arreglo
console.log('Usamos el ciclo for in');
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}
console.log('Cambiamos y eliminamos un error');
persona.apellida = 'Betancud'; //Cambiamos dinamicamente un valor del objeto
delete persona.apellida //Eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
//Numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un objeto: forma 1');
console.log(persona.nombre+', '+persona.apellido);

//Numero 2: A traves del ciclo for in
console.log('Distintas formas de imprimir un objeto: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion Object.values()
console.log('Distintas formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: Utilizaremos el metodo JSON.stringify
console.log('Distintas formas de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log('Comenzamos a utilizar el metodo Get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idioma');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){ //Constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Leo', 'Lopez', 'lopezl@gmail.com');
padre.nombre = 'Luis'; //Modificamos el nombre
padre.telefono = '5492618282821'; //Una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); //Utilizamos la funcion
let madre = new Persona3('Laura', 'Contrera', 'contreral@gmail.com');
console.log(madre);
console.log(madre.telefono); //La propiedad no esta definida
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos

//Caso objeto 1
let miObjeto = new Object(); //Esta es una opcion formal
//Caso objeto 2
let miObjeto2 = {}; //Esta opcion es breve y recomendada

//Caso String 1
let miCadena1 = new String('Hola'); //Sintaxis Formal
//Caso String 2
let miCadena2 = 'Hola'; //Esta es la sintaxis simplificada y recomendada

//Caso con numeros 1
let miNumero1 = new Number(1); //Es formal no recomendable
//Caso con numeros 2
let miNumero2 = 1; //Sintaxis recomendada

//Caso boolean 1
let miBoolean1 = new Boolean(false); //Formal
//Caso bollean 2
let miBoolean2 = false; //Sintaxis recomendada

//Caso Arreglos 1
let miArreglo1 = new Array(); //Formal
//Caso Arreglos 2
let miArreglo2 = []; //Sintaxis recomendada

//Caso funcion 1
let miFuncion1 = new function(){}; //Todo despues de new es considerado objeto
//Caso funcion 2
let miFuncion2 = function(){}; //Notacion simplificada y recomendada
 
// Uso de Prototype
Persona3.prototype.telefono = '2618383832';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '5492618383832';
console.log(madre.telefono);

//Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
        //return this.nombre+' '+this.apellido;
    }
}

let persona5 = {
    nombre:'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic.', '5492618383834'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '5492618585856'));

//Metodo Apply
let arreglo = ['Ing.', '5492618585856']
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));
