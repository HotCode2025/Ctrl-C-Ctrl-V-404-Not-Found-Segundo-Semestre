<template>
  <nav class="navbar">
    <div class="container nav-container">
      <!-- Logo -->
      <div class="nav-logo">
        <h2>UTN San Rafael</h2>
      </div>
      
      <!-- Menu Desktop -->
      <ul class="nav-menu" :class="{ active: isMenuOpen }">
        <li><a href="#inicio" @click="closeMenu">Inicio</a></li>
        <li><a href="#nosotros" @click="closeMenu">Nosotros</a></li>
        <li><a href="#equipo" @click="closeMenu">Equipo</a></li>
        <li><a href="#tecnologias" @click="closeMenu">Tecnologías</a></li>
        <li><a href="#proyectos" @click="closeMenu">Proyectos</a></li>
        <li><a href="#contacto" @click="closeMenu">Contacto</a></li>
      </ul>
      
      <!-- Hamburger Menu -->
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
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen
    },
    closeMenu() {
      this.isMenuOpen = false
    },
    handleScroll() {
      this.isScrolled = window.scrollY > 50
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
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background: rgba(30, 27, 75, 0.95);
  backdrop-filter: blur(10px);
  padding: 1rem 0;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-logo h2 {
  color: white;
  font-size: 1.5rem;
  font-weight: 700;
}

.nav-menu {
  display: flex;
  list-style: none;
  gap: 2rem;
}

.nav-menu li a {
  color: white;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
  position: relative;
}

.nav-menu li a:hover {
  color: var(--color-accent);
}

.nav-menu li a::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--color-accent);
  transition: width 0.3s ease;
}

.nav-menu li a:hover::after {
  width: 100%;
}

.nav-hamburger {
  display: none;
  flex-direction: column;
  cursor: pointer;
  gap: 5px;
}

.nav-hamburger span {
  width: 25px;
  height: 3px;
  background: white;
  border-radius: 3px;
  transition: all 0.3s ease;
}

.nav-hamburger.active span:nth-child(1) {
  transform: rotate(45deg) translate(8px, 8px);
}

.nav-hamburger.active span:nth-child(2) {
  opacity: 0;
}

.nav-hamburger.active span:nth-child(3) {
  transform: rotate(-45deg) translate(7px, -7px);
}

@media (max-width: 768px) {
  .nav-hamburger {
    display: flex;
  }
  
  .nav-menu {
    position: fixed;
    top: 70px;
    right: -100%;
    flex-direction: column;
    background: rgba(30, 27, 75, 0.98);
    width: 100%;
    padding: 2rem;
    transition: right 0.3s ease;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  }
  
  .nav-menu.active {
    right: 0;
  }
}
</style>