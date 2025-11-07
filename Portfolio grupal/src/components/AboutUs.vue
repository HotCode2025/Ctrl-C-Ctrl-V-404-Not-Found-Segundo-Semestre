<template>
  <section id="nosotros" class="about-section">
    <div class="container">
      <h2 class="section-title">Sobre Nosotros</h2>
      
      <div class="about-content">
        <div class="about-card">
          <div class="card-icon">🎯</div>
          <h3>Nuestra Misión</h3>
          <p>
            Formarnos como profesionales en programación, adquiriendo conocimientos 
            sólidos en desarrollo de software y preparándonos para los desafíos 
            tecnológicos del mundo actual.
          </p>
        </div>
        
        <div class="about-card">
          <div class="card-icon">👥</div>
          <h3>Quiénes Somos</h3>
          <p>
            Somos 8 estudiantes de la Tecnicatura Universitaria en Programación 
            de la UTN San Rafael, unidos por la pasión por la tecnología y el 
            compromiso con el aprendizaje continuo.
          </p>
        </div>
        
        <div class="about-card">
          <div class="card-icon">🚀</div>
          <h3>Nuestros Objetivos</h3>
          <p>
            Desarrollar habilidades técnicas y blandas, trabajar en equipo, 
            crear proyectos innovadores y contribuir al ecosistema tecnológico 
            de nuestra región y país.
          </p>
        </div>
      </div>
      
      <div class="about-university">
        <h3>Universidad Tecnológica Nacional</h3>
        <p class="university-location">Facultad Regional San Rafael - Mendoza</p>
        <p class="university-description">
          La UTN es una institución reconocida por su excelencia académica en carreras 
          de ingeniería y tecnología. Nuestra Facultad Regional en San Rafael nos brinda 
          una formación integral, combinando teoría y práctica para prepararnos como 
          profesionales competentes en el campo de la programación y el desarrollo de software.
        </p>
        
        <div class="university-stats">
          <div class="stat-item">
            <span class="stat-number">8</span>
            <span class="stat-label">Integrantes</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">6+</span>
            <span class="stat-label">Tecnologías</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">100%</span>
            <span class="stat-label">Compromiso</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'AboutUs'
}
</script>

<style scoped>
.about-section {
  padding: 5rem 0;
  background: white;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 3rem;
  color: var(--color-dark);
}

.about-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 4rem;
}

.about-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 2.5rem;
  border-radius: 15px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  color: white;
}

.about-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(102, 126, 234, 0.3);
}

.card-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.about-card h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  font-weight: 600;
}

.about-card p {
  font-size: 1rem;
  line-height: 1.7;
  opacity: 0.95;
}

.about-university {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
  padding: 3rem;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
  border-radius: 20px;
}

.about-university h3 {
  font-size: 2rem;
  color: var(--color-primary);
  margin-bottom: 0.5rem;
}

.university-location {
  font-size: 1.2rem;
  color: var(--color-secondary);
  margin-bottom: 1.5rem;
  font-weight: 600;
}

.university-description {
  font-size: 1.1rem;
  line-height: 1.8;
  color: var(--color-text);
  margin-bottom: 2rem;
}

.university-stats {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 2rem;
  margin-top: 2rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--color-primary);
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 1rem;
  color: var(--color-text-light);
  font-weight: 500;
}

@media (max-width: 768px) {
  .about-content {
    grid-template-columns: 1fr;
  }
  
  .about-university {
    padding: 2rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
}
</style>