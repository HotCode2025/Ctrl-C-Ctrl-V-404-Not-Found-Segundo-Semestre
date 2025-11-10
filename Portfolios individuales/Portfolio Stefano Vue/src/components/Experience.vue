<template>
  <section id="experience" class="section">
    <div class="container">
      <h2 class="section-title">Experiencia Laboral</h2>
      <div class="timeline">
        <div class="experience-item">
          <div class="timeline-marker"></div>
          <div class="experience-content">
            <h3>Desarrollador Web Junior - TechSolutions Argentina</h3>
            <p class="date">Marzo 2022 - Presente</p>
            <ul>
              <li>
                Desarrollo y mantenimiento de sitios web corporativos usando HTML,
                CSS, JavaScript y Vue.js.
              </li>
              <li>
                Colaboración en equipos ágiles para la implementación de nuevas
                funcionalidades.
              </li>
              <li>
                Optimización de rendimiento y accesibilidad en proyectos existentes.
              </li>
            </ul>
          </div>
        </div>
        <div class="experience-item">
          <div class="timeline-marker"></div>
          <div class="experience-content">
            <h3>Prácticas Profesionales - UTN San Rafael</h3>
            <p class="date">Agosto 2021 - Febrero 2022</p>
            <ul>
              <li>
                Participación en el desarrollo de aplicaciones internas para la
                gestión académica.
              </li>
              <li>Soporte técnico y capacitación a usuarios finales.</li>
            </ul>
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

.timeline {
  position: relative;
  max-width: 800px;
  margin: 0 auto;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 30px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(to bottom, #00796b, #004d40);
  border-radius: 1px;
}

.experience-item {
  position: relative;
  margin-bottom: 3rem;
  display: flex;
  align-items: flex-start;
}

.timeline-marker {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #00796b, #004d40);
  border: 4px solid white;
  box-shadow: 0 4px 15px rgba(0, 121, 107, 0.3);
  flex-shrink: 0;
  margin-right: 2rem;
  position: relative;
  z-index: 2;
}

.experience-content {
  flex: 1;
  background: white;
  border-radius: 1rem;
  padding: 2rem;
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08);
  border-left: 4px solid #00796b;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.experience-content:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
}

.experience-content h3 {
  font-size: 1.4rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.date {
  font-size: 1rem;
  color: #00796b;
  margin-bottom: 1rem;
  font-weight: 500;
  background: #e0f7fa;
  padding: 0.3rem 1rem;
  border-radius: 2rem;
  display: inline-block;
}

ul {
  padding-left: 1.5rem;
  color: #34495e;
  line-height: 1.6;
}

ul li {
  margin-bottom: 0.5rem;
  position: relative;
}

ul li::marker {
  color: #00796b;
  font-size: 1.2em;
}

@media (max-width: 768px) {
  .section {
    padding: 2rem 1rem;
    margin-bottom: 2rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .timeline::before {
    left: 25px;
  }
  
  .timeline-marker {
    width: 50px;
    height: 50px;
    margin-right: 1.5rem;
  }
  
  .experience-content {
    padding: 1.5rem;
  }
  
  .experience-content h3 {
    font-size: 1.2rem;
  }
}
</style>