<template>
  <section class="projects-section">
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
      </div>

    </div>
  </section>
</template>

<script setup>
// No hay lógica JavaScript compleja necesaria por ahora
</script>

<style scoped>
/* Pega el CSS que usaste en tu Projects.vue anterior para mantener el estilo */
.projects-section {
    padding: 3rem 1.5rem;
    background-color: #f4f4f9;
    text-align: center;
}
.title {
    font-size: 2.5rem;
    color: #2c3e50;
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
    color: #3498db;
    margin-bottom: 10px;
}
.project-description {
    color: #7f8c8d;
    margin-bottom: 15px;
}
.tech-badge {
    display: inline-block;
    background-color: #ecf0f1;
    color: #2c3e50;
    padding: 5px 10px;
    border-radius: 5px;
    margin-right: 5px;
    font-size: 0.8rem;
}
</style>