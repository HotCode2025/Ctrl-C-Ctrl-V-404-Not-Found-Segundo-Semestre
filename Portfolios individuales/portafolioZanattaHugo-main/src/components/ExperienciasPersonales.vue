<script setup>
import icono1 from "/src/assets/ProfTec.svg";
import icono2 from "/src/assets/AtnPubli.svg";
import icono3 from "/src/assets/Bodeg.svg";
import icono4 from "/src/assets/Desarrollador.svg";
import icono5 from "/src/assets/ProyectoPersonal.svg";

import {ref} from "vue";
const titulo="Profesor en Tecnologías";
const fecha="Desde2020 / 2025";
const experiencias= ref([
    {id:1, src: icono1, parrafo: "Profesor en Tecnologías (desde 2021): Diseño e implementación de clases prácticas orientadas a la comprensión de herramientas digitales y pensamiento lógico. Formación en informática básica y aplicaciones educativas."},
    {id:2, src: icono2, parrafo: "Atención al Cliente en Cadena de Supermercados y Andesmar (2020 / 2022): Asesoramiento personalizado y resolución de incidencias, priorizando la satisfacción del cliente y la eficiencia en el servicio."},
    {id:3, src: icono3, parrafo: "Encargado de Almacén en Bodega de Vinos (2022 / 2024): Gestión de inventarios, control de stock y coordinación logística interna. Implementación de mejoras en la organización del depósito y seguimiento de trazabilidad de productos."},
    {id:4, src: icono4, parrafo: "Desarrollador en formación / Tecnicatura Universitaria en Programación (2025): Creación de proyectos integradores en Python, Java y Vue.js, aplicando principios de programación estructurada y orientada a objetos."},
    {id:5, src: icono5, parrafo: "Proyecto personal: Portafolio Web Interactivo (2025): Desarrollo de un sitio personal con Vue, implementando componentes personalizados, animaciones y diseño responsivo. Integración de una línea de tiempo interactiva para mostrar formación y trayectoria."},
])
</script>

<template>
    <div class="card">
        <h3 class="titulo">{{ titulo }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
                <img class="imagen-svg" :src="experiencia.src" width="45rem" :alt="experiencia.parrafo">
                <p>{{ experiencia.parrafo }}</p>
            </li> 
            <!-- <li class="item"><img class="imagen-svg" src="/src/assets/ProfTec.svg" width="45rem" alt="">
                <p>Profesor en Tecnologías (desde 2021): Diseño e implementación de clases prácticas orientadas a la comprensión de herramientas digitales y pensamiento lógico. Formación en informática básica y aplicaciones educativas.</p>
            </li>                   
            <li class="item"><img class="imagen-svg" src="/src/assets/AtnPubli.svg" width="45rem" alt="">
                <p>Atención al Cliente en Cadena de Supermercados y Andesmar (2020 / 2022): Asesoramiento personalizado y resolución de incidencias, priorizando la satisfacción del cliente y la eficiencia en el servicio.</p>
            </li>
            <li class="item"><img class="imagen-svg" src="/src/assets/Bodeg.svg" width="45rem" alt="">
                <p>Encargado de Almacén en Bodega de Vinos (2022 / 2024): Gestión de inventarios, control de stock y coordinación logística interna. Implementación de mejoras en la organización del depósito y seguimiento de trazabilidad de productos.</p>
            </li>            
            <li class="item"><img class="imagen-svg" src="/src/assets/Desarrollador.svg" width="45rem" alt="">
                <p>Desarrollador en formación / Tecnicatura Universitaria en Programación (2025): Creación de proyectos integradores en Python, Java y Vue.js, aplicando principios de programación estructurada y orientada a objetos.</p>
            </li>
            <li class="item"><img class="imagen-svg" src="/src/assets/ProyectoPersonal.svg" width="45rem" alt="">
                <p>Proyecto personal: Portafolio Web Interactivo (2025): Desarrollo de un sitio personal con Vue, implementando componentes personalizados, animaciones y diseño responsivo. Integración de una línea de tiempo interactiva para mostrar formación y trayectoria.</p>
            </li> -->
        </ul>
    </div>
</template>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color: rgb(28, 41, 52);
    border-radius: 15px;
}

.titulo {
    font-size: 1.5rem;
    color: rgb(209, 183, 148);
}

.fecha {
    font-size: 1rem;
    color: rgb(238, 152, 40);
    margin-bottom: 1rem;
}

.listado {
    display: flex;
    flex-direction: column;
}

.item {
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
}
</style>