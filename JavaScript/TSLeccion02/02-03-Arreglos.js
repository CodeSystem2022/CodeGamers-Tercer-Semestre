
//Creacion de Array o Arreglos
// let autos = new Array('Ferrari', 'Renault', 'BMW'); esta es una sintaxis vieja
const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos);

//Recorremos los elementos de un arreglo
console.log(autos[0]); //De esta forma recorremos el arreglo manualmente
console.log(autos[2]);

for(let i = 0; i < autos.length; i++){ //De esta recorremos todo el arreglo y cada uno de sus elementos 
    console.log(i+' : '+autos[i]);
}

//Modificamos los elementos del arreglo
autos[1] = 'Volvo';
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push('Audi'); //Agregamos el elemento al final del arreglo
console.log(autos);

//Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Porche';
console.log(autos);

//Tercera forma de agregar un elemento teniendo CUIDADO
autos[6] = 'Renault';
console.log(autos);

//Como preguntar si es un Array o Arreglo
console.log(Array.isArray(autos)); //Devuelve un Booleano

console.log(autos instanceof Array); // Preguntamos si la variable es una instancia de la clase array
