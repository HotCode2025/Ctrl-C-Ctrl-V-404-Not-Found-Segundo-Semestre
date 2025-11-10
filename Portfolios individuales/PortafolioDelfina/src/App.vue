<script setup>
import NavBar from "./components/NavBar.vue";
import DatosPersonales from "./components/DatosPersonales.vue";
import EducacionCursos from "./components/EducacionCursos.vue";
import ExperienciasPersonales from "./components/ExperienciasPersonales.vue";
import ProyectosPersonales from "./components/ProyectosPersonales.vue";
import HabilidadesPersonales from "./components/HabilidadesPersonales.vue";
import InteresesPersonales from "./components/InteresesPersonales.vue";
</script>

<template>
  <header id="top">
    <NavBar />
    <DatosPersonales />
  </header>

  <main>
    <section id="educacion">

      <EducacionCursos />
    </section>

    <section id="experiencia">
      <h2>Experiencia</h2>
      <ExperienciasPersonales />
    </section>

    <section id="proyectos">
      <h2>Proyectos</h2>
      <ProyectosPersonales />
    </section>

    <section id="habilidades">

      <HabilidadesPersonales />
    </section>

    <section id="intereses">
      <h2>Intereses</h2>
      <InteresesPersonales />
    </section>
  </main>

  <footer>
    <a href="#top">Inicio</a>
    <p>© 2025 Delfina Mulinetti</p>
  </footer>
</template>

<style scoped>
footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    font-size: 1.3rem;
}
</style>
