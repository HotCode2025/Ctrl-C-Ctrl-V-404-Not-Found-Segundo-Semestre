<template>
  <section id="tecnologias" class="tech">
    <div class="container">
      <p class="section-subtitle">Stack técnico</p>
      <h2 class="section-title">Tecnologías</h2>
      <div class="section-divider"></div>

      <div class="tech-grid">
        <div v-for="(tech, index) in technologies" :key="index" class="tech-card">
          <div class="tech-header">
            <span class="tech-abbr">{{ tech.abbr }}</span>
            <span class="tech-level">{{ tech.level }}%</span>
          </div>
          <h3 class="tech-name">{{ tech.name }}</h3>
          <p class="tech-desc">{{ tech.description }}</p>
          <div class="progress-track">
            <div class="progress-fill" :style="{ width: tech.level + '%' }"></div>
          </div>
        </div>
      </div>

      <div class="tech-extra">
        <p class="extra-label">También trabajamos con</p>
        <div class="extra-tags">
          <span v-for="(t, i) in extraTools" :key="i" class="tag">{{ t }}</span>
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
        { name: 'Java',       abbr: 'JV',  description: 'Programación orientada a objetos y aplicaciones empresariales.', level: 75 },
        { name: 'Python',     abbr: 'PY',  description: 'Desarrollo web, scripts, análisis de datos y automatización.',    level: 80 },
        { name: 'JavaScript', abbr: 'JS',  description: 'Desarrollo web frontend y backend, aplicaciones interactivas.',    level: 85 },
        { name: 'MySQL',      abbr: 'SQL', description: 'Gestión de bases de datos relacionales y consultas avanzadas.',    level: 70 },
        { name: 'Git',        abbr: 'GIT', description: 'Control de versiones y colaboración en equipo.',                   level: 75 },
        { name: 'GitHub',     abbr: 'GH',  description: 'Repositorios remotos y gestión de proyectos colaborativos.',       level: 80 }
      ],
      extraTools: ['HTML5', 'CSS3', 'Vue.js', 'Node.js', 'Express', 'VS Code', 'IntelliJ IDEA', 'Postman', 'Docker', 'Linux']
    }
  }
}
</script>

<style scoped>
.tech {
  padding: 7rem 0;
  background: var(--white);
}

.tech-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  overflow: hidden;
  margin-bottom: 4rem;
}

.tech-card {
  background: var(--white);
  padding: 2.25rem;
  transition: background 0.25s;
}

.tech-card:hover {
  background: var(--cream);
}

.tech-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.tech-abbr {
  font-family: 'Playfair Display', serif;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: var(--gold);
  border: 1px solid rgba(201,169,110,0.3);
  padding: 0.25rem 0.6rem;
  border-radius: 2px;
}

.tech-level {
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--text-muted);
}

.tech-name {
  font-family: 'Playfair Display', serif;
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--navy);
  margin-bottom: 0.6rem;
}

.tech-desc {
  font-size: 0.875rem;
  color: var(--text-mid);
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

.progress-track {
  height: 2px;
  background: var(--border);
  border-radius: 1px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: var(--gold);
  border-radius: 1px;
  transition: width 1.2s ease;
}

.tech-extra {
  border-top: 1px solid var(--border);
  padding-top: 3rem;
}

.extra-label {
  font-size: 0.75rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 1.25rem;
  font-weight: 500;
}

.extra-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  padding: 0.4rem 0.9rem;
  border: 1px solid var(--border);
  border-radius: 2px;
  font-size: 0.8rem;
  font-weight: 400;
  color: var(--text-mid);
  background: var(--cream);
  transition: all 0.2s;
  cursor: default;
}

.tag:hover {
  border-color: var(--gold);
  color: var(--navy);
}

@media (max-width: 640px) {
  .tech-grid { grid-template-columns: 1fr; }
}
</style>
