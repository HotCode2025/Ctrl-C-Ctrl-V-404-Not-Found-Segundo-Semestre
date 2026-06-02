<template>
  <section id="nosotros" class="about">
    <div class="container">
      <p class="section-subtitle">Quiénes somos</p>
      <h2 class="section-title">Sobre Nosotros</h2>
      <div class="section-divider"></div>

      <div class="about-cards">
        <div class="about-card" v-for="(item, i) in cards" :key="i">
          <div class="card-num">{{ String(i + 1).padStart(2, '0') }}</div>
          <h3>{{ item.title }}</h3>
          <p>{{ item.text }}</p>
        </div>
      </div>

      <div class="about-university">
        <div class="university-text">
          <p class="section-subtitle section-subtitle--gold">Institución</p>
          <h3>Universidad Tecnológica Nacional</h3>
          <p class="university-location">Facultad Regional San Rafael — Mendoza, Argentina</p>
          <p class="university-description">
            La UTN es reconocida por su excelencia en carreras técnicas y de ingeniería.
            Nuestra formación combina bases teóricas sólidas con práctica real, preparándonos
            como profesionales competentes en el desarrollo de software.
          </p>
        </div>

        <div class="university-stats">
          <div class="stat" v-for="(s, i) in stats" :key="i">
            <span class="stat-num">{{ s.num }}</span>
            <span class="stat-label">{{ s.label }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'AboutUs',
  data() {
    return {
      cards: [
        {
          title: 'Nuestra Misión',
          text: 'Formarnos como profesionales en programación, adquiriendo conocimientos sólidos en desarrollo de software y preparándonos para los desafíos tecnológicos del mundo actual.'
        },
        {
          title: 'Quiénes Somos',
          text: 'Somos estudiantes de la Tecnicatura Universitaria en Programación de la UTN San Rafael, unidos por la pasión por la tecnología y el compromiso con el aprendizaje continuo.'
        },
        {
          title: 'Nuestros Objetivos',
          text: 'Desarrollar habilidades técnicas y blandas, trabajar en equipo, crear proyectos innovadores y contribuir al ecosistema tecnológico de nuestra región y país.'
        }
      ],
      stats: [
        { num: '9', label: 'Integrantes' },
        { num: '6+', label: 'Tecnologías' },
        { num: '100%', label: 'Compromiso' }
      ]
    }
  }
}
</script>

<style scoped>
.about {
  padding: 7rem 0;
  background: var(--white);
}

.section-subtitle--gold {
  color: var(--gold);
}

.about-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5px;
  background: var(--border);
  border: 1px solid var(--border);
  margin-bottom: 5rem;
  overflow: hidden;
}

.about-card {
  background: var(--white);
  padding: 2.5rem;
  transition: background 0.25s;
}

.about-card:hover {
  background: var(--cream);
}

.card-num {
  font-family: 'Playfair Display', serif;
  font-size: 3rem;
  font-weight: 700;
  color: var(--gold);
  opacity: 0.35;
  line-height: 1;
  margin-bottom: 1.25rem;
}

.about-card h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.25rem;
  color: var(--navy);
  margin-bottom: 1rem;
  font-weight: 600;
}

.about-card p {
  font-size: 0.95rem;
  color: var(--text-mid);
  line-height: 1.8;
}

.about-university {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 4rem;
  align-items: center;
  padding: 3.5rem;
  border: 1px solid var(--border);
  background: var(--cream);
}

.university-text h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.6rem;
  color: var(--navy);
  margin-bottom: 0.4rem;
}

.university-location {
  font-size: 0.85rem;
  letter-spacing: 0.08em;
  color: var(--gold);
  text-transform: uppercase;
  margin-bottom: 1.25rem;
  font-weight: 500;
}

.university-description {
  font-size: 0.95rem;
  color: var(--text-mid);
  line-height: 1.8;
  max-width: 560px;
}

.university-stats {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  border-left: 1px solid var(--border);
  padding-left: 3rem;
}

.stat {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.stat-num {
  font-family: 'Playfair Display', serif;
  font-size: 2.25rem;
  font-weight: 700;
  color: var(--navy);
  line-height: 1;
}

.stat-label {
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-muted);
}

@media (max-width: 768px) {
  .about-university {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }

  .university-stats {
    flex-direction: row;
    border-left: none;
    border-top: 1px solid var(--border);
    padding-left: 0;
    padding-top: 2rem;
    justify-content: space-around;
  }
}
</style>
