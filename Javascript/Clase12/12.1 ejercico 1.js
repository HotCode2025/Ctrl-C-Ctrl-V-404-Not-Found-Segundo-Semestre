/*La clase de hoy ser trata de crear una función en el lenguaje de JavaScript, 
esta función nos tiene que solucionar el ingreso de una contraseña del usuario, 
la cuál debe ser correcta:*/

// Ejercicio 1: Función que valide una contraseña (mínimo 8 caracteres, 1 número, 1 mayúscula)

function validatePassword(password) {

    return /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/.test(password);

}

console.log(validatePassword("Abc12345")); // true

console.log(validatePassword("weak")); // false