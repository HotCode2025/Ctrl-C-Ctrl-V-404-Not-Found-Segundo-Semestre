<template>
  <div class="fondo-intereses"></div>
  <div class="links">
        <a href="https://github.com/rocio2102"
            target="_blank"><img class="icon" src="https://ksenia-k.com/img/icons/link.svg"></a>
    </div>
</template>

<style scoped>
.fondo-intereses {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  border-radius: 12px;
  background: radial-gradient(
    circle at top left,
    #5a189a 0%,    
    #3caea3 50%,   
    #f0a500 100%   
  );
  opacity: 0.2; 
  pointer-events: none; 
}

body {
  background-color: #0d1117; 

}

.links {
    position: fixed;
    bottom: 20px;
    right: 20px;
    font-size: 18px;
    font-family: sans-serif;
}

@media (max-width: 768px) {
  .fondo-intereses {
    background: radial-gradient(
      circle at top left,
      #5a189a 0%,
      #3caea3 55%,
      #f0a500 100%
    );
  }
}
</style>
