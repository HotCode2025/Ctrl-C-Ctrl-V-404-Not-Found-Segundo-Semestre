<template>
  <section class="skills-section" id="habilidades">
    <h2 class="section-title">Habilidades Técnicas</h2>

    <div class="skills-container">
      
      <div class="skill-group">
        <h3 class="group-title">Desarrollo Frontend</h3>
        <ul class="skill-list">
          <li class="skill-item">HTML5 y CSS3 (Dominio de Flexbox)</li>
          <li class="skill-item">JavaScript Básico (ES6+)</li>
          <li class="skill-item">Vue.js (Creación y gestión de Componentes)</li>
          <li class="skill-item">Maquetación Responsive</li>
        </ul>
      </div>

      <div class="skill-group">
        <h3 class="group-title">Lenguajes y Lógica</h3>
        <ul class="skill-list">
          <li class="skill-item">Java (Programación Orientada a Objetos - POO)</li>
          <li class="skill-item">Python (Control de flujo y estructuras básicas)</li>
          <li class="skill-item">Lógica de Algoritmos</li>
        </ul>
      </div>

      <div class="skill-group">
        <h3 class="group-title">Herramientas</h3>
        <ul class="skill-list">
          <li class="skill-item">Git y GitHub (Clonación, Commits, Push)</li>
          <li class="skill-item">Visual Studio Code (VS Code)</li>
          <li class="skill-item">Terminal (Git Bash)</li>
        </ul>
      </div>

    </div>
  </section>
</template>

<style scoped>
.skills-section {
    padding: 3rem 2rem;
    background-color: #f4f4f9;
    text-align: center;
}
.section-title {
    font-size: 2.5rem;
    color: #281756;
    margin-bottom: 2.5rem;
}
.skills-container {
    display: flex;
    justify-content: center;
    gap: 30px;
    flex-wrap: wrap;
    max-width: 1000px;
    margin: 0 auto;
}
.skill-group {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    width: 280px;
    text-align: left;
}
.group-title {
    font-size: 1.5rem;
    color: #975be7;
    border-bottom: 2px solid #ecf0f1;
    padding-bottom: 10px;
    margin-bottom: 15px;
}
.skill-list {
    list-style: none;
    padding: 0;
    margin: 0;
}
.skill-item {
    padding: 8px 0;
    color: #512a94;
    font-size: 1rem;
    border-bottom: 1px dotted #e0e0e0;
}
.skill-item:last-child {
    border-bottom: none;
}
</style>