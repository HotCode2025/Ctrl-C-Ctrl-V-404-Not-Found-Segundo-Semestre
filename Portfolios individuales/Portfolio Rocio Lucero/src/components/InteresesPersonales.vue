<script setup>
import { ref } from "vue";
import FondoLava from "./FondoLava.vue";

const intereses = ref([
    "Desarrollo y Programación: Apasionada por el mundo del desarrollo de software, actualmente me encuentro estudiando la Tecnicatura Universitaria en Programación. Me interesa seguir profundizando en lenguajes como JavaScript y SQL, aplicando buenas prácticas y buscando soluciones eficientes a desafíos técnicos.",
    "Sistemas ERP y Análisis de Datos: Con más de cinco años de experiencia en soporte e implementación de Tango Gestión, disfruto optimizar procesos administrativos y contables mediante herramientas tecnológicas. Me motiva integrar mis conocimientos técnicos con la comprensión del funcionamiento empresarial para mejorar la toma de decisiones.",
    "Aprendizaje y Crecimiento Profesional: Me caracteriza la curiosidad constante y el interés por la innovación. Busco seguir desarrollando mis habilidades en desarrollo web, automatización y gestión de datos, participando en proyectos que aporten valor real a las organizaciones.",
    "Vida Activa y Bienestar: Creo en mantener un equilibrio entre el trabajo y el bienestar personal. En mi tiempo libre practico gimnasio y danza, actividades que me ayudan a mantenerme enfocada, disciplinada y con energía para mis proyectos profesionales."
]);
</script>

<template>
    <div class="intereses-contenedor">
        <FondoLava />
        <ul class="contenedor-lista">
            <li class="item" v-for="interes in intereses" :key="interes">
                <span class="subtitulo">{{ interes.split(':')[0] }}:</span>
                <span class="descripcion">{{ interes.split(':')[1].trim() }}</span>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.intereses-contenedor {
    display: flex;
    flex-direction: column;
    position: relative;
    margin: 0 auto;
    max-width: 85%;
    padding: 1rem;
}

.contenedor-lista {
    list-style-type: none;
    padding: 0;
    margin: 0;
    color: var(--vt-c-white-soft);
    font-size: 1.1rem;
}

.item {
    margin-bottom: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
}

/* Subtítulos con color destacado */
.subtitulo {
    font-weight: bold;
    color: black; 
    font-size: 1.15rem;
}

/* Descripción */
.descripcion {
    background: #523F55; 
    padding: 0.5rem 0.8rem;
    border-radius: 8px;
    line-height: 1.5;
    color: var(--vt-c-white-soft);
}

/* Responsive */
@media (max-width: 768px) {
    .subtitulo { font-size: 1rem; }
    .descripcion { font-size: 0.95rem; padding: 0.4rem 0.6rem; }
}

</style>

