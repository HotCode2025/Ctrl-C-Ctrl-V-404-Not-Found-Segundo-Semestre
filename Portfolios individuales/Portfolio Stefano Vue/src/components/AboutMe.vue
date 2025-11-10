<template>
  <section id="about" class="section">
    <div class="container">
      <h2 class="section-title">Sobre Mi</h2>
      <div class="about-content">
        <div class="about-text">
          <p>
            ¡Hola! Soy Stefano Aymar, un apasionado por la tecnología y la
            programación originario de Rosario, Argentina. Actualmente me
            encuentro cursando la Tecnicatura Universitaria en Programación en
            la UTN Facultad Regional San Rafael.
          </p>
          <p>
            Desde pequeño mostré interés por la informática, lo que me llevó a
            explorar el mundo de la programación de manera autodidacta antes de
            comenzar mis estudios formales. Me considero una persona curiosa,
            proactiva y con gran capacidad para resolver problemas.
          </p>
          <p>
            Fuera del ámbito académico, disfruto de participar en comunidades de
            desarrollo, aprender nuevas tecnologías y contribuir en proyectos de
            código abierto. También me gusta el fútbol y tocar la guitarra en mi
            tiempo libre.
          </p>
        </div>
        <div class="about-image">
          <div class="image-container">
            <img
              src="/images/foto_cv2.png"
              alt="Stefano Aymar"
              class="profile-img"
            />
            <div class="image-overlay"></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// No script logic needed for static content
</script>

<style scoped>
.section {
  margin-bottom: 4rem;
  background: linear-gradient(135deg, #f8fdff 0%, #e3f2fd 100%);
  border-radius: 1.5rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
  padding: 3rem 2rem;
  position: relative;
  overflow: hidden;
}

.section::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #00796b, #004d40);
}

.container {
  max-width: 1100px;
  margin: 0 auto;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 2rem;
  text-align: center;
  position: relative;
}

.section-title::after {
  content: "";
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
  background: linear-gradient(90deg, #00796b, #004d40);
  border-radius: 2px;
}

.about-content {
  display: flex;
  flex-wrap: wrap;
  gap: 3rem;
  align-items: center;
}

.about-text {
  flex: 2;
  font-size: 1.15rem;
  color: #34495e;
  line-height: 1.7;
}

.about-text p {
  margin-bottom: 1.5rem;
  position: relative;
  padding-left: 1.5rem;
}

.about-text p::before {
  content: "▸";
  position: absolute;
  left: 0;
  color: #00796b;
  font-weight: bold;
}

.about-image {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-container {
  position: relative;
  /* quitar recuadro: sin sombra ni borde */
  border-radius: 0;
  overflow: visible;
  box-shadow: none;
  transition: none;
}

.profile-img {
  max-width: 280px;
  display: block;
  border-radius: 0; /* imagen sin recuadro redondeado */
  box-shadow: none;
}

.image-overlay {
  display: none; /* eliminar overlay */
}

@media (max-width: 768px) {
  .about-content {
    flex-direction: column-reverse;
    gap: 2rem;
  }

  .section {
    padding: 2rem 1rem;
    margin-bottom: 2rem;
  }

  .section-title {
    font-size: 2rem;
  }

  .about-text {
    font-size: 1.05rem;
  }

  .profile-img {
    max-width: 220px;
  }
}
</style>
