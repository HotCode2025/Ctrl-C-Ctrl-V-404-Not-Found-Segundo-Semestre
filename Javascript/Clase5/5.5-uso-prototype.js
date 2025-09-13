//Uso de prototype
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

//agregamos un nuevo atributo al objeto padre
padre.tel = "5492618282821"; //propiedad exclusiva de objeto padre
console.log(padre);

//madre no tiene el atributo telefono
let madre = new Persona3("Laura","Contrera", "contreral@gmail.com" )
console.log(madre);
console.log(madre.tel); //la propiedad no esta definida


//uso de prototype para agregar un atributo a todos los objetos
Persona3.prototype.tel = "2613832822"; //propiedad es compartida por todos los objetos

console.log(padre.tel); //toma la propiedad del objeto
console.log(madre.tel); //toma la propiedad del prototype

madre.tel = "5492615555555"; //modifica la propiedad del objeto madre
console.log(madre.tel); //toma la propiedad del objeto madre
