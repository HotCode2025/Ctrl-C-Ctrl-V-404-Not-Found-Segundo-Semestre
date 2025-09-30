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
    constructor(departamento) {// falta constructor super (siguente archivo de la clase)
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }

}