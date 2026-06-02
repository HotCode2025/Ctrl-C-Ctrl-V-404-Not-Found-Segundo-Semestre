<template>
  <section id="habilidades" class="skills">
    <div class="container">
      <p class="section-subtitle">Nuestras capacidades</p>
      <h2 class="section-title">Habilidades</h2>
      <div class="section-divider"></div>

      <div class="skills-layout">
        <div class="skills-col">
          <h3 class="col-title">Técnicas</h3>
          <div class="skills-list">
            <div v-for="(skill, i) in technicalSkills" :key="i" class="skill-item">
              <div class="skill-meta">
                <span class="skill-name">{{ skill.name }}</span>
                <span class="skill-pct">{{ skill.level }}%</span>
              </div>
              <div class="skill-track">
                <div class="skill-fill" :style="{ width: skill.level + '%' }"></div>
              </div>
            </div>
          </div>
        </div>

        <div class="skills-col">
          <h3 class="col-title">Blandas</h3>
          <div class="soft-grid">
            <div v-for="(skill, i) in softSkills" :key="i" class="soft-card">
              <div class="soft-dot"></div>
              <div>
                <h4>{{ skill.name }}</h4>
                <p>{{ skill.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="achievements">
        <p class="section-subtitle section-subtitle--light">Trayectoria</p>
        <h3 class="achievements-title">Logros del Equipo</h3>
        <div class="section-divider"></div>
        <div class="ach-grid">
          <div v-for="(a, i) in achievements" :key="i" class="ach-card">
            <span class="ach-num">{{ String(i+1).padStart(2,'0') }}</span>
            <h4>{{ a.title }}</h4>
            <p>{{ a.description }}</p>
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
        { name: 'Programación Orientada a Objetos',    level: 85 },
        { name: 'Desarrollo Web (Frontend & Backend)', level: 80 },
        { name: 'Bases de Datos SQL',                  level: 75 },
        { name: 'Control de Versiones (Git)',          level: 85 },
        { name: 'Algoritmos y Estructuras de Datos',  level: 70 },
        { name: 'APIs REST y Servicios Web',           level: 75 }
      ],
      softSkills: [
        { name: 'Trabajo en Equipo',       description: 'Colaboración efectiva en proyectos grupales'   },
        { name: 'Comunicación',            description: 'Expresión clara de ideas técnicas'              },
        { name: 'Resolución de Problemas', description: 'Análisis y solución de desafíos complejos'     },
        { name: 'Aprendizaje Continuo',    description: 'Adaptación constante a nuevas tecnologías'     },
        { name: 'Pensamiento Crítico',     description: 'Evaluación objetiva de distintas soluciones'   },
        { name: 'Gestión del Tiempo',      description: 'Organización y cumplimiento de plazos'         }
      ],
      achievements: [
        { title: 'Proyectos Completados', description: 'Múltiples proyectos académicos finalizados exitosamente' },
        { title: 'Cursando Tecnicatura',  description: 'Estudiantes activos en UTN San Rafael'                   },
        { title: 'Trabajo Colaborativo',  description: 'Experiencia con metodologías ágiles y Git flow'          },
        { title: 'Innovación',            description: 'Implementación de soluciones creativas y modernas'       }
      ]
    }
  }
}
</script>

<style scoped>
.skills {
  padding: 7rem 0;
  background: var(--white);
}

.skills-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  margin-bottom: 5rem;
}

.col-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--navy);
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--border);
  letter-spacing: 0.02em;
}

.skills-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.skill-item {}

.skill-meta {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.skill-name {
  font-size: 0.875rem;
  color: var(--text-dark);
  font-weight: 400;
}

.skill-pct {
  font-size: 0.75rem;
  color: var(--text-muted);
  font-weight: 500;
}

.skill-track {
  height: 2px;
  background: var(--border);
  border-radius: 1px;
  overflow: hidden;
}

.skill-fill {
  height: 100%;
  background: var(--gold);
  border-radius: 1px;
  transition: width 1.2s ease;
}

.soft-grid {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.soft-card {
  display: flex;
  gap: 1rem;
  align-items: flex-start;
  padding: 1.25rem;
  border: 1px solid var(--border);
  background: var(--cream);
  transition: border-color 0.2s;
}

.soft-card:hover {
  border-color: var(--gold);
}

.soft-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--gold);
  margin-top: 0.55rem;
  flex-shrink: 0;
}

.soft-card h4 {
  font-family: 'Inter', sans-serif;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--navy);
  margin-bottom: 0.25rem;
}

.soft-card p {
  font-size: 0.825rem;
  color: var(--text-mid);
  line-height: 1.6;
}

.achievements {
  background: var(--navy);
  padding: 4rem;
  text-align: center;
}

.section-subtitle--light {
  color: var(--gold);
}

.achievements-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.8rem;
  color: var(--cream);
  margin-bottom: 0.5rem;
}

.ach-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1px;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.06);
  overflow: hidden;
  margin-top: 0.5rem;
}

.ach-card {
  background: var(--navy-mid);
  padding: 2rem;
  text-align: left;
  transition: background 0.25s;
}

.ach-card:hover {
  background: var(--navy-light);
}

.ach-num {
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  font-weight: 700;
  color: var(--gold);
  opacity: 0.3;
  display: block;
  line-height: 1;
  margin-bottom: 1rem;
}

.ach-card h4 {
  font-family: 'Playfair Display', serif;
  font-size: 1rem;
  color: var(--cream);
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.ach-card p {
  font-size: 0.825rem;
  color: rgba(240,235,225,0.55);
  line-height: 1.6;
}

@media (max-width: 768px) {
  .skills-layout { grid-template-columns: 1fr; gap: 3rem; }
  .achievements { padding: 3rem 1.5rem; }
  .ach-grid { grid-template-columns: 1fr; }
}
</style>
