<script setup>
import { ref } from "vue";
import FondoLava from "./FondoLava.vue";

const intereses = ref([
    "Desarrollo de Software de Código Abierto: Interés en colaborar en proyectos de código abierto y en comunidades de desarrollo, especialmente relacionados con JavaScript, Python y Vue.",
    "Tecnología e Innovación: Apasionado por las nuevas tendencias en inteligencia artificial, desarrollo web y automatización. Me motiva aprender y experimentar con herramientas modernas del ecosistema tecnológico.",
    "Creatividad y Diseño: Disfruto aplicar el lado visual de la tecnología, explorando diseño de interfaces y herramientas como Figma para crear experiencias agradables y funcionales.",
    "Deportes y Vida Activa: Me gusta mantener un equilibrio entre el trabajo y la vida personal a través de actividades al aire libre como ciclismo y caminatas."
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
    color: #14d37a; /* amarillo cálido que contrasta con el fondo violeta/azul */
    font-size: 1.15rem;
}

/* Descripción */
.descripcion {
    background: rgba(60, 174, 163, 0.2); /* recuadro suave */
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

