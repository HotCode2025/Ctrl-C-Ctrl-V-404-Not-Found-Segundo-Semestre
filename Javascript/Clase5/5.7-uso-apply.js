//5.7 Uso de Apply
let persona4 ={
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo, telefono){
        return titulo+" "+this.nombre+" "+this.apellido+" "+telefono;
    },
}

//persona 5 no tiene metodo nombreCompleto2
let persona5 = {
    nombre: "Carlos",
    apellido: "Lara",
}

console.log(persona4.nombreCompleto2("Lic.", "2615555555"));

//Metodo Apply
let arreglo = ["Ing.", "2618888888"];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo)); //se le pasa el objeto persona5 y un arreglo con los argumentos del metodo

