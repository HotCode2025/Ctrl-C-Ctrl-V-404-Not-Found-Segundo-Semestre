<script setup>
import { ref } from "vue";
import FondoLava from "./FondoLava.vue";

const intereses = ref([
  "Desarrollo web: Interés en crear soluciones tecnológicas útiles para empresas y personas, desarrollando aplicaciones que resuelvan problemas reales y mejoren la productividad. Me motiva el impacto práctico que puede tener un buen software en la vida cotidiana.",
  "IA: Apasionada por la inteligencia artificial y su aplicación en el desarrollo web y de software. Disfruto aprender nuevas herramientas y mantenerme al día con las tendencias que impulsan la evolución tecnológica.",
  "Diseño web: Me gusta combinar la lógica del código con la estética visual, explorando el diseño web y la experiencia de usuario. Busco que cada interfaz sea funcional, moderna y atractiva.",
  "Vida personal: Encuentro equilibrio y energía en actividades como la música, el gimnasio y el cine, que estimulan tanto mi cuerpo como mi creatividad."
]);
</script>

<template>
  <div class="intereses-contenedor">
    <FondoLava />
    <ul class="contenedor-lista">
      <li class="item" v-for="interes in intereses" :key="interes">
        <div class="card">
          <h3 class="subtitulo">{{ interes.split(':')[0] }}</h3>
          <p class="descripcion">{{ interes.split(':')[1].trim() }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.intereses-contenedor {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  margin: 0 auto;
  max-width: 85%;
  padding: 2rem;
  z-index: 1;
}

.titulo {
  font-size: 2rem;
  color: #ffffff;
  margin-bottom: 1.5rem;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
  letter-spacing: 1px;
}

/* Lista general */
.contenedor-lista {
  list-style: none;
  padding: 0;
  margin: 0;
  width: 100%;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

/* Tarjetas */
.card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  border-radius: 16px;
  padding: 1.2rem 1.5rem;
  color: var(--vt-c-white-soft);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.15);
}

.card:hover {
  transform: translateY(-6px) scale(1.02);
  box-shadow: 0 6px 25px rgba(255, 255, 255, 0.15);
  background: rgba(255, 255, 255, 0.15);
}

/* Subtítulo */
.subtitulo {
  font-weight: 600;
  color: #fff;
  margin-bottom: 0.4rem;
  font-size: 1.25rem;
}

/* Descripción */
.descripcion {
  line-height: 1.5;
  font-size: 1rem;
  color: #e9e9e9;
}

/* Responsive */
@media (max-width: 768px) {
  .titulo {
    font-size: 1.6rem;
  }

  .subtitulo {
    font-size: 1.1rem;
  }

  .descripcion {
    font-size: 0.95rem;
  }
}
</style>
