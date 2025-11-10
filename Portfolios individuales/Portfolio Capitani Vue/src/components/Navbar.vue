<template>
  <nav class="navbar">
    <h3>Portafolio Personal</h3>
    <div class="navegation">
      <a v-for="item in navegation" :key="item.id" :href="item.link">{{ item.name }}</a>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
const navegation = ref([
  { id: 1, name: 'Proyectos', link: '#project' },
  { id: 2, name: 'Contacto', link: '#contact' },
])
</script>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 10%;
  border-bottom: 1px solid var(--grey);
  flex-wrap: wrap;
  gap: 15px;
}

h3 {
  color: var(--primary);
  flex-shrink: 0;
  font-size: 1.25rem;
  transition: font-size 0.3s ease;
}

.navegation {
  display: flex;
  gap: 20px;
  transition: gap 0.3s ease;
}

.navegation a {
  color: var(--text-primary);
  font-weight: 500;
  transition:
    color 0.3s ease,
    font-size 0.3s ease;
  font-size: 1rem;
}

.navegation a:hover {
  color: var(--accent);
}

/* Responsive */
@media (max-width: 768px) {
  nav {
    padding: 15px 5%;
  }
}

@media (max-width: 480px) {
  nav {
    padding: 15px 2%;
    justify-content: center;
  }

  h3 {
    font-size: 1.1rem;
  }

  .navegation {
    gap: 10px;
  }

  .navegation a {
    font-size: 0.9rem;
  }
}
</style>
