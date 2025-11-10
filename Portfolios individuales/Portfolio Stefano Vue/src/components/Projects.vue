<template>
  <section id="projects" class="section">
    <div class="container">
      <h2 class="section-title">Proyectos</h2>
      <div class="project-grid">
        <div class="project-card">
          <div class="project-icon">💼</div>
          <h3>Sistema de Gestión Académica</h3>
          <p>
            Aplicación web para la administración de inscripciones, materias y
            calificaciones en la UTN San Rafael.
          </p>
          <div class="project-tech">
            <span>Vue.js</span>
            <span>Firebase</span>
            <span>CSS3</span>
          </div>
        </div>
        <div class="project-card">
          <div class="project-icon">🌐</div>
          <h3>Portfolio Personal</h3>
          <p>
            Desarrollo de portfolio web para mostrar experiencia, proyectos y
            conocimientos.
          </p>
          <div class="project-tech">
            <span>Vue.js</span>
            <span>Vite</span>
            <span>CSS3</span>
          </div>
        </div>
        <div class="project-card">
          <div class="project-icon">✅</div>
          <h3>App de Tareas</h3>
          <p>
            Aplicación para la gestión de tareas diarias con Vue.js y Firebase.
          </p>
          <div class="project-tech">
            <span>Vue.js</span>
            <span>Firebase</span>
            <span>JavaScript</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// No script logic needed for static content
</script>

<style scoped>
.section {
  margin-bottom: 4rem;
  background: linear-gradient(135deg, #f8fdff 0%, #e3f2fd 100%);
  border-radius: 1.5rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
  padding: 3rem 2rem;
  position: relative;
  overflow: hidden;
}

.section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #00796b, #004d40);
}

.container {
  max-width: 1100px;
  margin: 0 auto;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 3rem;
  text-align: center;
  position: relative;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
  background: linear-gradient(90deg, #00796b, #004d40);
  border-radius: 2px;
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1000px;
  margin: 0 auto;
}

.project-card {
  background: white;
  border-radius: 1.2rem;
  padding: 2rem;
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08);
  border-top: 4px solid #00796b;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.project-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #00796b, #004d40);
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.project-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.project-card:hover::before {
  transform: scaleX(1);
}

.project-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  text-align: center;
}

.project-card h3 {
  font-size: 1.4rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1rem;
  text-align: center;
}

.project-card p {
  color: #34495e;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  text-align: center;
}

.project-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
}

.project-tech span {
  background: linear-gradient(135deg, #e0f7fa, #b2ebf2);
  color: #00796b;
  padding: 0.3rem 0.8rem;
  border-radius: 1rem;
  font-size: 0.85rem;
  font-weight: 500;
  border: 1px solid rgba(0, 121, 107, 0.2);
}

@media (max-width: 768px) {
  .section {
    padding: 2rem 1rem;
    margin-bottom: 2rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .project-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .project-card {
    padding: 1.5rem;
  }
}
</style>