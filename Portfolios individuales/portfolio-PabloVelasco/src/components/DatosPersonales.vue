<script setup>
import linkedin from '/src/assets/linkedin_icon.svg'
import github from '/src/assets/github_icon.svg'
import cv from '/src/assets/cv_resume_icon.svg'
import profileImg from '../assets/img/profile/profile-photo.png'
import location from '../components/icons/location.svg'

const title = 'Pablo Ramiro Velasco'
const descripcion = 'Técnico Universitario en Programación - UTN'
const residencia = 'Mendoza, Argentina'
const presentacion =
  'Construyo aplicaciones webs responsivas que se adapten a las necesidades del cliente y exigencia del mercado. Autodidacta con un mindset enfocado en el crecimiento personal-grupal-empresarial. Lideré equipos de desarrollo y proyectos usando metodologías ágiles.'
const redesSociales = [
  { id: 1, name: 'linkedin', src: linkedin, url: 'https://www.linkedin.com/in/pablo-r-velasco/' },
  { id: 3, name: 'github', src: github, url: 'https://github.com/Pablo-r-stack' },
  { id: 4, name: 'curriculum', src: cv, url: 'https://drive.usercontent.google.com/uc?id=1PExmlWGaoRN8RU4L2pam1ncfnXaHLt3R&export=download' },
]
</script>

<template>
  <section class="datos-personales bg-gradient-animated">
    <div class="card">
      <div class="card-body">
          <h1>{{ title }}</h1>
          <h2>{{ descripcion }}</h2>
        <p>{{ presentacion }}</p>
      </div>
      <div class="card-social">
        <img id="devPhoto" :src="profileImg" alt="pablo-foto" />
        <span class="location">
          <img :src="location" width="30rem" alt="location" />
          {{ residencia }}
        </span>
        <ul class="container-lista">
          <li v-for="red in redesSociales" :key="red.id">
            <a :href="red.url"
              ><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"
            /></a>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<style scoped>
h1 {
  font-size: 2.5rem;
}

p {
  font-size: 1rem;
  text-align: justify;
  font-weight: 600;
  margin-bottom: 1rem;
}

.card {
  display: flex;
  justify-content: space-between;
  gap: 6rem;
  background-color: rgb(28, 41, 52);
  border-radius: 10px;
  padding: 10px 50px;
  margin: 10px;
}

.card-header {
  place-items: start;
}

.card-body {
  display: flex;
  text-align: justify;
  flex-direction: column;
  align-items: start;
  flex: 1;
}

.card-social {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  align-items: center;
  margin-left: auto;
}

#devPhoto {
  width: 200px;
  height: 200px;
  border-radius: 50%;
}

.location {
  display: flex;
  gap: 0.5rem;
  align-items: center;
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
  padding: 2px;
  margin: 5px;
}

.icon-redsocial:hover {
  transform: scale(1.1);
  transition: all 0.3s ease-in-out;
}

h2 {
  font-size: 1.2rem;
  font-weight: 600;
}

/* Overrides SOLO para MODO CLARO: mantener modo oscuro intacto */
@media (prefers-color-scheme: light) {
  .datos-personales .card {
    background-color: #f9f9f9;
    border: 2px solid #ddd;
  }

  .datos-personales h1,
  .datos-personales h2,
  .datos-personales p,
  .datos-personales .location {
    color: #333;
  }

  .datos-personales .icon-redsocial {
    background-color: #eef5ff;
  }
}

@media (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }

  p {
    font-size: 0.9rem;
  }

  .card {
    flex-direction: column;
    gap: 1.5rem;
  }

  .card-social {
    margin-left: 0;
  }
}
</style>
