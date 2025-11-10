<script setup>
import img1 from '/src/components/icons/javascript.svg';
import img2 from '/src/components/icons/python.svg';
import img3 from '/src/components/icons/html.svg';
import img4 from '/src/components/icons/java.svg';
import img6 from '/src/components/icons/react.svg';
import img7 from '/src/components/icons/vue.svg';
import img8 from '/src/components/icons/node.svg';
import img9 from '/src/components/icons/git.svg';
import img12 from '/src/components/icons/figma.svg';
import img13 from '/src/components/icons/visual-studio-code.svg';
import img17 from '/src/components/icons/lenguage.svg';
import img18 from '/src/components/icons/lenguages.svg';

import { ref } from 'vue';
const habilidades = ref([
  {
    id: 1,
    nombre: 'Lenguajes de Programación',
    habilidades: [
      { id: 1, nombre: 'JavaScript', nivel: 'Intermedio', icono: img1 },
      { id: 2, nombre: 'Python', nivel: 'Intermedio', icono: img2 },
      { id: 3, nombre: 'HTML/CSS', nivel: 'Avanzado', icono: img3 },
      { id: 4, nombre: 'Java', nivel: 'Intermedio', icono: img4 },
    ],
  },
  {
    id: 2,
    nombre: 'Frameworks y Librerías',
    habilidades: [
      { id: 1, nombre: 'React.js', nivel: 'Intermedio', icono: img6 },
      { id: 2, nombre: 'Vue.js', nivel: 'Intermedio', icono: img7 },
      { id: 3, nombre: 'Node.js', nivel: 'Intermedio', icono: img8 },
    ],
  },
  {
    id: 3,
    nombre: 'Herramientas y Software',
    habilidades: [
      { id: 1, nombre: 'Git', nivel: 'Avanzado', icono: img9 },
      { id: 4, nombre: 'Figma', nivel: 'Intermedio', icono: img12 },
      { id: 5, nombre: 'Visual Studio Code', nivel: 'Avanzado', icono: img13 },
    ],
  },
  {
    id: 5,
    nombre: 'Idiomas',
    habilidades: [
      { id: 1, nombre: 'Español', nivel: 'Nativo', icono: img17 },
      { id: 2, nombre: 'Inglés', nivel: 'Intermedio (B2)', icono: img18 },
    ],
  },
]);
</script>

<template>
  <section class="skills-section">
    <h1 class="skills-title">Habilidades</h1>

    <div class="skills-contenedor">
      <div
        v-for="categoria in habilidades"
        :key="categoria.id"
        class="skills-categoria"
      >
        <h3>{{ categoria.nombre }}</h3>
        <ul class="skills">
          <li
            v-for="hab in categoria.habilidades"
            :key="hab.id"
            class="skill"
          >
            <img :src="hab.icono" :alt="hab.nombre" />
            <div class="skill-info">
              <span class="skill-nombre">{{ hab.nombre }}</span>
              <span class="skill-nivel">{{ hab.nivel }}</span>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* 🔹 Sección principal */
.skills-section {
  padding: 4rem 2rem;
  color: #fff;
  text-align: center;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  box-shadow: 0 0 25px rgba(0, 255, 255, 0.1);
}

/* 🔹 Título general */
.skills-title {
  font-size: 2.8rem;
  margin-bottom: 3rem;
  letter-spacing: 2px;
  color: #ffffff;
  text-shadow: 0 0 15px rgba(255, 255, 255, 0.4);
}

/* 🔹 Contenedor de categorías */
.skills-contenedor {
  display: flex;
  flex-direction: column;
  gap: 3rem;
}

/* 🔹 Categorías */
.skills-categoria h3 {
  text-align: left;
  font-size: 1.6rem;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 1.2rem;
  border-left: 4px solid #ffffff;
  padding-left: 12px;
}


/* 🔹 Lista de habilidades */
.skills {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
}

/* 🔹 Tarjeta individual */
.skill {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 15px;
  padding: 1rem 1.5rem;
  min-width: 230px;
  max-width: 260px;
  box-shadow: 0 0 20px rgba(0, 255, 213, 0.05);
  transition: all 0.3s ease;
}

.skill:hover {
  transform: translateY(-5px);
  box-shadow: 0 0 25px rgba(0, 255, 213, 0.3);
  background: rgba(0, 255, 213, 0.15);
}

/* 🔹 Iconos */
.skill img {
  width: 40px;
  height: 40px;
}

/* 🔹 Texto */
.skill-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.skill-nombre {
  font-size: 1.1rem;
  font-weight: 600;
  color: #fff;
}

.skill-nivel {
  font-size: 0.9rem;
  color: #ffffff;
  opacity: 0.85;
}

/* 🔹 Responsivo */
@media (max-width: 768px) {
  .skills-categoria h3 {
    text-align: center;
  }

  .skills {
    justify-content: center;
  }

  .skill {
    width: 100%;
    max-width: 300px;
  }
}
</style>
