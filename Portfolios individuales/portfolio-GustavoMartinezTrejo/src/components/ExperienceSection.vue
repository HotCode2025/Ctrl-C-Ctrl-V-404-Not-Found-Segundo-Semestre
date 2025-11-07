<template>
  <section id="experiencia" class="section fade-in">
    <h2>Experiencia Laboral</h2>

    <div
      v-for="(exp, index) in experiences"
      :key="index"
      class="experience-item"
    >
      <div class="company-name">{{ exp.company }}</div>
      <div class="date">{{ exp.date }}</div>
      <p>{{ exp.description }}</p>
    </div>
  </section>
</template>

<script setup>
const experiences = [
  {
    company: 'Henry',
    date: 'Noviembre 2022 - Presente: Mentor Full Stack',
    description: 'Mentor de desarrolladores juniors en tecnologías JavaScript tanto en frontend como backend. Capacitación práctica en Node.js, React y Express.js, revisión de código, debugging y creación de material formativo.'
  },
  {
    company: 'Plerk',
    date: 'Agosto 2020 - Octubre 2022: Full Stack Developer',
    description: 'Desarrollo full stack con React, Vue.js, Node.js y Express. Construcción de APIs RESTful, gestión de datos en MySQL y despliegue en AWS.'
  },
  {
    company: 'Isibit',
    date: 'Julio 2020 - Agosto 2020: QA Automation Developer',
    description: 'Automatización de pruebas con frameworks personalizados, integración con CI/CD, documentación de errores y análisis de calidad.'
  }
]
</script>

<style scoped>
.section {
  background: rgba(99, 99, 99, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 40px;
  margin-bottom: 30px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.section:hover {
  transform: translateY(-5px);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
}

h2 {
  color: #2c3e50;
  font-size: 2rem;
  margin-bottom: 30px;
  padding-bottom: 15px;
  border-bottom: 3px solid #667eea;
  position: relative;
}

h2::after {
  content: '';
  position: absolute;
  bottom: -3px;
  left: 0;
  width: 50px;
  height: 3px;
  background: #6313b3;
}

.experience-item {
  margin-bottom: 30px;
  padding: 25px;
  background: rgba(102, 126, 234, 0.05);
  border-radius: 15px;
  border-left: 5px solid #667eea;
  transition: all 0.3s ease;
}

.experience-item:hover {
  background: rgba(102, 126, 234, 0.1);
  transform: translateX(10px);
}

.company-name {
  font-size: 1.3rem;
  font-weight: bold;
  color: #2c3e50;
  margin-bottom: 5px;
}

.date {
  color: #7f8c8d;
  font-style: italic;
  margin-bottom: 10px;
}

@media (max-width: 768px) {
  .section {
    padding: 20px;
  }
}
</style>