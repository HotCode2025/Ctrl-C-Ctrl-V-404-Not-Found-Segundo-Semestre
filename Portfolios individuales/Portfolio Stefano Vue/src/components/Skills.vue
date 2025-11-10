<template>
  <section id="skills" class="section">
    <div class="container">
      <h2 class="section-title">Conocimientos</h2>
      <div class="skills-grid">
        <div class="skill-category">
          <h3>Frontend</h3>
          <div class="skill-items">
            <div class="skill-item">
              <span class="skill-name">HTML5</span>
              <div class="skill-bar">
                <div class="skill-progress" style="width: 95%"></div>
              </div>
            </div>
            <div class="skill-item">
              <span class="skill-name">CSS3</span>
              <div class="skill-bar">
                <div class="skill-progress" style="width: 90%"></div>
              </div>
            </div>
            <div class="skill-item">
              <span class="skill-name">JavaScript</span>
              <div class="skill-bar">
                <div class="skill-progress" style="width: 85%"></div>
              </div>
            </div>
            <div class="skill-item">
              <span class="skill-name">Vue.js</span>
              <div class="skill-bar">
                <div class="skill-progress" style="width: 80%"></div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="skill-category">
          <h3>Backend & Tools</h3>
          <div class="skill-items">
            <div class="skill-item">
              <span class="skill-name">Git</span>
              <div class="skill-bar">
                <div class="skill-progress" style="width: 85%"></div>
              </div>
            </div>
            <div class="skill-item">
              <span class="skill-name">MySQL</span>
              <div class="skill-bar">
                <div class="skill-progress" style="width: 70%"></div>
              </div>
            </div>
            <div class="skill-item">
              <span class="skill-name">Scrum</span>
              <div class="skill-bar">
                <div class="skill-progress" style="width: 80%"></div>
              </div>
            </div>
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
  content: '';
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
  margin-bottom: 3rem;
  text-align: center;
  position: relative;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
  background: linear-gradient(90deg, #00796b, #004d40);
  border-radius: 2px;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 3rem;
  max-width: 900px;
  margin: 0 auto;
}

.skill-category {
  background: white;
  border-radius: 1.2rem;
  padding: 2rem;
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08);
  border-top: 4px solid #00796b;
  transition: transform 0.3s ease;
}

.skill-category:hover {
  transform: translateY(-5px);
}

.skill-category h3 {
  font-size: 1.4rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  text-align: center;
  position: relative;
}

.skill-category h3::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 3px;
  background: #00796b;
  border-radius: 2px;
}

.skill-items {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.skill-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.skill-name {
  font-weight: 500;
  color: #34495e;
  font-size: 1rem;
}

.skill-bar {
  height: 8px;
  background: #e0f2f1;
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}

.skill-progress {
  height: 100%;
  background: linear-gradient(90deg, #00796b, #004d40);
  border-radius: 4px;
  position: relative;
  transition: width 1.5s ease-in-out;
}

.skill-progress::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.4), 
    transparent);
  animation: shimmer 2s infinite;
}

@keyframes shimmer {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(100%);
  }
}

@media (max-width: 768px) {
  .section {
    padding: 2rem 1rem;
    margin-bottom: 2rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .skills-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .skill-category {
    padding: 1.5rem;
  }
}
</style>