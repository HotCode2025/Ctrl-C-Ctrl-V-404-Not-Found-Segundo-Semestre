class Persona { //Clase padre
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

class Empleado extends Persona { //Clase hija
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido); //Llama al constructor de la clase padre
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }

}

const empleado1 = new Empleado('Diego', 'Pérez', 'Sistemas');
console.log(empleado1);