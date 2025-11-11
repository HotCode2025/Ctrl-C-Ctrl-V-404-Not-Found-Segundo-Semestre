<script setup>
import { ref, computed } from 'vue'

const arreglo = ref([
  { id: 1, fecha: "2025", titulo: "Tecnicatura en Programación", descripcion: "En curso" },
  { id: 2, fecha: "2020", titulo: "Licenciatura en Diseño y Producción Audiovisual", descripcion: "Carrera en Cine y TV" },
])

// Orden ascendente por año
const reversedArreglo = computed(() => [...arreglo.value].sort((a, b) => a.fecha - b.fecha))
const selectedItem = ref(arreglo.value[0])
</script>

<template>
  <div class="timeline-container">
    <h2 class="titulo">Formación Académica</h2>

    <div class="circle-container">
      <div
        v-for="item in reversedArreglo"
        :key="item.id"
        class="year-dot"
        :class="{ active: selectedItem.id === item.id }"
        @mouseenter="selectedItem = item"
      >
        {{ item.fecha }}
      </div>
    </div>

    <transition name="fade">
      <div class="info-container" :key="selectedItem.id">
        <h3>{{ selectedItem.titulo }}</h3>
        <p>{{ selectedItem.descripcion }}</p>
      </div>
    </transition>
  </div>
</template>

<style scoped>
.timeline-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 1.5rem;
  color: #fff;
  font-family: 'Poppins', sans-serif;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(12px);
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}

.titulo {
  font-size: 2rem;
  margin-bottom: 2rem;
  text-shadow: 0 0 10px rgb(255, 255, 255);
}

.circle-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 40px;
  margin-bottom: 40px;
}

.year-dot {
  width: 60px;
  height: 60px;
  background: radial-gradient(circle at 30% 30%, #4b6bff, #001b44);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-weight: 600;
  color: #fff;
  transition: all 0.3s ease;
  box-shadow: 0 0 15px rgba(75, 107, 255, 0.3);
}

.year-dot:hover {
  transform: scale(1.2);
  box-shadow: 0 0 25px rgba(75, 107, 255, 0.8);
}

/* Estado activo */
.year-dot.active {
  background: radial-gradient(circle at 30% 30%, #7a91ff, #0026ff);
  box-shadow: 0 0 25px rgba(130, 160, 255, 0.9);
  transform: scale(1.1);
}

.info-container {
  text-align: center;
  max-width: 600px;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(8px);
  padding: 25px;
  border-radius: 15px;
  box-shadow: 0 0 25px rgba(0, 0, 0, 0.4);
  transition: all 0.4s ease;
}

.info-container h3 {
  color: #fdfeff;
  margin-bottom: 10px;
  font-size: 1.4rem;
}

.info-container p {
  color: #dcdcdc;
  font-size: 1.05rem;
}

/* Transición suave del texto */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

@media (max-width: 768px) {
  .titulo {
    font-size: 1.6rem;
  }
  .year-dot {
    width: 50px;
    height: 50px;
  }
}
</style>
