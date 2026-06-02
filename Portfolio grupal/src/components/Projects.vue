<template>
  <section id="proyectos" class="projects">
    <div class="container">
      <p class="section-subtitle">Lo que construimos</p>
      <h2 class="section-title">Proyectos</h2>
      <div class="section-divider"></div>

      <div class="projects-grid">
        <div
          v-for="(project, index) in projects"
          :key="index"
          class="project-card"
        >
          <div class="project-top">
            <span class="project-index">{{ String(index + 1).padStart(2, '0') }}</span>
            <span class="project-status" :class="project.statusClass">{{ project.status }}</span>
          </div>

          <h3 class="project-title">{{ project.title }}</h3>
          <p class="project-desc">{{ project.description }}</p>

          <div class="project-tech">
            <span v-for="(tech, idx) in project.technologies" :key="idx" class="tech-tag">{{ tech }}</span>
          </div>

          <div class="project-links">
            <a href="#" class="project-link">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
              </svg>
              GitHub
            </a>
            <a href="#" class="project-link">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
                <polyline points="15 3 21 3 21 9"/>
                <line x1="10" y1="14" x2="21" y2="3"/>
              </svg>
              Demo
            </a>
          </div>
        </div>
      </div>

      <div class="projects-cta">
        <p class="cta-label">¿Querés ver más?</p>
        <h3>Explorá todos nuestros repositorios</h3>
        <a href="https://github.com" target="_blank" class="btn btn-primary" style="margin-top:1.5rem">
          Ver en GitHub
        </a>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Projects',
  data() {
    return {
      projects: [
        {
          title: 'Sistema de Gestión Académica',
          description: 'Aplicación web para administrar alumnos, materias y calificaciones. Incluye autenticación de usuarios y generación de reportes.',
          status: 'Completado', statusClass: 'status-done',
          technologies: ['Java', 'MySQL', 'JavaScript']
        },
        {
          title: 'API REST E-commerce',
          description: 'Backend para tienda online con gestión de productos, usuarios y pedidos. Implementa autenticación JWT.',
          status: 'En Desarrollo', statusClass: 'status-wip',
          technologies: ['Python', 'MySQL', 'Git']
        },
        {
          title: 'Dashboard Analítico',
          description: 'Panel interactivo para visualización de datos con gráficos y estadísticas en tiempo real.',
          status: 'En Desarrollo', statusClass: 'status-wip',
          technologies: ['JavaScript', 'Python', 'MySQL']
        },
        {
          title: 'Portfolio Grupal',
          description: 'Este mismo sitio. Desarrollado colaborativamente con Vue.js y control de versiones con Git.',
          status: 'Activo', statusClass: 'status-active',
          technologies: ['Vue.js', 'Git', 'GitHub']
        },
        {
          title: 'Sistema de Inventario',
          description: 'Aplicación de escritorio para control de stock, proveedores y movimientos de almacén.',
          status: 'Planificado', statusClass: 'status-plan',
          technologies: ['Java', 'MySQL']
        },
        {
          title: 'Bot de Automatización',
          description: 'Script en Python para automatizar tareas repetitivas y procesamiento de datos.',
          status: 'Completado', statusClass: 'status-done',
          technologies: ['Python', 'Git']
        }
      ]
    }
  }
}
</script>

<style scoped>
.projects {
  padding: 7rem 0;
  background: var(--cream);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  overflow: hidden;
  margin-bottom: 4rem;
}

.project-card {
  background: var(--white);
  padding: 2.25rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  transition: background 0.25s;
}

.project-card:hover {
  background: #fdfcfa;
}

.project-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.project-index {
  font-family: 'Playfair Display', serif;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--gold);
  opacity: 0.6;
  letter-spacing: 0.1em;
}

.project-status {
  font-size: 0.7rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 0.25rem 0.7rem;
  border-radius: 2px;
}

.status-done   { background: rgba(34,197,94,0.1);  color: #16a34a; border: 1px solid rgba(34,197,94,0.2); }
.status-wip    { background: rgba(234,179,8,0.1);  color: #b45309; border: 1px solid rgba(234,179,8,0.2); }
.status-active { background: rgba(59,130,246,0.1); color: #1d4ed8; border: 1px solid rgba(59,130,246,0.2); }
.status-plan   { background: rgba(156,163,175,0.1);color: #6b7280; border: 1px solid rgba(156,163,175,0.2); }

.project-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--navy);
  line-height: 1.3;
}

.project-desc {
  font-size: 0.875rem;
  color: var(--text-mid);
  line-height: 1.75;
  flex: 1;
}

.project-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.tech-tag {
  font-size: 0.7rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  padding: 0.2rem 0.6rem;
  border: 1px solid var(--border);
  color: var(--text-mid);
  border-radius: 2px;
}

.project-links {
  display: flex;
  gap: 1rem;
  padding-top: 0.5rem;
  border-top: 1px solid var(--border);
}

.project-link {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--text-mid);
  text-decoration: none;
  letter-spacing: 0.05em;
  transition: color 0.2s;
}

.project-link:hover { color: var(--gold); }

.projects-cta {
  text-align: center;
  padding: 4rem 2rem;
  border: 1px solid var(--border);
  background: var(--white);
}

.cta-label {
  font-size: 0.75rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 0.75rem;
  font-weight: 500;
}

.projects-cta h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.6rem;
  color: var(--navy);
}

@media (max-width: 640px) {
  .projects-grid { grid-template-columns: 1fr; }
}
</style>
