const persona ={
    nombre: 'Juan',
    apellido: 'Lepez'
}
console.log(persona); //muestra objeto original

const cambiarValorObjeto = (p1) => {
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
}

//llamado por referencia
cambiarValorObjeto(persona);
console.log(persona); //muestra objeto modificado