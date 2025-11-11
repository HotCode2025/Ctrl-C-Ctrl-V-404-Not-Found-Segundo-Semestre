<script setup>
import icono1 from "/src/assets/edicion-de-video.png";
import icono4 from "/src/assets/desarrollo-web.png";
import { ref } from "vue";

const titulo = "Realización audiovisual y edición de video";
const fecha = "Desde 2017 / 2025";
const experiencias = ref([
  {
    id: 1,
    src: icono1,
    parrafo:
      "Edición de video freelancer: 2023 - Actualidad. Edición de video de múltiples formatos para redes sociales.",
  },
  {
    id: 2,
    src: icono4,
    parrafo:
      "Desarrollo web en Wordpress: 2023 - 2024. Desarrollo web en una empresa específica y como freelancer para personas particulares.",
  },
]);
</script>

<template>
  <div class="card">
    <h3 class="titulo">{{ titulo }}</h3>
    <p class="fecha">{{ fecha }}</p>
    <ul class="listado">
      <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
        <img
          class="imagen-svg"
          :src="experiencia.src"
          width="45"
          :alt="experiencia.parrafo"
        />
        <p>{{ experiencia.parrafo }}</p>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
  padding: 2rem;
  border-radius: 15px;
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.25);
  color: #fff;
  transition: all 0.3s ease;
}

.card:hover {
  background: rgba(255, 255, 255, 0.18);
  transform: translateY(-3px);
}

.titulo {
  font-size: 1.5rem;
  margin-bottom: 0.2rem;
  color: white;
}

.fecha {
  font-size: 1rem;
  color: #fcfcfc;
  margin-bottom: 1rem;
  font-weight: 500;
}

.listado {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.item {
  display: flex;
  align-items: center;
  gap: 1.2rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  padding: 1rem;
  transition: background 0.3s ease;
}

.item:hover {
  background: rgba(255, 255, 255, 0.15);
}

.imagen-svg {
  filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.2));
}
</style>
