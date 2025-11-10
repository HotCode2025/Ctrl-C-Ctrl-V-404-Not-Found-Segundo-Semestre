<template>
  <section id="project" class="projects-section">
    <h2>Mis Proyectos</h2>
    <div class="projects-grid">
      <article
        v-for="project in projects"
        :key="project.id"
        class="project-card"
        :style="{ '--btn-color': project.color }"
      >
        <div class="card-color-background" :style="{ backgroundColor: project.color }">
          <i :class="project.iconClass"></i>
        </div>

        <div class="card-content">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
          <div class="project-tags">
            <span
              v-for="tag in project.tags"
              :key="tag"
              class="tag"
              :style="{ backgroundColor: getTagColor(tag) }"
              >{{ tag }}</span
            >
          </div>
          <div class="project-links">
            <a :href="project.repoUrl" target="_blank" class="btn btn-secondary">Ver Código</a>
          </div>
        </div>
      </article>
    </div>

    <div class="more-projects-link">
      <a href="https://github.com/Santiagocapi" target="_blank" class="btn btn-accent">
        Ver más proyectos en
        <svg
          style="width: 36px"
          class="github"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 640 640"
        >
          <path
            d="M237.9 461.4C237.9 463.4 235.6 465 232.7 465C229.4 465.3 227.1 463.7 227.1 461.4C227.1 459.4 229.4 457.8 232.3 457.8C235.3 457.5 237.9 459.1 237.9 461.4zM206.8 456.9C206.1 458.9 208.1 461.2 211.1 461.8C213.7 462.8 216.7 461.8 217.3 459.8C217.9 457.8 216 455.5 213 454.6C210.4 453.9 207.5 454.9 206.8 456.9zM251 455.2C248.1 455.9 246.1 457.8 246.4 460.1C246.7 462.1 249.3 463.4 252.3 462.7C255.2 462 257.2 460.1 256.9 458.1C256.6 456.2 253.9 454.9 251 455.2zM316.8 72C178.1 72 72 177.3 72 316C72 426.9 141.8 521.8 241.5 555.2C254.3 557.5 258.8 549.6 258.8 543.1C258.8 536.9 258.5 502.7 258.5 481.7C258.5 481.7 188.5 496.7 173.8 451.9C173.8 451.9 162.4 422.8 146 415.3C146 415.3 123.1 399.6 147.6 399.9C147.6 399.9 172.5 401.9 186.2 425.7C208.1 464.3 244.8 453.2 259.1 446.6C261.4 430.6 267.9 419.5 275.1 412.9C219.2 406.7 162.8 398.6 162.8 302.4C162.8 274.9 170.4 261.1 186.4 243.5C183.8 237 175.3 210.2 189 175.6C209.9 169.1 258 202.6 258 202.6C278 197 299.5 194.1 320.8 194.1C342.1 194.1 363.6 197 383.6 202.6C383.6 202.6 431.7 169 452.6 175.6C466.3 210.3 457.8 237 455.2 243.5C471.2 261.2 481 275 481 302.4C481 398.9 422.1 406.6 366.2 412.9C375.4 420.8 383.2 435.8 383.2 459.3C383.2 493 382.9 534.7 382.9 542.9C382.9 549.4 387.5 557.3 400.2 555C500.2 521.8 568 426.9 568 316C568 177.3 455.5 72 316.8 72zM169.2 416.9C167.9 417.9 168.2 420.2 169.9 422.1C171.5 423.7 173.8 424.4 175.1 423.1C176.4 422.1 176.1 419.8 174.4 417.9C172.8 416.3 170.5 415.6 169.2 416.9zM158.4 408.8C157.7 410.1 158.7 411.7 160.7 412.7C162.3 413.7 164.3 413.4 165 412C165.7 410.7 164.7 409.1 162.7 408.1C160.7 407.5 159.1 407.8 158.4 408.8zM190.8 444.4C189.2 445.7 189.8 448.7 192.1 450.6C194.4 452.9 197.3 453.2 198.6 451.6C199.9 450.3 199.3 447.3 197.3 445.4C195.1 443.1 192.1 442.8 190.8 444.4zM179.4 429.7C177.8 430.7 177.8 433.3 179.4 435.6C181 437.9 183.7 438.9 185 437.9C186.6 436.6 186.6 434 185 431.7C183.6 429.4 181 428.4 179.4 429.7z"
          />
        </svg>
      </a>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

