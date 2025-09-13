let= persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 28,
    idioma: "es",
    //Clase 5.1.2
    get lang(){
        return this.idioma.toUpperCase();
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },   
    nombreCompleto: function(){
        return this.apellido+" "+this.nombre;
    },
    //Clase 5.1.1
    // Uso de la palabra reservada get
    get nombreEdad(){
        return "El nombre es: "+this.nombre+" y la edad es: "+this.edad;
    }
}

//Clase 5.1.1
console.log("Comenzamos a utilizar el método get");
console.log(persona.nombreEdad);

//Clase 5.1.2
console.log("Comenzamos con el metodo get para idiomas");
console.log(persona.lang);

console.log("Cambiamos el idioma a través del método set");
persona.lang = "en";
console.log(persona.lang);