<template>
  <section id="habilidades" class="skills-section">
    <div class="container">
      <h2 class="section-title">Habilidades del Equipo</h2>
      <p class="skills-subtitle">
        Combinamos habilidades técnicas con competencias interpersonales
      </p>
      
      <div class="skills-container">
        <!-- Habilidades Técnicas -->
        <div class="skills-category">
          <h3 class="category-title">
            <span class="category-icon">💻</span>
            Habilidades Técnicas
          </h3>
          
          <div class="skills-list">
            <div 
              v-for="(skill, index) in technicalSkills" 
              :key="index"
              class="skill-item"
            >
              <div class="skill-header">
                <span class="skill-name">{{ skill.name }}</span>
                <span class="skill-percentage">{{ skill.level }}%</span>
              </div>
              <div class="skill-bar">
                <div 
                  class="skill-progress" 
                  :style="{ width: skill.level + '%', background: skill.color }"
                ></div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Habilidades Blandas -->
        <div class="skills-category">
          <h3 class="category-title">
            <span class="category-icon">🤝</span>
            Habilidades Blandas
          </h3>
          
          <div class="soft-skills-grid">
            <div 
              v-for="(skill, index) in softSkills" 
              :key="index"
              class="soft-skill-card"
            >
              <div class="soft-skill-icon" :style="{ background: skill.color }">
                {{ skill.icon }}
              </div>
              <h4>{{ skill.name }}</h4>
              <p>{{ skill.description }}</p>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Certificaciones y Logros -->
      <div class="achievements">
        <h3 class="achievements-title">Certificaciones y Logros</h3>
        <div class="achievements-grid">
          <div 
            v-for="(achievement, index) in achievements" 
            :key="index"
            class="achievement-card"
          >
            <div class="achievement-badge">{{ achievement.icon }}</div>
            <h4>{{ achievement.title }}</h4>
            <p>{{ achievement.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Skills',
  data() {
    return {
      technicalSkills: [
        {
          name: 'Programación Orientada a Objetos',
          level: 85,
          color: 'linear-gradient(90deg, #667eea 0%, #764ba2 100%)'
        },
        {
          name: 'Desarrollo Web (Frontend & Backend)',
          level: 80,
          color: 'linear-gradient(90deg, #f093fb 0%, #f5576c 100%)'
        },
        {
          name: 'Bases de Datos SQL',
          level: 75,
          color: 'linear-gradient(90deg, #4facfe 0%, #00f2fe 100%)'
        },
        {
          name: 'Control de Versiones (Git)',
          level: 85,
          color: 'linear-gradient(90deg, #43e97b 0%, #38f9d7 100%)'
        },
        {
          name: 'Algoritmos y Estructuras de Datos',
          level: 70,
          color: 'linear-gradient(90deg, #fa709a 0%, #fee140 100%)'
        },
        {
          name: 'APIs REST y Servicios Web',
          level: 75,
          color: 'linear-gradient(90deg, #30cfd0 0%, #330867 100%)'
        }
      ],
      softSkills: [
        {
          name: 'Trabajo en Equipo',
          icon: '👥',
          description: 'Colaboración efectiva en proyectos grupales',
          color: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
        },
        {
          name: 'Comunicación',
          icon: '💬',
          description: 'Expresión clara de ideas técnicas',
          color: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)'
        },
        {
          name: 'Resolución de Problemas',
          icon: '🧩',
          description: 'Análisis y solución de desafíos complejos',
          color: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)'
        },
        {
          name: 'Aprendizaje Continuo',
          icon: '📚',
          description: 'Adaptación a nuevas tecnologías',
          color: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)'
        },
        {
          name: 'Pensamiento Crítico',
          icon: '🎯',
          description: 'Evaluación objetiva de soluciones',
          color: 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)'
        },
        {
          name: 'Gestión del Tiempo',
          icon: '⏰',
          description: 'Organización y cumplimiento de plazos',
          color: 'linear-gradient(135deg, #30cfd0 0%, #330867 100%)'
        }
      ],
      achievements: [
        {
          icon: '🏆',
          title: 'Proyectos Completados',
          description: 'Múltiples proyectos académicos finalizados exitosamente'
        },
        {
          icon: '📜',
          title: 'Cursando Tecnicatura',
          description: 'Estudiantes activos en UTN San Rafael'
        },
        {
          icon: '🚀',
          title: 'Trabajo Colaborativo',
          description: 'Experiencia en desarrollo con metodologías ágiles'
        },
        {
          icon: '💡',
          title: 'Innovación',
          description: 'Implementación de soluciones creativas'
        }
      ]
    }
  }
}
</script>

<style scoped>
.skills-section {
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

.skills-subtitle {
  text-align: center;
  font-size: 1.1rem;
  color: var(--color-text-light);
  margin-bottom: 3rem;
}

.skills-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 4rem;
  margin-bottom: 4rem;
}

.skills-category {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
  padding: 3rem;
  border-radius: 20px;
}

.category-title {
  font-size: 1.8rem;
  color: var(--color-dark);
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.category-icon {
  font-size: 2rem;
}

.skills-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.skill-item {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.skill-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.8rem;
}

.skill-name {
  font-weight: 600;
  color: var(--color-dark);
  font-size: 1.05rem;
}

.skill-percentage {
  font-weight: 700;
  color: var(--color-primary);
}

.skill-bar {
  height: 10px;
  background: rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  overflow: hidden;
}

.skill-progress {
  height: 100%;
  border-radius: 10px;
  transition: width 1.5s ease;
}

.soft-skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.soft-skill-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease;
}

.soft-skill-card:hover {
  transform: translateY(-5px);
}

.soft-skill-icon {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  margin: 0 auto 1rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.soft-skill-card h4 {
  font-size: 1.2rem;
  color: var(--color-dark);
  margin-bottom: 0.5rem;
}

.soft-skill-card p {
  font-size: 0.9rem;
  color: var(--color-text-light);
  line-height: 1.6;
}

.achievements {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 4rem;
  border-radius: 20px;
  color: white;
}

.achievements-title {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 3rem;
}

.achievements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.achievement-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 2rem;
  border-radius: 15px;
  text-align: center;
  transition: all 0.3s ease;
}

.achievement-card:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-5px);
}

.achievement-badge {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.achievement-card h4 {
  font-size: 1.3rem;
  margin-bottom: 0.8rem;
}

.achievement-card p {
  font-size: 0.95rem;
  opacity: 0.9;
}

@media (max-width: 768px) {
  .skills-category {
    padding: 2rem;
  }
  
  .soft-skills-grid,
  .achievements-grid {
    grid-template-columns: 1fr;
  }
}
</style>