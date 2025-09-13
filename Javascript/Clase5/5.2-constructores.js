//Clase 5.2 Constructores

// Constructor de objetos
function Persona3(nombre = "Luis", apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
}
//Instanciamos el objeto
let padre = new Persona3("Leo","Lopez", "lopezl@gmail.com");
console.log(padre);

//Puedo asignar y modificar una propiedad de padre
padre.nombre = "Leonardo";
console.log(padre); // Se modifica el nombre


//Creamos una segunda instancia del objeto
let madre = new Persona3("Laura","Contrera", "contreral@gmail.com" )
console.log(madre);