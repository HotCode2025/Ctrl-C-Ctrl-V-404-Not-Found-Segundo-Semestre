// Primera Parte
let x = 10; // Variable de tipo primitiva
console.log(x.ength);

// Objeto
console.log("// Tipos Primitivos");
let= persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30,
    // Tercera Parte
    nombreCompleto: function(){ // Método o función en JavaScript
        return this.apellido+" "+this.nombre;
    }    
}

console.log(persona.nombre);

// Segunda parte
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona.nombreCompleto());
console.log("// Ejecutando con un objeto");

// Cuarta Parte
let persona2 = new Object(); // Debe crear un objeto en memotria
persona2.nombre = "Juan";
persona2.direccion = "Sadalada 14";
persona2.telefono = 260456385247;
console.log(persona2.telefono);

// Quinta Parte
console.log("// Creamos un nuevo objeto");
console.log(persona["apellido"]); //Accedemos como si fuera un arreglo
console.log("// Usamos el ciclo for in")
// for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

// Sexta Parte
console.log("// Cambiamos y eliminamos un error");
persona.apellida = "Zanatta"; //Cambiamos dinamicamente un valor de un objeto
delete persona.apellida; // Eliminamos el error
console.log(JSON.stringify(persona));

// Octava Parte
// Distinta formas de imprimir un objeto
// Número 1: la más sencilla: concatenar cada valor de cada propiedad
console.log("// Distintas formas de imprimir un objeto: forma 1");
console.log(persona.nombre+","+persona.apellido);

// Número 2: A través del ciclo for in
console.log("// Distintas formas de imprimir un objeto: forma 2");
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

// Número 3: La función Object.values()
console.log("// Distintas formas de imprimir un objeto: forma 3");
let personaArray = Object.values(persona);
console.log(personaArray);

// Número 4: Utilizaremos el método JSON.stringify
console.log("// Distintas formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);