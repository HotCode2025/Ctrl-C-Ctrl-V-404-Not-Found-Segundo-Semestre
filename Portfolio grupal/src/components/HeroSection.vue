<template>
  <section id="inicio" class="hero">
    <div class="hero-bg"></div>
    <div class="hero-grid-overlay"></div>

    <div class="container hero-inner">
      <p class="hero-eyebrow">Tecnicatura Universitaria en Programación</p>

      <h1 class="hero-title">
        Construimos software.<br />
        <span class="hero-title--accent">Con propósito.</span>
      </h1>

      <div class="hero-line"></div>

      <p class="hero-description">
        Somos un equipo de estudiantes de la UTN Facultad Regional San Rafael,
        apasionados por la tecnología y comprometidos con el desarrollo de
        software de calidad.
      </p>

      <div class="hero-actions">
        <a href="#equipo" class="btn btn-primary">Conocer al Equipo</a>
        <a href="#proyectos" class="btn btn-outline">Ver Proyectos</a>
      </div>
    </div>

    <a href="#nosotros" class="hero-scroll">
      <span>Scroll</span>
      <svg width="16" height="24" viewBox="0 0 16 24" fill="none">
        <rect x="1" y="1" width="14" height="22" rx="7" stroke="currentColor" stroke-width="1.5"/>
        <circle class="scroll-dot" cx="8" cy="7" r="2" fill="currentColor"/>
      </svg>
    </a>
  </section>
</template>

<script>
export default { name: 'HeroSection' }
</script>

<style scoped>
.hero {
  min-height: 100vh;
  background: var(--navy);
  display: flex;
  align-items: center;
  position: relative;
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 80% 60% at 60% 40%, rgba(201,169,110,0.06) 0%, transparent 70%),
              radial-gradient(ellipse 60% 80% at 20% 80%, rgba(201,169,110,0.04) 0%, transparent 60%);
}

.hero-grid-overlay {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 60px 60px;
}

.hero-inner {
  position: relative;
  z-index: 1;
  padding-top: 8rem;
  padding-bottom: 6rem;
}

.hero-eyebrow {
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 1.5rem;
}

.hero-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(2.8rem, 6vw, 5rem);
  font-weight: 700;
  color: var(--cream);
  line-height: 1.1;
  letter-spacing: -0.02em;
  margin-bottom: 2rem;
}

.hero-title--accent {
  color: var(--gold);
}

.hero-line {
  width: 64px;
  height: 1px;
  background: var(--gold);
  margin-bottom: 2rem;
  opacity: 0.7;
}

.hero-description {
  font-size: 1.05rem;
  color: rgba(240,235,225,0.65);
  max-width: 520px;
  line-height: 1.8;
  margin-bottom: 3rem;
  font-weight: 300;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.hero-scroll {
  position: absolute;
  bottom: 2.5rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  color: rgba(255,255,255,0.3);
  text-decoration: none;
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  transition: color 0.25s;
}

.hero-scroll:hover { color: var(--gold); }

.scroll-dot {
  animation: scrollBounce 2s ease-in-out infinite;
}

@keyframes scrollBounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(8px); }
}

@media (max-width: 768px) {
  .hero-title { font-size: 2.5rem; }
  .hero-description { font-size: 0.95rem; }
  .hero-actions { flex-direction: column; max-width: 260px; }
  .btn { text-align: center; }
}
</style>
