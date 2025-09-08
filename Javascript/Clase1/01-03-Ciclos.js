//While

let contador = 0;
while (contador < 3 ){
    contador ++;
}
console.log ("Fin del ciclo while");


// Do while 
let conteo = 0;
do {
conteo++;
}while (conteo < 3);
console.log("fin del ciclo do while");

//for 
for (let contando = 0; contando < 3; contando ++){
    console.log(contando) 
    }
console.log ("fin del ciclo flor") ;

// palabra reservada break

for(let contando = 0; contando <= 10; contando ++){
    if(contando % 2 == 0) {
 console.log(contando);       
    }
}
console.log ("Termina el ciclo al encontrar los pares");

// palabra resverda brack 2 "primer numero"
for(let contando = 0; contando <= 10; contando ++){
    if(contando % 2 == 0) {
 console.log(contando);   
 break    
    }
}
console.log ("Termina el ciclo al encontrar el primer número");



// La palabra continue REVISAR
for(let contando = 0; contando <= 10; contando ++){
    if(contando % 2 !== 0) {
 continue; 
    }
    console.log (contando);
}
console.log ("Termina el ciclo");

// La palabra continue y etiquetas label 
inicio:
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 !== 0) {
        break inicio;
    }
    console.log(contando);
}
console.log("Termina el ciclo");