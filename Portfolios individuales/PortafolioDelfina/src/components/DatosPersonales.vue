<script setup>
import linkedin from '/src/components/icons/linkedin_icon.svg';
import instagram from '/src/components/icons/instagram_icon.svg';
import github from '/src/components/icons/github_icon.svg';
import cv from '/src/components/icons/cv_resume_icon.svg';

const title = "Delfina Mulinetti";
const descripcion = "Realizadora audiovisual";
const residencia = "Villa Nueva, Córdoba, Argentina";
const presentacion = "Bienvenidos a mi portafolio elaborado para poder presentarlo en el segundo semestre de la Tecnicatura en Programación.";
const redesSociales = [
  { id: 1, name: 'LinkedIn', src: linkedin, url: "https://www.linkedin.com/in/hugo-jeús-zanatta-lopez-2030b9359" },
  { id: 2, name: 'Instagram', src: instagram, url: "https://www.instagram.com/delfimulinetti/" },
  { id: 3, name: 'GitHub', src: github, url: "https://github.com/DelfinaMulinetti" },
  { id: 4, name: 'CV', src: cv, url: "" },
];
const telefono = "+54 9 3534 593258";
</script>

<template>
  <div>
    <!-- 🔹 Banner superior -->
    <header class="banner">
      <h1>MI PORTAFOLIO</h1>
    </header>

    <!-- 🔹 Tarjeta de presentación -->
    <section class="datos-personales">
      <div class="card">
        <h1>{{ title }}</h1>
        <h2>{{ descripcion }}</h2>
        <p class="presentacion">{{ presentacion }}</p>

        <ul class="container-lista">
          <li v-for="red in redesSociales" :key="red.id">
            <a :href="red.url" target="_blank" class="social-link">
              <img class="icon-redsocial" :src="red.src" width="40" :alt="red.name" />
            </a>
          </li>
        </ul>

        <div class="info-contacto">
          <h3>{{ telefono }}</h3>
          <h4>{{ residencia }}</h4>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* 🔸 Banner principal */
.banner {
  width: 100%;
  text-align: center;
  padding: 3rem 1rem 2rem 1rem;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 4px 20px rgba(255, 255, 255, 0.1);
}

.banner h1 {
  font-size: 3rem;
  color: #ffffff;
  letter-spacing: 2px;
  font-weight: 700;
  text-shadow: 0 0 15px rgba(255, 255, 255, 0.4);
}

/* 🔸 Datos personales (tu card original) */
.datos-personales {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 4rem 1rem;
}

.card {
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(15px) saturate(180%);
  -webkit-backdrop-filter: blur(15px) saturate(180%);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.25);
  padding: 2.5rem;
  max-width: 600px;
  text-align: center;
  color: #fff;
  box-shadow: 0 0 30px rgba(0, 255, 255, 0.08);
  transition: all 0.3s ease;
}

.card:hover {
  background: rgba(255, 255, 255, 0.18);
  transform: translateY(-5px);
  box-shadow: 0 0 35px rgba(0, 255, 255, 0.15);
}

h1 {
  font-size: 2.4rem;
  margin-bottom: 0.5rem;
  font-weight: 700;
  color: #ffffff;
}

h2 {
  font-size: 1.4rem;
  color: #ffffff;
  margin-bottom: 1rem;
  font-weight: 500;
}

.presentacion {
  font-size: 1.1rem;
  font-weight: 400;
  color: #ffffff;
  margin-bottom: 1.5rem;
  line-height: 1.5;
}

.container-lista {
  display: flex;
  justify-content: center;
  gap: 1rem;
  list-style: none;
  margin: 1rem 0 2rem 0;
  padding: 0;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  width: 50px;
  height: 50px;
  transition: all 0.3s ease;
}

.social-link:hover {
  background: rgba(0, 255, 213, 0.2);
  transform: scale(1.1);
  box-shadow: 0 0 10px rgba(0, 255, 213, 0.6);
}

.icon-redsocial {
  width: 28px;
  height: 28px;
}

.info-contacto h3 {
  font-size: 1.1rem;
  margin-bottom: 0.3rem;
  color: #fff;
}

.info-contacto h4 {
  font-size: 1rem;
  color: #b5fff6;
  font-weight: 400;
}
</style>
