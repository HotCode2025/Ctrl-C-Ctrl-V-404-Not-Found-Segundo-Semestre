<template>
  <section class="education-section">
    <h2>Mi Educación</h2>
    <div class="horizontal-timeline">
      <div v-for="item in education" :key="item.id" class="timeline-item">
        <div class="timeline-point" :class="{ active: item.isFlipped }"></div>

        <div class="flip-card-scene">
          <div
            class="flip-card-inner"
            :class="{ 'is-flipped': item.isFlipped }"
            @click="item.isFlipped = !item.isFlipped"
          >
            <div class="timeline-card card-front">
              <time class="years">{{ item.years }}</time>
              <h3 class="degree">{{ item.degree }}</h3>
              <p class="institution">{{ item.institution }}</p>
              <span class="flip-indicator">Tocar para más info</span>
            </div>

            <div class="timeline-card card-back">
              <p class="description">{{ item.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const education = ref([
  {
    id: 1,
    degree: 'Tecnico Informatico',
    institution: 'Escuela Técnica de la Universidad de Mendoza',
    years: '2018-2023',
    description:
      'Formación integral en hardware, software y redes. Adquirí una base sólida en mantenimiento de sistemas, arquitectura de computadoras y los principios fundamentales de la programación y bases de datos.',
    isFlipped: false,
  },
  {
    id: 2,
    degree: 'Ingeniero Informático',
    institution: 'Universidad de Mendoza',
    years: '2024-2025',
    description:
      'Profundización en algoritmos complejos, arquitectura de software y paradigmas de programación avanzados. El enfoque está en el diseño de soluciones tecnológicas eficientes, escalables y seguras.',
    isFlipped: false,
  },
  {
    id: 3,
    degree: 'Tecnico en Programación',
    institution: 'Universidad Tecnológica Nacional',
    years: '2025-Actualidad',
    description:
      'Carrera intensiva centrada en el desarrollo de software práctico. Especialización en stacks de tecnologías modernas, metodologías ágiles y la construcción de aplicaciones full-stack.',
    isFlipped: false,
  },
])
</script>

<style scoped>
.education-section {
  padding: 4rem 2rem;
  background-color: var(--light-grey);
  text-align: center;

  .horizontal-timeline {
    display: flex;
    justify-content: space-between;
    position: relative;
    width: 80%;
    margin: 0 auto;

    &::before {
      content: '';
      position: absolute;
      top: 10px;
      left: 0;
      width: 100%;
      height: 4px;
      background-color: var(--grey, #6c757d);
    }
  }
}

.timeline-item {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: calc(100% / 3);

  /* Point in the timeline */
  .timeline-point {
    width: 24px;
    height: 24px;
    background-color: var(--white, #fff);
    border: 4px solid var(--primary, #0d6efd);
    border-radius: 50%;
    position: relative;
    z-index: 2;
    margin-bottom: 1.5rem;
    transition: border-color 0.4s ease;

    &.active {
      border-color: var(--accent);
    }
  }

  /* Card Movement */
  .flip-card-scene {
    width: 90%;
    height: 220px;
    perspective: 1000px;
    cursor: pointer;

    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      transition: transform 0.8s;
      transform-style: preserve-3d;

      &.is-flipped {
        transform: rotateY(180deg);
      }
    }
  }
}

.flip-card-inner {
  .timeline-card {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    background-color: var(--white, #fff);
    border-radius: 8px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .card-back {
    transform: rotateY(180deg);
    justify-content: center;
    position: relative;

    &::before {
      content: '“';
      position: absolute;
      top: 1rem;
      left: 1.5rem;
      font-size: 5rem;
      color: var(--light-grey, #e2e2e2);
      font-family: 'Times New Roman', serif;
      z-index: 0;
      line-height: 1;
    }
  }
}

/* Card Content */
.timeline-card {
  .years {
    display: inline-block;
    background-color: var(--primary, #0d6efd);
    color: var(--white, #fff);
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 1rem;
  }
  .degree {
    font-size: 1.15rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
  }
  .institution {
    font-size: 0.95rem;
    color: var(--text-secondary);
  }
  .flip-indicator {
    font-size: 0.75rem;
    color: #adb5bd;
    margin-top: 1rem;
    font-style: italic;
  }
  .description {
    font-size: 0.95rem;
    color: var(--text-secondary);
    line-height: 1.6;
    position: relative;
    z-index: 1;
  }
}

/* Responsive */

@media (max-width: 900px) {
  .education-section .horizontal-timeline {
    /* Change the direction of the flex to see the timeline vertically */
    flex-direction: column;
    width: 100%;
    max-width: 450px;

    /* Redrew the line from horizontal to vertical. */
    &::before {
      top: 0;
      left: 10px;
      width: 4px;
      height: 100%;
    }
  }

  .timeline-item {
    width: 100%;
    align-items: flex-start;
    padding-left: 40px;
    margin-bottom: 2rem;
  }

  .timeline-item:last-child {
    margin-bottom: 0;
  }

  .timeline-item .timeline-point {
    position: absolute;
    left: 0;
    top: 0;
    margin-bottom: 0;
  }

  .timeline-item .flip-card-scene {
    width: 100%;
    height: 230px;
  }
}

@media (max-width: 480px) {
  .education-section {
    padding: 3rem 1rem;
  }
}
</style>
