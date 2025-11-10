<template>
  <div class="intereses-container">
    <div class="fondo-intereses"></div>
    <div class="links">
      <a href="https://github.com/DelfinaMulinetti" target="_blank">
        <img class="icon" src="https://ksenia-k.com/img/icons/link.svg" alt="GitHub">
      </a>
    </div>
  </div>
</template>

<style scoped>
.intereses-container {
  position: relative;
}

.fondo-intereses {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  border-radius: 12px;
  background: radial-gradient(circle at top left, rgba(255, 255, 255, 0.1), transparent);
  backdrop-filter: blur(10px);
  opacity: 0.2;
  pointer-events: none;
}

.links {
  position: fixed;
  bottom: 20px;
  right: 20px;
}

.icon {
  width: 30px;
  height: 30px;
  transition: transform 0.2s ease;
}

.icon:hover {
  transform: scale(1.1);
}

@media (max-width: 768px) {
  .fondo-intereses {
    background: radial-gradient(circle at top left, rgba(255, 255, 255, 0.15), transparent);
  }
}
</style>

