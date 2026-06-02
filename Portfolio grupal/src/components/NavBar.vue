<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="container nav-container">
      <div class="nav-logo">
        <span class="logo-main">UTN</span>
        <span class="logo-sep">·</span>
        <span class="logo-sub">San Rafael</span>
      </div>

      <ul class="nav-menu" :class="{ active: isMenuOpen }">
        <li><a href="#inicio" @click="closeMenu">Inicio</a></li>
        <li><a href="#nosotros" @click="closeMenu">Nosotros</a></li>
        <li><a href="#equipo" @click="closeMenu">Equipo</a></li>
        <li><a href="#tecnologias" @click="closeMenu">Tecnologías</a></li>
        <li><a href="#proyectos" @click="closeMenu">Proyectos</a></li>
        <li><a href="#contacto" @click="closeMenu">Contacto</a></li>
      </ul>

      <div class="nav-hamburger" @click="toggleMenu" :class="{ active: isMenuOpen }">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  data() {
    return {
      isMenuOpen: false,
      isScrolled: false
    }
  },
  methods: {
    toggleMenu() { this.isMenuOpen = !this.isMenuOpen },
    closeMenu() { this.isMenuOpen = false },
    handleScroll() { this.isScrolled = window.scrollY > 60 }
  },
  mounted() { window.addEventListener('scroll', this.handleScroll) },
  beforeUnmount() { window.removeEventListener('scroll', this.handleScroll) }
}
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 1.5rem 0;
  z-index: 1000;
  transition: background 0.35s ease, padding 0.35s ease, box-shadow 0.35s ease;
  background: transparent;
}

.navbar.scrolled {
  background: rgba(13, 14, 26, 0.97);
  backdrop-filter: blur(12px);
  padding: 1rem 0;
  box-shadow: 0 1px 0 rgba(255,255,255,0.05);
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-logo {
  display: flex;
  align-items: baseline;
  gap: 0.4rem;
  text-decoration: none;
}

.logo-main {
  font-family: 'Playfair Display', serif;
  font-size: 1.4rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.05em;
}

.logo-sep {
  color: var(--gold);
  font-size: 1.2rem;
}

.logo-sub {
  font-family: 'Inter', sans-serif;
  font-size: 0.8rem;
  font-weight: 300;
  color: rgba(255,255,255,0.55);
  letter-spacing: 0.15em;
  text-transform: uppercase;
}

.nav-menu {
  display: flex;
  list-style: none;
  gap: 2.5rem;
}

.nav-menu li a {
  color: rgba(255,255,255,0.75);
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 400;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  transition: color 0.25s ease;
  position: relative;
  padding-bottom: 4px;
}

.nav-menu li a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 1px;
  background: var(--gold);
  transition: width 0.3s ease;
}

.nav-menu li a:hover {
  color: #ffffff;
}

.nav-menu li a:hover::after {
  width: 100%;
}

.nav-hamburger {
  display: none;
  flex-direction: column;
  cursor: pointer;
  gap: 6px;
}

.nav-hamburger span {
  width: 24px;
  height: 1px;
  background: white;
  transition: all 0.3s ease;
}

.nav-hamburger.active span:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}
.nav-hamburger.active span:nth-child(2) {
  opacity: 0;
}
.nav-hamburger.active span:nth-child(3) {
  transform: rotate(-45deg) translate(5px, -5px);
}

@media (max-width: 768px) {
  .nav-hamburger { display: flex; }

  .nav-menu {
    position: fixed;
    top: 0;
    right: -100%;
    flex-direction: column;
    background: var(--navy);
    width: 280px;
    height: 100vh;
    padding: 6rem 2.5rem;
    gap: 2rem;
    transition: right 0.35s ease;
    box-shadow: -4px 0 40px rgba(0,0,0,0.4);
  }

  .nav-menu.active { right: 0; }

  .nav-menu li a {
    font-size: 1rem;
    color: rgba(255,255,255,0.85);
  }
}
</style>
