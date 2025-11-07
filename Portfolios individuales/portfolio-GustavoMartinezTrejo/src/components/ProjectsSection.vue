<template>
  <section id="proyectos" class="section fade-in">
    <h2>Proyectos</h2>
    
    <div class="projects-grid">
      <div
        v-for="(project, index) in projects"
        :key="index"
        class="project-card"
      >
        <div class="project-img">
          <img :src="project.image" :alt="project.title" />
        </div>
        <div class="project-title">{{ project.title }}</div>
        <div class="project-desc">{{ project.description }}</div>
        <div class="project-links">
          <a
            v-if="project.github"
            :href="project.github"
            class="btn-github"
            target="_blank"
            rel="noopener noreferrer"
          >
            GitHub
          </a>
          <a
            v-if="project.deploy"
            :href="project.deploy"
            class="btn-tech"
            target="_blank"
            rel="noopener noreferrer"
          >
            Deploy
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const projects = [
  {
    title: 'Pokedex',
    description: 'Descripción breve de qué hace tu proyecto y qué tecnologías usaste para desarrollarlo.',
    image: 'https://gm-poke.vercel.app/assets/welcome-image-C_jtqqXB.svg',
    github: 'https://github.com/GustavoMartinezFS/pokedex',
    deploy: 'https://gm-poke.vercel.app/'
  }
]
</script>

<style scoped>
.section {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 40px;
  margin-bottom: 30px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.section:hover {
  transform: translateY(-5px);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
}

h2 {
  color: #2c3e50;
  font-size: 2rem;
  margin-bottom: 30px;
  padding-bottom: 15px;
  border-bottom: 3px solid #667eea;
  position: relative;
}

h2::after {
  content: '';
  position: absolute;
  bottom: -3px;
  left: 0;
  width: 50px;
  height: 3px;
  background: #764ba2;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 30px;
  margin-top: 30px;
}

.project-card {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  padding: 25px;
  text-align: center;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.project-card:hover {
  transform: translateY(-10px);
  border-color: #667eea;
  box-shadow: 0 15px 30px rgba(102, 126, 234, 0.2);
}

.project-img {
  width: 100%;
  height: 200px;
  border-radius: 10px;
  margin-bottom: 15px;
  overflow: hidden;
}

.project-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.project-title {
  font-size: 1.4rem;
  font-weight: bold;
  color: #2c3e50;
  margin-bottom: 10px;
}

.project-desc {
  color: #7f8c8d;
  margin-bottom: 20px;
}

.project-links {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
}

.project-links a {
  padding: 8px 16px;
  border-radius: 20px;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: bold;
  transition: all 0.3s ease;
  color: white;
}

.btn-github {
  background: #2c3e50;
}

.btn-tech {
  background: #e74c3c;
}

.btn-github:hover,
.btn-tech:hover {
  transform: scale(1.1);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

@media (max-width: 768px) {
  .section {
    padding: 20px;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
}
</style>