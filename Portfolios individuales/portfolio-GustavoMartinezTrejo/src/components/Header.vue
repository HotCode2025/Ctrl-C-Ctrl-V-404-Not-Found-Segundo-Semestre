<template>
  <header id="inicio" class="fade-in">
    <img
      src="https://res.cloudinary.com/dgy5dhomw/image/upload/v1762301503/1592658693347_shqvlz.jpg"
      alt="Gustavo Martinez"
      class="profile-img"
    />
    
    <h1>Gustavo Alfredo Martinez Trejo</h1>
    
    <p class="subtitle">Desarrollador Full Stack | Programador</p>
    
    <div class="social-links">
      <a
        href="https://www.linkedin.com/in/martinez-trejo-gustavo/"
        class="social-link"
        target="_blank"
        rel="noopener noreferrer"
        title="LinkedIn"
      >
        in
      </a>
      <a
        href="https://github.com/GustavoMartinezFS"
        class="social-link"
        target="_blank"
        rel="noopener noreferrer"
        title="GitHub"
      >
        git
      </a>
      <a
        href="mailto:martinez.trejo.gustavo.a@gmail.com"
        class="social-link"
        title="Email"
      >
        @
      </a>
    </div>
  </header>
</template>

<style scoped>
header {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 60px 40px 40px;
  text-align: center;
  margin-bottom: 30px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}

.profile-img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin: 0 auto 20px;
  display: block;
  border: 5px solid #667eea;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

h1 {
  color: #2c3e50;
  font-size: 2.5rem;
  margin-bottom: 10px;
  background: linear-gradient(45deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.subtitle {
  color: #7f8c8d;
  font-size: 1.2rem;
  margin-bottom: 20px;
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin: 30px 0;
}

.social-link {
  width: 50px;
  height: 50px;
  background: linear-gradient(45deg, #667eea, #764ba2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-decoration: none;
  font-weight: bold;
  transition: all 0.3s ease;
}

.social-link:hover {
  transform: translateY(-5px) scale(1.1);
  box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
}

@media (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }
}
</style>