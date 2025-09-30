class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }
}

const persona1 = new Persona('Juan', 'Pérez');
console.log(persona1.nombre);

const persona2 = new Persona('María', 'Gómez');
console.log(persona2.nombre); 