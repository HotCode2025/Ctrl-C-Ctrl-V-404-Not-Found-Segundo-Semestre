<script setup>
import { ref, computed } from 'vue'
const arreglo = ref([
  { id: 1, fecha: "2025", titulo: "Tecnicatura en Programación", descripcion: "Aprendizaje de Python, PSeInt, Git Bash y Java. Proyecto de portafolio en Vue" },
  { id: 2, fecha: "2020", titulo: "Egreso Terciario", descripcion: "Profesor en Tecnologías. Curso de impresoras 3D" },
  { id: 3, fecha: "2014", titulo: "Egreso Escuela Técnica", descripcion: "Escuela Técnica en Enología" },
])

const reversedArreglo = computed(() => [...arreglo.value].sort((a,b) => a.fecha - b.fecha))
const selectedItem = ref(arreglo.value[0])
</script>

<template>
  <div class="timeline-container">    
    <div class="circle-container">
      <div
        v-for="item in reversedArreglo"
        :key="item.id"
        class="year-dot"
        @mouseenter="selectedItem = item"
      >
        {{ item.fecha }}
      </div>
    </div>
    
    <div class="info-container">
      <h2>{{ selectedItem.titulo }}</h2>
      <p>{{ selectedItem.descripcion }}</p>
    </div>
  </div>
</template>

<style scoped>
.timeline-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  color: white;
  background-color: #111;
  padding: 20px;
  font-family: 'Poppins', sans-serif;
}

.circle-container {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-bottom: 40px;
}

.year-dot {
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, #3fb37b, #3fb37b);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-weight: bold;
  color: #fff;
  transition: transform 0.3s, background 0.3s;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

.year-dot:hover {
  transform: scale(1.3);
  background: linear-gradient(135deg, rgba(95, 124, 205, 0.934), rgba(95, 124, 205, 0.934));
}

.info-container {
  text-align: center;
  max-width: 600px;
  background: rgba(255,255,255,0.05);
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.5);
  transition: background 0.3s;
}

.info-container h2 {
  margin-bottom: 10px;
  color: rgba(95, 124, 205, 0.934);
}

.info-container p {
  color: #ccc;
}
</style>
