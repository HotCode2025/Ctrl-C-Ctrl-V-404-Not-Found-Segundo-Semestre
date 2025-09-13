//Clase 5.3 Agregar metodos a constructores

function Persona3(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.apellido+" "+this.nombre;
    }
}

//Instanciamos el objeto
let padre = new Persona3("Leo","Lopez", "lopezl@gmail.com");
console.log(padre);

//llamada a metodo agregado al constructor
console.log(padre.nombreCompleto());


let madre = new Persona3("Laura","Contrera", "contreral@gmail.com" )
console.log(madre);
console.log(madre.nombreCompleto());