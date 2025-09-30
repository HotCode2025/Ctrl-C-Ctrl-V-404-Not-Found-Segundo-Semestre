class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }
}

const persona1 = new Persona('Juan', 'Pérez');
console.log(persona1);

const persona2 = new Persona('María', 'Gómez');
console.log(persona2); 