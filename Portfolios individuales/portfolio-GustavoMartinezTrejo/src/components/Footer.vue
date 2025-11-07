<template>
  <footer>
    <div class="footer-content">
      <div class="footer-links">
        <a
          v-for="item in menuItems"
          :key="item.id"
          @click.prevent="scrollToSection(item.id)"
          :href="`#${item.id}`"
        >
          {{ item.label }}
        </a>
      </div>
      
      <div class="social-links">
        <a
          href="https://www.linkedin.com/in/martinez-trejo-gustavo/"
          class="social-link"
          target="_blank"
          rel="noopener noreferrer"
          title="LinkedIn"
        >
          in
        </a>
        <a
          href="https://github.com/GustavoMartinezFS"
          class="social-link"
          target="_blank"
          rel="noopener noreferrer"
          title="GitHub"
        >
          git
        </a>
        <a
          href="mailto:martinez.trejo.gustavo.a@gmail.com"
          class="social-link"
          title="Email"
        >
          @
        </a>
      </div>
      
      <div class="copyright">
        <p>&copy; 2025 Gustavo Alfredo Martinez Trejo. Todos los derechos reservados.</p>
        <p>Hecho con ❤️ y mucho código</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
const menuItems = [
  { id: 'inicio', label: 'Inicio' },
  { id: 'experiencia', label: 'Experiencia' },
  { id: 'estudios', label: 'Estudios' },
  { id: 'proyectos', label: 'Proyectos' },
  { id: 'contacto', label: 'Contacto' }
]

const scrollToSection = (id) => {
  const element = document.getElementById(id)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
}
</script>

<style scoped>
footer {
  background: rgba(44, 62, 80, 0.95);
  backdrop-filter: blur(10px);
  color: white;
  text-align: center;
  padding: 40px 20px;
  margin-top: 50px;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
}

.footer-links {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.footer-links a {
  color: #ecf0f1;
  text-decoration: none;
  transition: color 0.3s ease;
  cursor: pointer;
}

.footer-links a:hover {
  color: #667eea;
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin: 30px 0;
}

.social-link {
  width: 50px;
  height: 50px;
  background: linear-gradient(45deg, #667eea, #764ba2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-decoration: none;
  font-weight: bold;
  transition: all 0.3s ease;
}

.social-link:hover {
  transform: translateY(-5px) scale(1.1);
  box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
}

.copyright {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 20px;
  color: #bdc3c7;
}

@media (max-width: 768px) {
  .footer-links {
    flex-direction: column;
    gap: 15px;
  }
}
</style>