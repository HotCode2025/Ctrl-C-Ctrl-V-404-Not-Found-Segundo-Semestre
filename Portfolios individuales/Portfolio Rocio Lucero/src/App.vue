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
    <!--Barra de Navegación-->
    <NavBar /> 
    <!--Componente Datos Personales-->
    <DatosPersonales />   
  </header>

  <main>
    <!--Componente Educacion-->
    <section id="educacion">
      <h2>Estudios</h2>
    <EducacionCursos />
    </section>

    <!--Componente Experiencias-->    
    <section id="experiencia">
      <h2>Experiencia laboral</h2>
    <ExperienciasPersonales />
    </section>

    <!--Componente Proyectos--> 
    <section id="proyectos">
      <h2>Proyectos</h2>
      <ProyectosPersonales />
    </section>
    
    <!--Componente Habilidades--> 
    <section id="habilidades">
      <h2>Habilidades</h2></section>
      <HabilidadesPersonales />

    <!--Componente Intereses--> 
    <section id="intereses">
      <h2>Intereses</h2></section>
      <InteresesPersonales />
    
  </main>
  <footer>
    <a href="#top">Inicio</a>
    <p>© 2025 Rocio Lucero - PortafolioWEB</p>
  </footer>
</template>

<style scoped>
footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    font-size: 1.33rem;
}

body {
    background-color: white;
}
</style>


