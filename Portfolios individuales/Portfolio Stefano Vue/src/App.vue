<script setup>
import AboutMe from "./components/AboutMe.vue";
import Experience from "./components/Experience.vue";
import Projects from "./components/Projects.vue";
import Skills from "./components/Skills.vue";
import Contact from "./components/Contact.vue";
</script>

<template>
  <header class="navbar">
    <div class="navbar-content">
      <div class="brand">
        <h1>Stéfano Aymar</h1>
        <span class="subtitle">Técnico Universitario en Programación</span>
      </div>
      <nav>
        <ul class="nav-list">
          <li><a href="#about">Sobre Mi</a></li>
          <li><a href="#experience">Experiencia</a></li>
          <li><a href="#projects">Proyectos</a></li>
          <li><a href="#skills">Conocimientos</a></li>
          <li><a href="#contact">Contacto</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main>
    <AboutMe />
    <Experience />
    <Projects />
    <Skills />
    <Contact />
  </main>
</template>

<style scoped>
.navbar {
  position: sticky;
  top: 0;
  width: 100%;
  background: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(10px);
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.08);
  z-index: 1000;
  border-bottom: 1px solid rgba(0, 121, 107, 0.1);
}

.navbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem 2rem;
}

.brand h1 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 0.2rem;
  background: linear-gradient(135deg, #00796b, #004d40);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.subtitle {
  font-size: 1rem;
  color: #00796b;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.nav-list {
  display: flex;
  gap: 2rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-list a {
  color: #2c3e50;
  font-weight: 500;
  font-size: 1.05rem;
  padding: 0.5rem 1rem;
  border-radius: 0.75rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.nav-list a:hover {
  background: linear-gradient(135deg, #e0f7fa, #b2ebf2);
  color: #00796b;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 121, 107, 0.15);
}

.nav-list a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background: #00796b;
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

.nav-list a:hover::after {
  width: 80%;
}

@media (max-width: 768px) {
  .navbar-content {
    flex-direction: column;
    align-items: flex-start;
    padding: 1rem;
    gap: 1rem;
  }
  
  .nav-list {
    gap: 1rem;
    font-size: 0.95rem;
    flex-wrap: wrap;
  }
  
  .brand h1 {
    font-size: 1.5rem;
  }
}
</style>