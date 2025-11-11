<script setup>
import { ref, computed } from 'vue'
const arreglo = ref([
  { id: 1, fecha: "2025", titulo: "Tecnicatura en Programación", descripcion: "Aprendizaje de Python, PSeInt, Git Bash y Java. Proyecto de portafolio en Vue" },
  { id: 2, fecha: "2022", titulo: "Contador Público Nacional", descripcion: "Cursada completa hasta cuarto año. Formación en contabilidad, impuestos, sistemas administrativos y análisis de datos. Decidí no finalizar la carrera al descubrir que mi verdadera vocación está en el mundo de la tecnología y el desarrollo de software, donde hoy me estoy formando activamente." },
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
  min-height: 300px;
  color: white;
  background-color:#523F55;
  padding: 20px;
  border-radius: 10px;
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
  background:#DEAAE6 ;
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
  background: #FFF;
}

.info-container {
  text-align: center;
  max-width: 600px;
  background: #523F55;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.5);
  transition: background 0.3s;
}

.info-container h2 {
  margin-bottom: 10px;
  color: white;
}

.info-container p {
  color: white;
}

p {
  color: white;
}

h2 {
  color: white;
}

body {
  background-color: #0d1117; 

}
</style>
