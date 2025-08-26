let sumar = function(a,b){
    console.log(arguments[0]); //muestra parametro a
    console.log(arguments[1]); //muestra parametro b
    return a + b + arguments[2]; //suma a, b y tercer argumento
}

let resultado = sumar(3, 2, 9);
console.log(resultado); //muestra resultado de la suma