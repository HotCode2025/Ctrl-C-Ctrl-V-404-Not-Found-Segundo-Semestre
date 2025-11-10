<script setup>
import img1 from '/src/components/icons/javascript.svg';
import img2 from '/src/components/icons/python.svg';
import img3 from '/src/components/icons/html.svg';
import img4 from '/src/components/icons/java.svg';
import img5 from '/src/components/icons/sql.svg';
import img6 from '/src/components/icons/react.svg';
import img7 from '/src/components/icons/vue.svg';
import img8 from '/src/components/icons/node.svg';
import img9 from '/src/components/icons/git.svg';
import img10 from '/src/components/icons/docker2.svg';
import img11 from '/src/components/icons/jenkins.svg';
import img12 from '/src/components/icons/figma.svg';
import img13 from '/src/components/icons/visual-studio-code.svg';
import img14 from '/src/components/icons/mongodb.svg';
import img15 from '/src/components/icons/mysql-logo.svg';
import img16 from '/src/components/icons/postgresql.svg';
import img17 from '/src/components/icons/lenguage.svg';
import img18 from '/src/components/icons/lenguages.svg';


import { ref } from 'vue';
const habilidades = ref([
    {
        id: 1, nombre: 'Lenguajes de Programación', habilidades: [
            //Se crea un objeto con id, nombre, nivel e icono
            { id: 1, nombre: 'JavaScript', nivel: 'Avanzado', icono: img1 },
            { id: 2, nombre: 'Python', nivel: 'Intermedio', icono: img2 },
            { id: 3, nombre: 'HTML/CSS', nivel: 'Avanzado', icono: img3 },
            { id: 4, nombre: 'Java', nivel: 'Intermedio', icono: img4 },
            { id: 5, nombre: 'SQL', nivel: 'Básico', icono: img5 }
        ]
    },
    {
        id: 2, nombre: 'Frameworks y Librerías', habilidades: [
            { id: 1, nombre: 'React.js', nivel: 'Avanzado', icono: img6 },
            { id: 2, nombre: 'Vue.js', nivel: 'Intermedio', icono: img7 },
            { id: 3, nombre: 'Node.js', nivel: 'Intermedio', icono: img8 }            
        ]
    },
    {
        id: 3, nombre: 'Herramientas y Software', habilidades: [
            { id: 1, nombre: 'Git', nivel: 'Avanzado', icono: img9 },
            { id: 2, nombre: 'Docker', nivel: 'Intermedio', icono: img10 },
            { id: 3, nombre: 'Jenkins', nivel: 'Intermedio', icono: img11 },
            { id: 4, nombre: 'Figma', nivel: 'Intermedio', icono: img12 },
            { id: 5, nombre: 'Visual Studio Code', nivel: 'Avanzado', icono: img13 }
        ]
    },
    {
        id: 4, nombre: 'Bases de Datos', habilidades: [
            { id: 1, nombre: 'MongoDB', nivel: 'Avanzado', icono: img14 },
            { id: 2, nombre: 'MySQL', nivel: 'Intermedio', icono: img15 },
            { id: 3, nombre: 'PostgreSQL', nivel: 'Intermedio', icono: img16 }
        ]
    },
    {
        id: 5, nombre: 'Idiomas', habilidades: [
            { id: 1, nombre: 'Español', nivel: 'Nativo', icono: img17 },
            { id: 2, nombre: 'Inglés', nivel: 'Avanzado (C1)', icono: img18 }
        ]
    }
]);

</script>

<template>     
    <div class="skills-contenedor">
        
        <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">            
            <h3>{{ habilidad.nombre }}</h3>
            <ul class="skills">                
                <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">                   
                    <img :src="habilidad.icono" :alt="habilidad.nombre">                    
                    <span>{{ habilidad.nombre }}: {{ habilidad.nivel }}</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.skills-contenedor {
    padding: 2rem;    
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

.skill:hover {
    background-color: rgba(2, 151, 151, 0.963);
}

.skill img {
    width: 35px;
    height: 35px;
}

.skill span {
    font-size: 1em;
    color: #333;
}

.skill:hover {
    font-size: 1.3em;
    transition: 2s ease;
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