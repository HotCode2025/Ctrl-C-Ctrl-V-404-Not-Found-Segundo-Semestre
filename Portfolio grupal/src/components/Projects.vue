<template>
  <section id="proyectos" class="projects-section">
    <div class="container">
      <h2 class="section-title">Nuestros Proyectos</h2>
      <p class="projects-subtitle">
        Aplicaciones y sistemas desarrollados durante nuestra formación
      </p>
      
      <div class="projects-grid">
        <div 
          v-for="(project, index) in projects" 
          :key="index"
          class="project-card"
        >
          <div class="project-image" :style="{ background: project.gradient }">
            <span class="project-icon">{{ project.icon }}</span>
          </div>
          
          <div class="project-content">
            <div class="project-header">
              <h3 class="project-title">{{ project.title }}</h3>
              <span class="project-status" :class="project.statusClass">
                {{ project.status }}
              </span>
            </div>
            
            <p class="project-description">{{ project.description }}</p>
            
            <div class="project-tech">
              <span 
                v-for="(tech, idx) in project.technologies" 
                :key="idx"
                class="tech-badge"
              >
                {{ tech }}
              </span>
            </div>
            
            <div class="project-links">
              <a href="#" class="project-link">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
                GitHub
              </a>
              <a href="#" class="project-link">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <line x1="10" y1="14" x2="21" y2="3"></line>
                </svg>
                Demo
              </a>
            </div>
          </div>
        </div>
      </div>
      
      <div class="projects-cta">
        <h3>¿Quieres ver más?</h3>
        <p>Visita nuestro repositorio de GitHub para explorar todos nuestros proyectos</p>
        <a href="https://github.com" target="_blank" class="btn btn-primary">
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
          icon: '📚',
          gradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          status: 'Completado',
          statusClass: 'status-completed',
          technologies: ['Java', 'MySQL', 'JavaScript']
        },
        {
          title: 'API REST E-commerce',
          description: 'Backend para tienda online con gestión de productos, usuarios y pedidos. Implementa autenticación JWT.',
          icon: '🛒',
          gradient: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
          status: 'En Desarrollo',
          statusClass: 'status-progress',
          technologies: ['Python', 'MySQL', 'Git']
        },
        {
          title: 'Dashboard Analítico',
          description: 'Panel interactivo para visualización de datos con gráficos y estadísticas en tiempo real.',
          icon: '📊',
          gradient: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
          status: 'En Desarrollo',
          statusClass: 'status-progress',
          technologies: ['JavaScript', 'Python', 'MySQL']
        },
        {
          title: 'Portfolio Grupal',
          description: 'Este sitio web! Desarrollado colaborativamente usando Vue.js y trabajando con Git para control de versiones.',
          icon: '🌐',
          gradient: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
          status: 'Activo',
          statusClass: 'status-active',
          technologies: ['JavaScript', 'Git', 'GitHub']
        },
        {
          title: 'Sistema de Inventario',
          description: 'Aplicación de escritorio para control de stock, proveedores y movimientos de almacén.',
          icon: '📦',
          gradient: 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
          status: 'Planificado',
          statusClass: 'status-planned',
          technologies: ['Java', 'MySQL']
        },
        {
          title: 'Bot de Automatización',
          description: 'Script en Python para automatizar tareas repetitivas y procesamiento de datos.',
          icon: '🤖',
          gradient: 'linear-gradient(135deg, #30cfd0 0%, #330867 100%)',
          status: 'Completado',
          statusClass: 'status-completed',
          technologies: ['Python', 'Git']
        }
      ]
    }
  }
}
</script>

<style scoped>
.projects-section {
  padding: 5rem 0;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 1rem;
  color: var(--color-dark);
}

.projects-subtitle {
  text-align: center;
  font-size: 1.1rem;
  color: var(--color-text-light);
  margin-bottom: 3rem;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  margin-bottom: 4rem;
}

.project-card {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.project-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.project-image {
  height: 150px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.project-icon {
  font-size: 4rem;
}

.project-content {
  padding: 2rem;
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
  gap: 1rem;
}

.project-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: var(--color-dark);
  flex: 1;
}

.project-status {
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  white-space: nowrap;
}

.status-completed {
  background: #d4edda;
  color: #155724;
}

.status-progress {
  background: #fff3cd;
  color: #856404;
}

.status-active {
  background: #d1ecf1;
  color: #0c5460;
}

.status-planned {
  background: #f8d7da;
  color: #721c24;
}

.project-description {
  font-size: 0.95rem;
  color: var(--color-text-light);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.project-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.tech-badge {
  padding: 0.4rem 0.8rem;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
  border-radius: 15px;
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--color-primary);
}

.project-links {
  display: flex;
  gap: 1rem;
}

.project-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 1.2rem;
  background: var(--color-primary);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.project-link:hover {
  background: var(--color-secondary);
  transform: translateY(-2px);
}

.projects-cta {
  text-align: center;
  padding: 3rem;
  background: white;
  border-radius: 20px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
}

.projects-cta h3 {
  font-size: 2rem;
  color: var(--color-dark);
  margin-bottom: 1rem;
}

.projects-cta p {
  font-size: 1.1rem;
  color: var(--color-text-light);
  margin-bottom: 2rem;
}

.btn-primary {
  display: inline-block;
  padding: 1rem 2rem;
  background: var(--color-primary);
  color: white;
  text-decoration: none;
  border-radius: 10px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: var(--color-secondary);
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
}

@media (max-width: 768px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
</style>