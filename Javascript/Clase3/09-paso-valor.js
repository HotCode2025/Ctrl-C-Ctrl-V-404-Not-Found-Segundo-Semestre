//Tipos primitivos
let k = 10;

function cambiarValor(a){ //Paso por valor
    a = 20; //cambia valor de a, no de x
}

cambiarValor(k);

console.log(k); //muestra 10, no 20