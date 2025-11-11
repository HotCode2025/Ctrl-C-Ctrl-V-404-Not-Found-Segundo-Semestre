<script setup>
// Asumimos que la foto está en la carpeta /public
</script>

<template>
  <section class="about-me-section">
    <div class="content-wrapper">
      <div class="text-content">
        <h1 class="main-title">Dolores Mendoza</h1>
        <h2 class="subtitle">Programadora en Formación | Segundo Semestre</h2>
        
        <p class="paragraph">
          ¡Hola! Soy Dolores, una estudiante apasionada por el desarrollo web y la programación. Actualmente me enfoco en consolidar mis habilidades en el stack Vue.js y la lógica de programación orientada a objetos (POO).
        </p>

        <p class="paragraph">
          Mi objetivo es aplicar mis conocimientos de JavaScript, HTML y CSS en proyectos reales, como el Portafolio Grupal que desarrollamos en la clase de Programación. Siempre estoy buscando aprender nuevas tecnologías y colaborar en desafíos interesantes.
        </p>
        
        <div class="contact-buttons">
          <a href="mailto:mariadoloresmendoza159@gmail.com" class="btn primary">Contáctame</a>
          <a href="/CV_Maria_Dolores_Mendoza.pdf" class="btn secondary" target="_blank">Ver mi CV</a>
        </div>
        
      </div>

      <div class="profile-image">
        <img src="/myphoto.jpg" alt="Foto de perfil de Dolores Mendoza" />
      </div>

    </div>
  </section>
</template>

<style scoped>
.about-me-section {
    padding: 4rem 2rem;
    background-color: #ffffff;
    color: #8f70d0;
}
.content-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    gap: 40px;
}
.text-content {
    max-width: 600px;
}
.main-title {
    font-size: 3.5rem;
    margin-bottom: 0.5rem;
    color: #521dbc;
}
.subtitle {
    font-size: 1.5rem;
    color: #1a0d45;
    margin-bottom: 1.5rem;
}
.paragraph {
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 1rem;
}
.profile-image img {
    width: 300px;
    height: 300px;
    border-radius: 50%; /* Para hacerla circular */
    object-fit: cover;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}
.contact-buttons {
    margin-top: 2rem;
}
.btn {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    font-weight: bold;
    margin-right: 15px;
    transition: background-color 0.3s;
}
.btn.primary {
    background-color: #8650dc;
    color: white;
}
.btn.primary:hover {
    background-color: #714ad4;
}
.btn.secondary {
    background-color: #ecf0f1;
    color: #481480;
    border: 1px solid #7f8c8d;
}
.btn.secondary:hover {
    background-color: #dcdde1;
}
</style>