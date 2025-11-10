<script setup>
import Header from './components/Header.vue'
import AboutMe from './components/AboutMe.vue'
import Skills from './components/Skills.vue' // <-- Nuevo
import Projects from './components/Projects.vue'
</script>

<template>
  <div id="portfolio-app">
    <Header />
    <main>
      <AboutMe />
      <Skills />    <Projects />
      </main>
  </div>
</template>

<style>
/* Estilos globales */
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