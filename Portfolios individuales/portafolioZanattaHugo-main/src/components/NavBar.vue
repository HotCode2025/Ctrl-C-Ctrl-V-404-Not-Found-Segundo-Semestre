<template>
  <nav class="navbar">
    <div class="navbar-menu">
      <!-- Inicio -->
      <a @click.prevent="scrollToSection('top')" class="nav-item">Inicio</a>

      <!-- Resto de la navegación -->
      <a
        v-for="nav in navegacion"
        :key="nav.nombre"
        @click.prevent="scrollToSection(nav.enlace.substring(1))"
        class="nav-item"
      >
        {{ nav.nombre }}
      </a>
    </div>
  </nav>
</template>

<script setup>
import { ref } from "vue";

const navegacion = ref([
    {id:1, nombre:"Educacion", enlace:"#educacion"},
    {id:2, nombre:"Experiencia", enlace:"#experiencia"},
    {id:3, nombre:"Proyectos", enlace:"#proyectos"},
    {id:4, nombre:"Intereses", enlace:"#intereses"},
    {id:5, nombre:"Habilidades", enlace:"#habilidades"}
]);

// Función de scroll con offset para que la barra no tape los títulos
function scrollToSection(id) {
  const element = document.getElementById(id);
  if (!element) return;

  const navbarHeight = 60; // altura aproximada de la barra
  const elementPosition = element.getBoundingClientRect().top + window.scrollY;
  const offsetPosition = elementPosition - navbarHeight;

  window.scrollTo({
    top: offsetPosition,
    behavior: "smooth"
  });
}
</script>

<style scoped>
.navbar {
    position: fixed;
    top: 0;               
    left: 0;
    width: 100%;          
    z-index: 999;         
    background-color: rgba(17, 17, 27, 0.85); /* transparente */
    color: #fff;
    padding: 0.5rem 2rem;
    display: flex;
    justify-content: center;
    backdrop-filter: blur(8px); /* efecto vidrio */
    box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    transition: background-color 0.3s ease;
}

.navbar-menu {
    display: flex;
    justify-content: flex-end;
    width: 100%;
    max-width: 1200px;
}

a.nav-item {
    border: 1px solid hsla(160, 100%, 37%, 0.2);
    border-radius: 50px;
    text-decoration: none;
    transition: 0.4s;
    padding: 5px 10px;
    margin-left: 0.8rem;
    color: #fff;
    font-weight: 500;
    backdrop-filter: blur(4px);
}

a.nav-item:hover {
    background-color: hsla(160, 100%, 37%, 0.3);
}

/* Responsive */
@media (max-width: 768px) {
    .navbar-menu {
        justify-content: center;
    }
    a.nav-item {
        padding: 5px 8px;
        font-size: 0.95rem;
    }
}
</style>