// Array with tag's colors
const tagColors = {
  Unity: '#8e44ad',
  'C#': '#8e44ad',
  JavaScript: '#27ae60',
  'Node.js': '#27ae60',
  Express: '#27ae60',
  MongoDB: '#27ae60',
  Python: '#f39c12',
  Django: '#f39c12',
}

// Function to apply colors to tags
const getTagColor = (tag) => {
  return tagColors[tag.trim()] || tagColors.default
}

// Projects
const projects = ref([
  {
    id: 1,
    title: 'Información del terminal de red óptica',
    color: '#f39c12',
    iconClass: 'fas fa-code',
    description:
      'Aplicacion para la seccion de atencion al cliente, en las pasantias en ITC (Informatica y Telecomunicaciones)',
    tags: ['Python', 'Django'],
    repoUrl: 'https://github.com/MauroGuar/ONT-Info',
  },
  {
    id: 2,
    title: 'Juego 2D en Unity',
    color: '#8e44ad',
    iconClass: 'fas fa-gamepad',
    description:
      'Un juego de plataformas 2D desarrollado con el motor Unity, enfocado en físicas y mecánicas de movimiento. Nota final para programacion.',
    tags: ['Unity', 'C#'],
    repoUrl: 'https://github.com/Santiagocapi/Proyecto-Unity',
  },
  {
    id: 3,
    title: 'Web de venta de entradas',
    color: '#27ae60',
    iconClass: 'fas fa-server',
    description:
      'Aplicacion para nota final de Programacion, diseño simple, con base de datos y backend',
    tags: ['JavaScript', 'Node.js', 'Express', 'MongoDB'],
    repoUrl: 'https://github.com/Santiagocapi/Proyecto-Integrador',
  },
])
</script>

<style scoped>
.projects-section {
  padding: 4rem 2rem;
  background-color: var(--light-grey, #f8f9fa);

  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }
}

/* Cards */
.project-card {
  background: var(--white);
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;

  &:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);

    .card-color-background i {
      transform: scale(1.1);
    }
  }
}

.card-color-background {
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;

  i {
    font-size: 6rem;
    color: rgba(255, 255, 255, 0.2);
    transition: transform 0.4s ease;
  }
}

.card-content {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;

  h3 {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
  }

  p {
    font-size: 0.95rem;
    color: var(--text-secondary);
    line-height: 1.6;
    flex-grow: 1;
  }

  .project-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 1rem 0;
  }
}

/* Tags */

.tag {
  padding: 0.3rem 0.8rem;
  border-radius: 5px 0 5px 0;
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--white);
  transition: 0.5s;
  cursor: pointer;

  &:hover {
    transform: translateY(-5px);
  }
}

/* Projects Link Button */

.project-links {
  display: flex;
  gap: 1rem;
  margin-top: auto;

  .btn-secondary {
    background-color: transparent;
    color: var(--btn-color);
    border: 2px solid var(--btn-color);

    &:hover {
      background-color: var(--btn-color);
      color: var(--white);
    }
  }
}

/* More Projects Button */

.more-projects-link {
  text-align: center;
  margin-top: 3rem;

  .btn-accent {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background-color: var(--primary);
    color: var(--white);
    padding: 0.8rem 2rem;
    font-size: 1.1rem;
    border: none;

    &:hover {
      background-color: var(--accent);
      transform: translateY(-2px);
      box-shadow: 0 4px 15px rgba(13, 110, 253, 0.4);
    }

    .github {
      fill: var(--white);
    }
  }
}
</style>
