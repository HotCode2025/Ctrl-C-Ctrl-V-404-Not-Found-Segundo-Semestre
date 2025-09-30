//no se puede crear un objeto antes de la declaración de la clase
// let person3 = new Persona('Ana', 'Martínez'); // persona is not defined

class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set nombre(nombre){
        this._nombre = nombre.toUpperCase();
    }
    set apellido(apellido){
        this._apellido = apellido.toUpperCase();
    }
}

const persona1 = new Persona('Juan', 'Pérez');
console.log(persona1.nombre);
console.log(persona1.apellido);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
persona1.apellido = 'López';
console.log(persona1.apellido);

const persona2 = new Persona('María', 'Gómez');
console.log(persona2.nombre);
console.log(persona2.apellido);
persona2.nombre = 'María José';
console.log(persona2.nombre); 
persona2.apellido = 'Rodríguez';
console.log(persona2.apellido);