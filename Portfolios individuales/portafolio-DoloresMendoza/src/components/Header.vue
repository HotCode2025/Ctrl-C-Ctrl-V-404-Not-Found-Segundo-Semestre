<template>
  <header class="main-header">
    <div class="logo">Dolores Mendoza</div>
    <nav class="navigation">
      <a href="#proyectos">Proyectos</a>
      <a href="#habilidades">Habilidades</a>
      <a href="#contacto">Contacto</a>
    </nav>
  </header>
</template>

<style scoped>
.main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #3498db;
  color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.logo {
  font-size: 1.5rem;
  font-weight: bold;
}
.navigation a {
  color: white;
  text-decoration: none;
  margin-left: 20px;
  font-size: 1rem;
  transition: color 0.3s;
}
.navigation a:hover {
  color: #ecf0f1; /* Gris muy claro */
}
</style>