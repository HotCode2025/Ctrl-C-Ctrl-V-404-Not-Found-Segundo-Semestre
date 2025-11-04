<template>
  <section id="tecnologias" class="tech-section">
    <div class="container">
      <h2 class="section-title">Tecnologías que Dominamos</h2>
      <p class="tech-subtitle">
        Lenguajes, frameworks y herramientas que utilizamos en nuestros proyectos
      </p>
      
      <div class="tech-grid">
        <div 
          v-for="(tech, index) in technologies" 
          :key="index"
          class="tech-card"
        >
          <div class="tech-icon" :style="{ background: tech.color }">
            <span class="tech-emoji">{{ tech.icon }}</span>
          </div>
          <h3 class="tech-name">{{ tech.name }}</h3>
          <p class="tech-description">{{ tech.description }}</p>
          <div class="tech-progress">
            <div class="progress-bar">
              <div 
                class="progress-fill" 
                :style="{ width: tech.level + '%', background: tech.color }"
              ></div>
            </div>
            <span class="progress-label">{{ tech.level }}%</span>
          </div>
        </div>
      </div>
      
      <div class="tech-extra">
        <h3>También Trabajamos Con:</h3>
        <div class="extra-tags">
          <span v-for="(extra, index) in extraTools" :key="index" class="tag">
            {{ extra }}
          </span>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Technologies',
  data() {
    return {
      technologies: [
        {
          name: 'Java',
          icon: '☕',
          description: 'Programación orientada a objetos, desarrollo de aplicaciones empresariales.',
          level: 75,
          color: 'linear-gradient(135deg, #f44336 0%, #e91e63 100%)'
        },
        {
          name: 'Python',
          icon: '🐍',
          description: 'Desarrollo web, scripts, análisis de datos y automatización.',
          level: 80,
          color: 'linear-gradient(135deg, #2196f3 0%, #00bcd4 100%)'
        },
        {
          name: 'JavaScript',
          icon: '⚡',
          description: 'Desarrollo web frontend y backend, aplicaciones interactivas.',
          level: 85,
          color: 'linear-gradient(135deg, #ffeb3b 0%, #ffc107 100%)'
        },
        {
          name: 'MySQL',
          icon: '🗄️',
          description: 'Gestión de bases de datos relacionales, consultas SQL.',
          level: 70,
          color: 'linear-gradient(135deg, #00bcd4 0%, #03a9f4 100%)'
        },
        {
          name: 'Git',
          icon: '🌿',
          description: 'Control de versiones, colaboración en equipo.',
          level: 75,
          color: 'linear-gradient(135deg, #ff5722 0%, #ff9800 100%)'
        },
        {
          name: 'GitHub',
          icon: '🐙',
          description: 'Repositorios remotos, gestión de proyectos colaborativos.',
          level: 80,
          color: 'linear-gradient(135deg, #424242 0%, #212121 100%)'
        }
      ],
      extraTools: [
        'HTML5', 'CSS3', 'Vue.js', 'Node.js', 'Express', 
        'VS Code', 'IntelliJ IDEA', 'Postman', 'Docker', 'Linux'
      ]
    }
  }
}
</script>

<style scoped>
.tech-section {
  padding: 5rem 0;
  background: white;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 1rem;
  color: var(--color-dark);
}

.tech-subtitle {
  text-align: center;
  font-size: 1.1rem;
  color: var(--color-text-light);
  margin-bottom: 3rem;
}

.tech-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 4rem;
}

.tech-card {
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  padding: 2rem;
  border-radius: 15px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.tech-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.tech-icon {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin: 0 auto 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.tech-emoji {
  font-size: 2.5rem;
}

.tech-name {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--color-dark);
  margin-bottom: 1rem;
}

.tech-description {
  font-size: 0.95rem;
  color: var(--color-text-light);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.tech-progress {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.progress-bar {
  flex: 1;
  height: 8px;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  border-radius: 10px;
  transition: width 1s ease;
}

.progress-label {
  font-weight: 600;
  color: var(--color-primary);
  min-width: 45px;
  text-align: right;
}

.tech-extra {
  text-align: center;
  padding: 3rem;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
  border-radius: 20px;
}

.tech-extra h3 {
  font-size: 1.8rem;
  color: var(--color-dark);
  margin-bottom: 2rem;
}

.extra-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}

.tag {
  padding: 0.75rem 1.5rem;
  background: white;
  border-radius: 25px;
  font-weight: 500;
  color: var(--color-primary);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.tag:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
}

@media (max-width: 768px) {
  .tech-grid {
    grid-template-columns: 1fr;
  }
}
</style>