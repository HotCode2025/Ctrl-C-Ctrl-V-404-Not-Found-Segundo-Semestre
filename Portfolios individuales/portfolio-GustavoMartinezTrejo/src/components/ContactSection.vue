<template>
  <section id="contacto" class="section fade-in">
    <h2>Contáctame</h2>
    
    <div class="contact-grid">
      <div>
        <h3>Información de Contacto</h3>
        
        <div class="contact-info">
          <div class="contact-icon">📧</div>
          <h4>Email</h4>
          <p>martinez.trejo.gustavo.a@gmail.com</p>
        </div>
        
        <div class="contact-info">
          <div class="contact-icon">📱</div>
          <h4>Teléfono</h4>
          <p>+54 9 381 604 1076</p>
        </div>
        
        <div class="contact-info">
          <div class="contact-icon">📍</div>
          <h4>Ubicación</h4>
          <p>Argentina</p>
        </div>
      </div>
      
      <div>
        <h3>Envíame un Mensaje</h3>
        
        <form
          class="contact-form"
          action="https://formsubmit.co/martinez.trejo.gustavo.a@gmail.com"
          method="POST"
        >
          <input type="hidden" name="_captcha" value="false" />
          
          <div class="form-group">
            <label for="nombre">Nombre</label>
            <input type="text" id="nombre" name="name" required />
          </div>
          
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required />
          </div>
          
          <div class="form-group">
            <label for="asunto">Asunto</label>
            <input type="text" id="asunto" name="subject" required />
          </div>
          
          <div class="form-group">
            <label for="mensaje">Mensaje</label>
            <textarea id="mensaje" name="message" required></textarea>
          </div>
          
          <button type="submit" class="submit-btn">Enviar Mensaje</button>
        </form>
      </div>
    </div>
  </section>
</template>

<style scoped>
.section {
  background: rgba(99, 99, 99, 0.95);
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

h3 {
  color: #2c3e50;
  margin-bottom: 20px;
}

.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
}

.contact-info {
  background: rgba(255, 255, 255, 0.1);
  padding: 30px;
  border-radius: 15px;
  text-align: center;
}

.contact-icon {
  width: 60px;
  height: 60px;
  background: linear-gradient(45deg, #667eea, #764ba2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 15px;
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
}

.contact-form {
  display: grid;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  margin-bottom: 5px;
  font-weight: bold;
  color: #2c3e50;
}

.form-group input,
.form-group textarea {
  padding: 12px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #667eea;
}

.form-group textarea {
  resize: vertical;
  min-height: 120px;
}

.submit-btn {
  background: linear-gradient(45deg, #667eea, #764ba2);
  color: white;
  padding: 15px 30px;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
}

@media (max-width: 768px) {
  .section {
    padding: 20px;
  }
  
  .contact-grid {
    grid-template-columns: 1fr;
  }
}
</style>