<template>
  <nav class="navbar">
    <div class="navbar-menu">
      <a @click.prevent="scrollToSection('top')" class="nav-item">Inicio</a>

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
  { id: 1, nombre: "Educación", enlace: "#educacion" },
  { id: 2, nombre: "Experiencia", enlace: "#experiencia" },
  { id: 3, nombre: "Proyectos", enlace: "#proyectos" },
  { id: 4, nombre: "Intereses", enlace: "#intereses" },
  { id: 5, nombre: "Habilidades", enlace: "#habilidades" }
]);

function scrollToSection(id) {
  const element = document.getElementById(id);
  if (!element) return;

  const navbarHeight = 60;
  const elementPosition = element.getBoundingClientRect().top + window.scrollY;
  const offsetPosition = elementPosition - navbarHeight;

  window.scrollTo({
    top: offsetPosition,
    behavior: "smooth"
  });
}
</script>

<style scoped>
/* --- Navbar --- */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 999;
  padding: 0.6rem 2rem;
  background: rgba(20, 20, 25, 0.65);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  display: flex;
  justify-content: center;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.35);
  animation: fadeIn 0.8s ease forwards;
}

.navbar-menu {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1rem;
  max-width: 1100px;
}

/* --- Items --- */
.nav-item {
  color: #f3f3f3;
  font-weight: 500;
  text-decoration: none;
  position: relative;
  font-size: 1rem;
  letter-spacing: 0.5px;
  padding: 6px 10px;
  transition: color 0.3s ease;
}

.nav-item::after {
  content: "";
  position: absolute;
  bottom: 2px;
  left: 0;
  width: 0%;
  height: 2px;
  background: #ffffff;
  transition: width 0.3s ease;
}

.nav-item:hover {
  color: #fff;
}

.nav-item:hover::after {
  width: 100%;
}

/* --- Animación de entrada --- */
@keyframes fadeIn {
  from {
    transform: translateY(-20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

/* --- Responsive --- */
@media (max-width: 768px) {
  .navbar-menu {
    flex-direction: column;
    align-items: center;
    gap: 0.6rem;
  }
  .nav-item {
    font-size: 0.95rem;
  }
}
</style>
