<template>
  <section class="projects-section" id="proyectos">
    <h2 class="title">Mis Proyectos Destacados</h2>
    <div class="project-list">
      
      <div class="project-card">
        <h3 class="project-title">Portafolio Grupal (Ctrl-C-Ctrl-V-404)</h3>
        <p class="project-description">
          Contribución al portafolio de equipo de Segundo Semestre. Desarrollé el componente de Proyectos con el diseño y lógica de datos.
        </p>
        <div class="project-tech-list">
          <span class="tech-badge">Vue.js</span>
          <span class="tech-badge">Vite</span>
          <span class="tech-badge">CSS</span>
        </div>
        <a href="https://github.com/HotCode2025/Ctrl-C-Ctrl-V-404-Not-Found-Segundo-Semestre" target="_blank" class="project-link">Ver en GitHub</a>
      </div>
      
      <div class="project-card">
        <h3 class="project-title">Sistema de Gestión en Java</h3>
        <p class="project-description">
          Simulación de gestión de inventario y pedidos, aplicando conceptos de Programación Orientada a Objetos (POO).
        </p>
        <div class="project-tech-list">
          <span class="tech-badge">Java</span>
          <span class="tech-badge">POO</span>
        </div>
        <a href="#URL_REPOSITORIO_JAVA" target="_blank" class="project-link">Ver en GitHub (Pendiente)</a>
      </div>

      </div>
  </section>
</template>

<script setup>
// No hay lógica JavaScript compleja necesaria por ahora
</script>

<style scoped>
.projects-section {
    padding: 3rem 1.5rem;
    background-color: #f4f4f9;
    text-align: center;
}
.title {
    font-size: 2.5rem;
    color: #7a54eb;
    margin-bottom: 2rem;
}
.project-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
}
.project-card {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 20px;
    width: 300px;
    text-align: left;
}
.project-title {
    font-size: 1.5rem;
    color: #b75ef3;
    margin-bottom: 10px;
}
.project-description {
    color: #ae47e1;
    margin-bottom: 15px;
}
.tech-badge {
    display: inline-block;
    background-color: #ecf0f1;
    color: #a050d2;
    padding: 5px 10px;
    border-radius: 5px;
    margin-right: 5px;
    font-size: 0.8rem;
}
.project-link {
    display: block;
    margin-top: 10px;
    color: #9362e8;
    text-decoration: none;
    font-weight: bold;
}
.project-link:hover {
    text-decoration: underline;
}
</style>