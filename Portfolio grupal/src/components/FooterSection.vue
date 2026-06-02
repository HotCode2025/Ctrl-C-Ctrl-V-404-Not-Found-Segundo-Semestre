<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col footer-col--wide">
          <div class="footer-brand">
            <span class="brand-main">UTN</span>
            <span class="brand-sep">·</span>
            <span class="brand-sub">San Rafael</span>
          </div>
          <p class="footer-desc">
            Grupo de estudiantes de la Tecnicatura Universitaria en Programación,
            comprometidos con la excelencia académica y el desarrollo tecnológico.
          </p>
          <div class="footer-social">
            <a href="https://github.com" target="_blank" aria-label="GitHub">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
              </svg>
            </a>
            <a href="https://linkedin.com" target="_blank" aria-label="LinkedIn">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
              </svg>
            </a>
            <a href="mailto:grupo@utn.edu.ar" aria-label="Email">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,13 2,6"/>
              </svg>
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Navegación</h4>
          <ul>
            <li><a href="#inicio">Inicio</a></li>
            <li><a href="#nosotros">Nosotros</a></li>
            <li><a href="#equipo">Equipo</a></li>
            <li><a href="#tecnologias">Tecnologías</a></li>
            <li><a href="#proyectos">Proyectos</a></li>
            <li><a href="#contacto">Contacto</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Tecnologías</h4>
          <ul>
            <li><a href="#tecnologias">Java</a></li>
            <li><a href="#tecnologias">Python</a></li>
            <li><a href="#tecnologias">JavaScript</a></li>
            <li><a href="#tecnologias">MySQL</a></li>
            <li><a href="#tecnologias">Git & GitHub</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Contacto</h4>
          <ul class="contact-list">
            <li>San Rafael, Mendoza<br />Argentina</li>
            <li>UTN Facultad Regional<br />San Rafael</li>
            <li>grupo.programacion<br />@utn.edu.ar</li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p class="footer-copy">&copy; {{ currentYear }} Portfolio Grupal — Tecnicatura en Programación · UTN San Rafael</p>
        <p class="footer-team">
          Aymar · Capitani · Lucero · Jauregui · Martinez Trejo · Mendoza · Mulinetti · Vargas · Zanatta
        </p>
      </div>
    </div>

    <button
      v-if="showScrollTop"
      @click="scrollToTop"
      class="scroll-top"
      aria-label="Volver arriba"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <polyline points="18 15 12 9 6 15"/>
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
    scrollToTop() { window.scrollTo({ top: 0, behavior: 'smooth' }) },
    handleScroll() { this.showScrollTop = window.scrollY > 500 }
  },
  mounted() { window.addEventListener('scroll', this.handleScroll) },
  beforeUnmount() { window.removeEventListener('scroll', this.handleScroll) }
}
</script>

<style scoped>
.footer {
  background: var(--navy);
  padding: 5rem 0 2rem;
  position: relative;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 4rem;
  padding-bottom: 4rem;
  border-bottom: 1px solid var(--border-dark);
  margin-bottom: 2.5rem;
}

.footer-col h4 {
  font-family: 'Inter', sans-serif;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 1.5rem;
}

.footer-col ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.footer-col ul li a {
  font-size: 0.875rem;
  color: rgba(240,235,225,0.5);
  text-decoration: none;
  transition: color 0.2s;
}

.footer-col ul li a:hover { color: var(--cream); }

.contact-list li {
  font-size: 0.875rem;
  color: rgba(240,235,225,0.5);
  line-height: 1.6;
}

.footer-brand {
  display: flex;
  align-items: baseline;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}

.brand-main {
  font-family: 'Playfair Display', serif;
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--cream);
  letter-spacing: 0.05em;
}

.brand-sep { color: var(--gold); }

.brand-sub {
  font-size: 0.75rem;
  font-weight: 300;
  color: rgba(255,255,255,0.35);
  letter-spacing: 0.15em;
  text-transform: uppercase;
}

.footer-desc {
  font-size: 0.875rem;
  color: rgba(240,235,225,0.45);
  line-height: 1.75;
  margin-bottom: 1.75rem;
  max-width: 300px;
}

.footer-social {
  display: flex;
  gap: 0.75rem;
}

.footer-social a {
  width: 34px;
  height: 34px;
  border: 1px solid var(--border-dark);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255,255,255,0.4);
  transition: all 0.25s;
}

.footer-social a:hover {
  border-color: var(--gold);
  color: var(--gold);
}

.footer-bottom {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  align-items: center;
  text-align: center;
}

.footer-copy {
  font-size: 0.8rem;
  color: rgba(240,235,225,0.3);
}

.footer-team {
  font-size: 0.75rem;
  color: rgba(240,235,225,0.2);
  letter-spacing: 0.05em;
}

.scroll-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 44px;
  height: 44px;
  border: 1px solid rgba(255,255,255,0.15);
  background: var(--navy-mid);
  color: rgba(255,255,255,0.5);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s;
  z-index: 999;
}

.scroll-top:hover {
  border-color: var(--gold);
  color: var(--gold);
}

@media (max-width: 1024px) {
  .footer-grid { grid-template-columns: 1fr 1fr; gap: 3rem; }
}

@media (max-width: 640px) {
  .footer-grid { grid-template-columns: 1fr; gap: 2.5rem; text-align: center; }
  .footer-social { justify-content: center; }
  .footer-desc { margin-left: auto; margin-right: auto; }
}
</style>
