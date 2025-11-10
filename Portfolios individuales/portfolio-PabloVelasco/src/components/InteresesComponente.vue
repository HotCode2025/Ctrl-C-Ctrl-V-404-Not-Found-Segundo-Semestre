<script setup>
import { ref } from 'vue'
//Este es un arreglo con ref para que se pueda reactivar el cambio de los intereses
const intereses = ref([
  'Aprendizaje autodidácta: Me encanta aprender nuevas cosas por mi cuenta, ya sea a través de libros, tutoriales en línea, o simplemente investigando sobre temas que me interesan.',
  'Desarrollo de software: Me apasiona crear soluciones tecnológicas para problemas reales. Disfruto trabajando en proyectos personales y colaborando con otros desarrolladores para mejorar herramientas y librerías populares.',
  'Música: Disfruto escuchar música de diferentes géneros, como rock, electrónica, y practicar la guitarra.',
  'Turismo: Disfruto viajar y explorar diferentes lugares, lo que me ayuda a mantenerme en forma y a conectar con la naturaleza.',
])
</script>

<template>
  <div class="intereses-contenedor bg-gradient-animated">
    <ul class="contenedor-lista">
      <li class="item" v-for="interes in intereses" :key="interes">
        {{ interes }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.intereses-contenedor {
    background-color: rgb(28, 41, 52);
  display: flex;
  position: relative;
  margin: 0 auto;
  max-width: 85%;
  border-radius: 10px;
  padding: 10px 50px;
}

.contenedor-lista {
  list-style-type: none;
  padding: 1rem;
  margin-bottom: 0.5rem;
  color: var(--vt-c-white-soft);
  font-size: 1.4rem;
  text-shadow: 3px 3px 6px rgba(0, 0, 0, 1);
}

.item {
  margin-bottom: 1rem;
}

/* Overrides SOLO para MODO CLARO: mantener modo oscuro intacto */
@media (prefers-color-scheme: light) {
  .intereses-contenedor {
    /* Dejamos ver el fondo degradado animado de la clase global */
    background-color: transparent;
    border: 2px solid #ddd;
  }

  .contenedor-lista {
    color: #1f2937; /* texto oscuro para alto contraste */
    text-shadow: none;
    /* Añadimos una capa translúcida para asegurar legibilidad sobre el gradiente */
    background: rgba(255, 255, 255, 0.78);
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
    backdrop-filter: saturate(160%) blur(6px);
  }
}
</style>
