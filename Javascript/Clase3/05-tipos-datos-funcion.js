function miFuncionDos(a, b){
    console.log(arguments); //muestra argumentos e índice
}

miFuncionDos(5, 7); 
function miFuncionTres(a, b){
    console.log(arguments.length); //muestra cantidad de argumentos
}

miFuncionDos(5, 7, 3, 6); 

//toString
var miFuncionTexto = miFuncionTres.toString(); //convierte función a texto
console.log(miFuncionTexto);