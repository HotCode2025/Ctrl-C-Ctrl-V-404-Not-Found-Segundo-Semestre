<script setup>
import Header from './components/Header.vue'
import Projects from './components/Projects.vue'
// Aquí puedes importar más componentes (Sobre Mí, Habilidades, Contacto)
</script>

<template>
  <div id="portfolio-app">
    <Header />
    <main>
      <Projects />
      </main>
  </div>
</template>

<style>
/* Estilos globales para la aplicación */
#portfolio-app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
body {
  margin: 0;
  padding: 0;
  background-color: #ecf0f1;
}
</style>