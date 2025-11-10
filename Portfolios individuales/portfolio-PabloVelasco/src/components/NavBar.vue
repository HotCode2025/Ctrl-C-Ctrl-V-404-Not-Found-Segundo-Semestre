<template>
  <nav class="navbar">
    <div class="navbar-menu">
      <ul class="nav-list">
        <!--Se coloco el operador v-bind al atributo href utilizando su minima expreción el operador : / y se soluciono el enlace a las distintas secciones-->
        <a
          v-for="nav in navegacion"
          :key="nav.nombre"
          :href="nav.enlace"
          class="nav-item"
          @click.prevent="scrollToSection(nav.enlace)"
        >
          {{ nav.nombre }}
        </a>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
const navegacion = ref([
  { id: 0, nombre: 'Inicio', enlace: '#inicio' },
  { id: 1, nombre: 'Educación', enlace: '#educacion' },
  { id: 2, nombre: 'Experiencia', enlace: '#experiencia' },
  { id: 3, nombre: 'Proyectos', enlace: '#proyectos' },
  { id: 4, nombre: 'Habilidades', enlace: '#habilidades' },
  { id: 5, nombre: 'Intereses', enlace: '#intereses' },
])

const scrollToSection = (hash) => {
  const el = document.querySelector(hash)
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' })
    // Actualiza el hash en la URL sin recargar
    history.pushState(null, '', hash)
  }
}
</script>

<style scoped>
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 4rem;
    place-content: center;
    background-color: var(--vt-c-indigo); /* Establece el color de fondo usando una variable CSS */
    color: #fff; /* Establece el color del texto en blanco */
    padding: 0.5rem 1rem; /* Añade un padding de 0.5rem arriba y abajo, y 1rem a los lados */
    align-items: center; /* Centra verticalmente los elementos dentro de la navbar */
    z-index: 1000; /* Asegura que la navbar quede por encima del contenido */
}

.navbar-item {
  color: #fff; /* Establece el color del texto en blanco */
  text-decoration: none; /* Elimina el subrayado de los enlaces */
  margin-right: 1rem; /* Añade un margen derecho de 1rem entre los elementos */
}

.navbar-menu {
  display: flex; /* Organiza los elementos en línea usando flexbox */
  justify-content: flex-end; /* Alinea los elementos al final de la navbar */
}

.nav-list {
  display: flex;
  gap: 0.5rem;
  list-style: none; /* Elimina los puntos o números de las listas */
}

a {
  border-color: hsla(160, 100%, 37%, 0.2); /* Define el color del borde usando hsla */
  border-radius: 5px; /* Redondea las esquinas del borde */
  text-decoration: none; /* Elimina el subrayado de los enlaces */
  transition: all 0.4s ease-in-out; /* Transición completa para hover/focus */
  padding: 5px; /* Añade un padding de 5px alrededor del contenido */
}

a:hover {
  background-color: hsla(
    160,
    100%,
    37%,
    0.2
  ); /* Cambia el color de fondo al pasar el mouse sobre un enlace */
}

@media (max-width: 768px) {
  .navbar-menu {
    display: flex; /* Organiza los elementos en línea usando flexbox */
    justify-content: flex-end; /* Alinea los elementos al final de la navbar */
    width: 100%; /* Asegura que la navbar ocupe el 100% del ancho en pantallas pequeñas */
  }
}
</style>
