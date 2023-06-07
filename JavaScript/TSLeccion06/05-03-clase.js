//let persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer: Persona is not defined

class Persona{ //CLASE PADRE

    static contadorPersonas = 0; //Atributo stático
    //email = 'Valor default email'; //Atributo NO estático

    static get MAX_OBJ(){ //Este método simula una constante
        return 5;
    }  
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorPersonas <Persona.MAX_OBJ){
            this.idPersona = ++Persona.contadorPersonas;
        }
        else{
            console.log('Se ha superado el máximo de objetos permitidos');
        }
        
        //console.log('Se incrementa el contador: '+Persona.contadorObjetosPersona);
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){
        return this.idPersona+' '+this.nombre+' '+this._apellido;
    }

    //Sobreescribiendo el método de la clase padre (Object)
  
    toString(){ //Regresa un String
        //Se aplica el polimosfismo que significa = multiples formas en tiempo de ejecución
        //El método que se ejecuta depende si es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }

    static saludar(){
        console.log('Saludos desde este método static');

    }

    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido);

    }
}

class Empleado extends Persona{ //CLASE HIJA
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }

    //Sobreescritura 
    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento;
    }
}

//creación y métodos creados

let persona1 = new Persona('Martín', 'Garay'); //objeto1 constructor
console.log(persona1.nombre); //método get
persona1.nombre = 'Juan Carlos'; //método set modifica
console.log(persona1.nombre); //método get nuevo resultado
persona1.nombre = 'Gastón Exequiel';
console.log(persona1.nombre);
//console.log(persona1);

let persona2 = new Persona('Carlos', 'Lara'); //objeto2 constructor
console.log(persona2.nombre); //método get
persona2.nombre = 'María Laura'; //método set modifica
console.log(persona2.nombre); //método get nuevo resultado
persona2.nombre = 'Montiel Ariel';
console.log(persona2.nombre);
//console.log(persona2);

let empleado1 = new Empleado('María', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

//Object.prototype.toString Esta es la manera de acceder a atributos y métodos de manera dinámica
console.log(empleado1.toString());
console.log(persona1.toString());
