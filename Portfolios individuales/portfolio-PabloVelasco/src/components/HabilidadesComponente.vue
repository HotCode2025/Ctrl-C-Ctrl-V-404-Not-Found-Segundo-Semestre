<script setup>
import img1 from '/src/components/icons/js.svg';
import img2 from '/src/components/icons/python.svg';
import img3 from '/src/components/icons/html-css.svg';
import img4 from '/src/components/icons/java.svg';
import img5 from '/src/components/icons/typescript.svg';
import img6 from '/src/components/icons/react.svg';
import img7 from '/src/components/icons/vue.svg';
import img8 from '/src/components/icons/node.svg';
import img9 from '/src/components/icons/next.svg';
import img10 from '/src/components/icons/next.svg';
import img11 from '/src/components/icons/git.svg';
import img12 from '/src/components/icons/docker.svg';
import img13 from '/src/components/icons/nest.svg';
import img14 from '/src/components/icons/figma.svg';
import img15 from '/src/components/icons/visual.svg';
import img16 from '/src/components/icons/mongo.svg';
import img17 from '/src/components/icons/mysql.svg';
import img18 from '/src/components/icons/postman.svg';
import img19 from '/src/components/icons/arg.svg';
import img20 from '/src/components/icons/eeuu.svg';
import img21 from '/src/components/icons/brasil.svg';
import img22 from '/src/components/icons/swagger.svg';



//Se importa ref de vue para poder usarlo
import { ref } from 'vue';
//Se crea un array de objetos con las habilidades
//Este es un array de objetos con habilidades que se pueden modificar o agregar
const habilidades = ref([
    {// Se crea un objeto con id, nombre y habilidades
        id: 1, nombre: 'Lenguajes de Programación', habilidades: [
            //Se crea un objeto con id, nombre, nivel e icono
            { id: 1, nombre: 'JavaScript', nivel: 'Avanzado', icono: img1 },
            { id: 2, nombre: 'Python', nivel: 'Intermedio', icono: img2 },
            { id: 3, nombre: 'HTML/CSS', nivel: 'Avanzado', icono: img3 },
            { id: 4, nombre: 'Java', nivel: 'Avanzado', icono: img4 },
            { id: 5, nombre: 'Typescript', nivel: 'Avanzado', icono: img5 },
        ]
    },
    {
        id: 2, nombre: 'Frameworks y Librerías', habilidades: [
            { id: 1, nombre: 'React.js', nivel: 'Avanzado', icono: img6 },
            { id: 2, nombre: 'Next.js', nivel: 'Avanzado', icono: img10 },
            { id: 3, nombre: 'Vue.js', nivel: 'Intermedio', icono: img7 },
            { id: 4, nombre: 'Node.js', nivel: 'Avanzado', icono: img8 },
            { id: 5, nombre: 'Express.js', nivel: 'Avanzado', icono: img8 },
            { id: 6, nombre: 'Nest.js', nivel: 'Intermedio', icono: img13 },
            { id: 7, nombre: 'Java', nivel: 'Avanzado', icono: img9 },
            { id: 8, nombre: 'Tailwind Css', nivel: 'Avanzado', icono: img10 }
        ]
    },
    {
        id: 3, nombre: 'Herramientas y Software', habilidades: [
            { id: 1, nombre: 'Git', nivel: 'Avanzado', icono: img11 },
            { id: 2, nombre: 'Docker', nivel: 'Intermedio', icono: img12 },
            { id: 3, nombre: 'Postman', nivel: 'Intermedio', icono: img18 },
            { id: 4, nombre: 'Swagger ui', nivel: 'Intermedio', icono: img22 },
            { id: 5, nombre: 'Figma', nivel: 'Intermedio', icono: img14 },
            { id: 6, nombre: 'Jira', nivel: 'Intermedio', icono: img15 },
            { id: 7, nombre: 'Markdown', nivel: 'Avanzado', icono: img15 }
        ]
    },
    {
        id: 4, nombre: 'Bases de Datos', habilidades: [
            { id: 1, nombre: 'MongoDB', nivel: 'Intermedio', icono: img16 },
            { id: 2, nombre: 'MySQL', nivel: 'Avanzado', icono: img17 },
            { id: 3, nombre: 'PostgreSQL', nivel: 'Intermedio', icono: img18 }
        ]
    },
    {
        id: 5, nombre: 'Idiomas', habilidades: [
            { id: 1, nombre: 'Español', nivel: 'Nativo', icono: img19 },
            { id: 2, nombre: 'Inglés', nivel: 'Avanzado (C1)', icono: img20 },
            { id: 3, nombre: 'Portugués', nivel: 'Intermedio (A2)', icono: img21 }
        ]
    }
]);

</script>


<template>
    <!--Este componente vue funciona de esta forma:-->
    <div class="skills-contenedor bg-gradient-animated">
        <!--Se recorre el array habilidades con v-for y se asigna la key habilidad.id-->
        <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
            <!--Se muestra el nombre de la habilidad-->
            <h3>{{ habilidad.nombre }}</h3>
            <ul class="skills">
                <!--Se recorre el array habilidades con v-for y se asigna la key habilidad.id-->
                <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">
                    <!--Se muestra el icono de la habilidad y el nombre de la habilidad con su nivel-->
                    <img :src="habilidad.icono" :alt="habilidad.nombre">
                    <!--Se muestra el icono de la habilidad y el nombre de la habilidad con su nivel-->
                    <span>{{ habilidad.nombre }}: {{ habilidad.nivel }}</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.skills-contenedor {
    padding: 2rem;
    border-radius: 10px;
    background: linear-gradient(-45deg, #021526, #03346E, #6EACDA, #E2E2B6);
}

.skills-categoria {
    margin-bottom: 20px;
}

.skills-categoria h3 {
    display: flex;
    justify-content: left;
    margin-bottom: 10px;
    font-size: 1.5em;
    color: aliceblue;
    font-size: 1.5em;
    font-weight: bold;
}

.skills {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    gap: 20px;
}

.skill {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    background-color: rgba(241, 245, 243, 0.856);
    padding: 0.3em;
    border-radius: 8px;
    box-shadow: 0px 4px 12px rgba(2, 151, 151, 0.963);
    flex: 1 1 200px;
    max-width: 250px;
}

.skill img {
    width: 35px;
    height: 35px;
}

.skill span {
    font-size: 1em;
    color: #333;
}

/* Overrides SOLO para MODO CLARO: mantener modo oscuro intacto */
@media (prefers-color-scheme: light) {
    .skills-contenedor {
        /* Dejamos ver el fondo degradado animado de la clase global */
        border-radius: 10px;
    }

    .skills-categoria h3 {
        color: #333;
    }

    .skill {
        background-color: #f9f9f9;
        border: 2px solid #ddd;
        box-shadow: none;
    }

    .skill span {
        color: #333;
    }
}

@media (max-width: 768px) {
    .skills-categoria h3 {
        justify-content: center;
    }

    .skill {
        justify-content: center;
    }
}
</style>