<template>
  <section id="estudios" class="section fade-in">
    <h2>Mis Estudios</h2>

    <div
      v-for="(edu, index) in education"
      :key="index"
      class="education-item"
    >
      <div class="university-logo">{{ edu.logo }}</div>
      <div class="date">{{ edu.date }}</div>
      <div class="institution-name">{{ edu.institution }}</div>
      <p>{{ edu.description }}</p>
    </div>
  </section>
</template>

<script setup>
const education = [
  {
    logo: 'UTN',
    date: '2025',
    institution: 'Tecnicatura Universitaria en Programación',
    description: 'Formación académica enfocada en desarrollo de software, algoritmos, estructuras de datos y paradigmas de programación.'
  },
  {
    logo: 'UNT',
    date: '2015',
    institution: 'Ingeniería Eléctrica y Electrónica',
    description: 'Estudios en ingeniería con enfoque técnico y base matemática aplicada a circuitos, sistemas digitales y redes eléctricas.'
  },
  {
    logo: 'Henry',
    date: '2020',
    institution: 'Programación Full Stack JS',
    description: 'Formación intensiva en JavaScript moderno, React, Node, Express, SQL, metodologías ágiles y despliegue de apps full stack.'
  },
  {
    logo: 'Cisco',
    date: '2019',
    institution: 'CCNA - Cisco Networking Academy',
    description: 'Conocimientos sobre redes, direccionamiento IP, protocolos de enrutamiento, seguridad y configuración de dispositivos Cisco.'
  },
  {
    logo: 'D H',
    date: '2019',
    institution: 'Programación Web Full Stack PHP - Digital House',
    description: 'Desarrollo full stack en PHP, MVC, MySQL y tecnologías web complementarias como HTML, CSS y JavaScript.'
  }
]
</script>

<style scoped>
.section {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 40px;
  margin-bottom: 30px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.section:hover {
  transform: translateY(-5px);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
}

h2 {
  color: #2c3e50;
  font-size: 2rem;
  margin-bottom: 30px;
  padding-bottom: 15px;
  border-bottom: 3px solid #667eea;
  position: relative;
}

h2::after {
  content: '';
  position: absolute;
  bottom: -3px;
  left: 0;
  width: 50px;
  height: 3px;
  background: #764ba2;
}

.education-item {
  margin-bottom: 30px;
  padding: 25px;
  background: rgba(99, 99, 99, 0.95);
  border-radius: 15px;
  border-left: 5px solid #667eea;
  transition: all 0.3s ease;
}

.education-item:hover {
  background: rgba(102, 126, 234, 0.1);
  transform: translateX(10px);
}

.university-logo {
  width: 80px;
  height: 80px;
  float: right;
  margin-left: 20px;
  border-radius: 10px;
  background: #667eea;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
}

.institution-name {
  font-size: 1.3rem;
  font-weight: bold;
  color: #2c3e50;
  margin-bottom: 5px;
}

.date {
  color: #7f8c8d;
  font-style: italic;
  margin-bottom: 10px;
}

@media (max-width: 768px) {
  .section {
    padding: 20px;
  }
  
  .university-logo {
    float: none;
    margin: 0 auto 15px;
  }
}
</style>