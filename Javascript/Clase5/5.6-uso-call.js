//5.6 Uso de Call
let persona4 ={
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo, tel){
        return titulo+" "+this.nombre+" "+this.apellido+" "+tel;
    },
}

//persona 5 no tiene metodo nombreCompleto2
let persona5 = {
    nombre: "Carlos",
    apellido: "Lara",
}


//llamada a nombrecompleto2 de persona4
console.log(persona4.nombreCompleto2("Lic.", "2615555555"));

//uso de call para usar el metodo nombreCompleto2 en el objeto Persona5
console.log(persona4.nombreCompleto2.call(persona5, "Ing.", "2618888888")); //se le pasa el objeto persona5 y los argumentos del metodo

