const autos = ['Ferrari','Renault','BMW'];

//Recorremos los elementos de un arreglo
console.log(autos[0]);//recorro manual el primer elemento
console.log(autos[2]);//recorro manual el último elemento
//ciclo for
for(let i = 0; i < autos.length; i++){
    console.log(i+' : '+autos[i]);
}