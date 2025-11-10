<script setup>
import linkedin from '/src/components/icons/linkedin_icon.svg';
import instagram from '/src/components/icons/instagram_icon.svg';
import github from '/src/components/icons/github_icon.svg';

const title = "Rocio Lucero";
const descripcion = "Tecnicatura Universitaria en Programación - UTN";
const residencia = "San Rafael, Mendoza, Argentina";
const presentacion = "Bienvenidos a mi portafolio personal";
const redesSociales = [
  { id: 1, name: linkedin, src: linkedin, url: "https://www.linkedin.com/in/rocio-lucero-821b02160/" },
  { id: 2, name: instagram, src: instagram, url: "https://www.instagram.com/rocioluceroalvarez/" },
  { id: 3, name: github, src: github, url: "https://github.com/rocio2102" },
];
</script>

<template>
<section class="datos-personales">
    <div class="card">
      <h1>{{ title }}</h1>
      <h2>{{ descripcion }}</h2>
      <p>{{ presentacion }}</p>
      <ul class="container-lista">
        <li v-for="red in redesSociales" :key="red.id">
          <a :href="red.url" target="_blank" class="social-link">
            <img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name">
          </a>

        </li>
      </ul>
      <h4>{{ residencia }}</h4>
    </div>
  </section>
</template>

<style scoped>
h1 {
  font-size: 2.5rem;
  color: white;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

p {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: white;
}

.card {
  background-color:#523F55;
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  text-align: center;
}

.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center;
}

.icon-redsocial {
  align-items: center;
  background-color: aliceblue;
  border-radius: 50%;
  padding: px;
  margin: 5px;
  box-shadow: 0 0 5px rgba(12, 34, 92, 0.934);
}

.icon-redsocial:hover {
  background-color: rgb(4, 8, 10);
  box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
}

h2 {
  color: rgb(252, 252, 252);
}

h4 {
  color: rgb(252, 252, 252);
}

.social-link {
  border: none;
  text-decoration: none;
  transition: 0.3s;
}
.social-link:hover {
  background-color: transparent;
  border: none;
}
</style>