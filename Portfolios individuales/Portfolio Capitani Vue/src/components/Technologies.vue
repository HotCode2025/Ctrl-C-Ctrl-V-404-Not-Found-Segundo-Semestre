<template>
  <section class="technologies-section">
    <h2>Mis Tecnologías</h2>
    <div class="tech-grid">
      <div
        v-for="tech in technologies"
        :key="tech.name"
        class="tech-card-wrapper"
        :class="tech.gradientClass"
        :style="{ '--tech-color': tech.color }"
      >
        <div class="tech-card">
          <i :class="tech.iconClass"></i>
          <span>{{ tech.name }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const technologies = ref([
  // Frontend
  {
    name: 'Vue.js',
    iconClass: 'devicon-vuejs-plain',
    gradientClass: 'vue-gradient',
    color: '#42b883',
  },
  {
    name: 'React',
    iconClass: 'devicon-react-original',
    gradientClass: 'react-gradient',
    color: '#61dafb',
  },
  {
    name: 'JavaScript',
    iconClass: 'devicon-javascript-plain',
    gradientClass: 'js-gradient',
    color: '#f7df1e',
  },
  {
    name: 'HTML5',
    iconClass: 'devicon-html5-plain',
    gradientClass: 'html-gradient',
    color: '#e34f26',
  },
  {
    name: 'CSS3',
    iconClass: 'devicon-css3-plain',
    gradientClass: 'css-gradient',
    color: '#1572b6',
  },

  // Backend
  {
    name: 'Node.js',
    iconClass: 'devicon-nodejs-plain',
    gradientClass: 'node-gradient',
    color: '#68a063',
  },
  {
    name: 'Express',
    iconClass: 'devicon-express-original',
    gradientClass: 'express-gradient',
    color: '#000000',
  },
  {
    name: 'Python',
    iconClass: 'devicon-python-plain',
    gradientClass: 'python-gradient',
    color: '#3776ab',
  },
  {
    name: 'Flask',
    iconClass: 'devicon-flask-original',
    gradientClass: 'flask-gradient',
    color: '#000000',
  },
  {
    name: 'Java',
    iconClass: 'devicon-java-plain',
    gradientClass: 'java-gradient',
    color: '#f89820',
  },

  // Bases de Datos
  {
    name: 'MongoDB',
    iconClass: 'devicon-mongodb-plain',
    gradientClass: 'mongo-gradient',
    color: '#47a248',
  },
  {
    name: 'MySQL',
    iconClass: 'devicon-mysql-plain',
    gradientClass: 'mysql-gradient',
    color: '#4479a1',
  },

  // Herramientas y Otros
  { name: 'Git', iconClass: 'devicon-git-plain', gradientClass: 'git-gradient', color: '#f05032' },
  {
    name: 'Docker',
    iconClass: 'devicon-docker-plain',
    gradientClass: 'docker-gradient',
    color: '#2496ed',
  },
  {
    name: 'Figma',
    iconClass: 'devicon-figma-plain',
    gradientClass: 'figma-gradient',
    color: '#f24e1e',
  },
])
</script>

<style scoped>
.technologies-section {
  padding: 4rem 2rem;
  background-size: cover;
  background-attachment: fixed;
  padding: 4rem 2rem;
  position: relative;

  .tech-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 2rem;
    max-width: 1000px;
    margin: 0 auto;

    /* Contour */
    .tech-card-wrapper {
      padding: 4px;
      border-radius: 12px;
      background-size: 200% 200%;
      transition: transform 0.3s ease;
      cursor: pointer;

      &:hover {
        transform: translateY(-8px);

        .tech-card i {
          color: var(--tech-color);
        }
      }
    }
  }
}

/* Cards */

.tech-card {
  background-color: var(--white);
  border-radius: 10px;
  height: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  transition: all 0.3s ease;

  i {
    font-size: 4rem;
    color: var(--grey);
    transition: color 0.4s ease;
    transition: all 0.4s ease;
  }

  span {
    font-weight: 500;
    color: #34495e;
  }
}

/* Gradients */
.vue-gradient {
  background-image: linear-gradient(45deg, #42b883, #347474);
}

.react-gradient {
  background-image: linear-gradient(45deg, #61dafb, #20232a);
}

.js-gradient {
  background-image: linear-gradient(45deg, #f7df1e, #b0a010);
}

.html-gradient {
  background-image: linear-gradient(45deg, #e34f26, #f16529);
}

.css-gradient {
  background-image: linear-gradient(45deg, #1572b6, #3c99dc);
}

.node-gradient {
  background-image: linear-gradient(45deg, #68a063, #333);
}

.express-gradient {
  background-image: linear-gradient(45deg, #000000, #444);
}

.python-gradient {
  background-image: linear-gradient(45deg, #3776ab, #ffde57);
}

.flask-gradient {
  background-image: linear-gradient(45deg, #000000, #333);
}

.java-gradient {
  background-image: linear-gradient(45deg, #f89820, #5382a1);
}

.mongo-gradient {
  background-image: linear-gradient(45deg, #47a248, #3f9942);
}

.mysql-gradient {
  background-image: linear-gradient(45deg, #0091ff, #f29111);
}

.git-gradient {
  background-image: linear-gradient(45deg, #f05032, #333);
}

.docker-gradient {
  background-image: linear-gradient(45deg, #2496ed, #1d6fa5);
}

.figma-gradient {
  background-image: linear-gradient(45deg, #f24e1e, #ffffff);
}

@media (max-width: 600px) {
  .technologies-section {
    padding: 3rem 1.5rem;
  }

  .tech-grid {
    grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
    gap: 1rem;
  }

  .tech-card {
    height: 110px;
    gap: 0.5rem;
  }

  .tech-card i {
    font-size: 2.5rem;
  }

  .tech-card span {
    font-size: 0.9rem;
  }
}
</style>
