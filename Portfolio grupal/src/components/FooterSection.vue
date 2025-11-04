<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="container">
        <div class="footer-grid">
          <!-- Columna 1: Información -->
          <div class="footer-column">
            <h3 class="footer-title">UTN San Rafael</h3>
            <p class="footer-description">
              Grupo de estudiantes de la Tecnicatura Universitaria en Programación, 
              comprometidos con la excelencia académica y el desarrollo tecnológico.
            </p>
            <div class="footer-social">
              <a href="https://github.com" target="_blank" aria-label="GitHub">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
              </a>
              <a href="https://linkedin.com" target="_blank" aria-label="LinkedIn">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                </svg>
              </a>
              <a href="mailto:grupo@utn.edu.ar" aria-label="Email">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                  <polyline points="22,6 12,13 2,6"></polyline>
                </svg>
              </a>
            </div>
          </div>
          
          <!-- Columna 2: Enlaces Rápidos -->
          <div class="footer-column">
            <h4 class="footer-heading">Enlaces Rápidos</h4>
            <ul class="footer-links">
              <li><a href="#inicio">Inicio</a></li>
              <li><a href="#nosotros">Sobre Nosotros</a></li>
              <li><a href="#equipo">Equipo</a></li>
              <li><a href="#tecnologias">Tecnologías</a></li>
              <li><a href="#proyectos">Proyectos</a></li>
              <li><a href="#contacto">Contacto</a></li>
            </ul>
          </div>
          
          <!-- Columna 3: Tecnologías -->
          <div class="footer-column">
            <h4 class="footer-heading">Tecnologías</h4>
            <ul class="footer-links">
              <li><a href="#tecnologias">Java</a></li>
              <li><a href="#tecnologias">Python</a></li>
              <li><a href="#tecnologias">JavaScript</a></li>
              <li><a href="#tecnologias">MySQL</a></li>
              <li><a href="#tecnologias">Git & GitHub</a></li>
            </ul>
          </div>
          
          <!-- Columna 4: Contacto -->
          <div class="footer-column">
            <h4 class="footer-heading">Contacto</h4>
            <ul class="footer-contact">
              <li>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
                <span>San Rafael, Mendoza<br/>Argentina</span>
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                  <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
                </svg>
                <span>UTN Facultad Regional<br/>San Rafael</span>
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                  <polyline points="22,6 12,13 2,6"></polyline>
                </svg>
                <span>grupo.programacion@utn.edu.ar</span>
              </li>
            </ul>
          </div>
        </div>
        
        <!-- Separador -->
        <div class="footer-divider"></div>
        
        <!-- Sección inferior -->
        <div class="footer-bottom">
          <div class="footer-copyright">
            <p>© {{ currentYear }} Portfolio Grupal - Tecnicatura en Programación</p>
            <p>Universidad Tecnológica Nacional - Facultad Regional San Rafael</p>
          </div>
          
          <div class="footer-team">
            <p>Desarrollado con ❤️ por:</p>
            <p class="team-names">
              Aymar • Capitani • Lucero • Mandile • Martinez Trejo • 
              Mendoza • Mulinetti • Velasco • Zanatta
            </p>
          </div>
          
          <div class="footer-tech">
            <p>Construido con <strong>Vue.js</strong> y <strong>Vite</strong></p>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Botón volver arriba -->
    <button 
      v-if="showScrollTop"
      @click="scrollToTop" 
      class="scroll-top-btn"
      aria-label="Volver arriba"
    >
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="18 15 12 9 6 15"></polyline>
      </svg>
    </button>
  </footer>
</template>

<script>
export default {
  name: 'FooterSection',
  data() {
    return {
      currentYear: new Date().getFullYear(),
      showScrollTop: false
    }
  },
  methods: {
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      })
    },
    handleScroll() {
      this.showScrollTop = window.scrollY > 500
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style scoped>
.footer {
  background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
  color: white;
  position: relative;
}

.footer-content {
  padding: 4rem 0 2rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 3rem;
  margin-bottom: 3rem;
}

.footer-column {
  display: flex;
  flex-direction: column;
}

.footer-title {
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 1rem;
  background: linear-gradient(45deg, #ec4899, #f97316);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.footer-description {
  font-size: 0.95rem;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 1.5rem;
}

.footer-social {
  display: flex;
  gap: 1rem;
}

.footer-social a {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  transition: all 0.3s ease;
}

.footer-social a:hover {
  background: var(--color-accent);
  transform: translateY(-3px);
}

.footer-heading {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  color: white;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.footer-links li a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  display: inline-block;
}

.footer-links li a:hover {
  color: white;
  transform: translateX(5px);
}

.footer-contact {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.footer-contact li {
  display: flex;
  gap: 1rem;
  align-items: flex-start;
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
  line-height: 1.6;
}

.footer-contact li svg {
  flex-shrink: 0;
  margin-top: 2px;
}

.footer-divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.1);
  margin: 2rem 0;
}

.footer-bottom {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.footer-copyright p {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.9rem;
  line-height: 1.6;
}

.footer-team {
  padding: 1.5rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
}

.footer-team p {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.team-names {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.85rem;
}

.footer-tech {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.9rem;
}

.footer-tech strong {
  color: var(--color-accent);
  font-weight: 600;
}

.scroll-top-btn {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: var(--color-primary);
  border: none;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 5px 20px rgba(99, 102, 241, 0.4);
  transition: all 0.3s ease;
  z-index: 999;
}

.scroll-top-btn:hover {
  background: var(--color-secondary);
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(99, 102, 241, 0.5);
}

@media (max-width: 1024px) {
  .footer-grid {
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
}

@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: 1fr;
    text-align: center;
  }
  
  .footer-social {
    justify-content: center;
  }
  
  .footer-links,
  .footer-contact {
    align-items: center;
  }
  
  .footer-links li a:hover {
    transform: none;
  }
  
  .footer-contact li {
    justify-content: center;
  }
  
  .scroll-top-btn {
    bottom: 1rem;
    right: 1rem;
    width: 45px;
    height: 45px;
  }
}
</style>