<template>
  <section class="contact-section" id="contact">
    <h2>Contacto</h2>
    <p class="subtitle">¿Tienes una pregunta o quieres trabajar juntos? Déjame un mensaje.</p>
    <div class="form-card">
      <form @submit.prevent="handleSubmit">
        <div class="input-group">
          <label for="name">Nombre</label>
          <input
            type="text"
            id="name"
            placeholder="Tu nombre"
            v-model="form.name"
            required
            :disabled="isSending"
          />
        </div>
        <div class="input-group">
          <label for="email">Email</label>
          <input
            type="email"
            id="email"
            placeholder="Tu correo electrónico"
            v-model="form.email"
            required
            :disabled="isSending"
          />
        </div>
        <div class="input-group">
          <label for="message">Mensaje</label>
          <textarea
            id="message"
            placeholder="Escribe tu mensaje aquí..."
            v-model="form.message"
            required
            :disabled="isSending"
          ></textarea>
        </div>
        <button type="submit" class="btn submit-btn" :disabled="isSending">
          {{ isSending ? 'Enviando...' : 'Enviar Mensaje' }}
        </button>
      </form>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import emailjs from '@emailjs/browser' // Import EmailJS

const form = ref({
  name: '',
  email: '',
  message: '',
})

const isSending = ref(false)

const sendEmail = () => {
  isSending.value = true // Start the shipping status

  // IDs EmailJS
  const serviceID = import.meta.env.VITE_EMAILJS_SERVICE_ID
  const templateID = import.meta.env.VITE_EMAILJS_TEMPLATE_ID
  const publickKey = import.meta.env.VITE_EMAILJS_PUBLIC_KEY
  // Using environment variables to hide EmailJS IDs

  emailjs
    .send(serviceID, templateID, form.value, publickKey)
    .then((result) => {
      console.log('Success', result.text)
      alert('Mensaje enviado con exito')
      // Form Reset
      form.value = { name: '', email: '', message: '' }
    })
    .catch((error) => {
      /// Changed to .catch to handle errors
      console.log('FAILED...', error.text)
      alert('Hubo un error al enviar el mensaje. Por favor, inténtalo de nuevo.')
    })
    .finally(() => {
      isSending.value = false // Sending status ends (success or error)
    })
}

const handleSubmit = () => {
  // Avoid multiple submissions if already being sent
  if (!isSending.value) {
    sendEmail()
  }
}
</script>

<style scoped>
.contact-section {
  padding: 4rem 2rem;
  text-align: center;

  .subtitle {
    color: var(--text-secondary);
    margin-bottom: 3rem;
    max-width: 500px;
    margin-left: auto;
    margin-right: auto;
  }

  .form-card {
    max-width: 700px;
    margin: 0 auto;
    background-color: var(--white);
    padding: 2.5rem;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  }
}

.input-group {
  text-align: left;
  margin-bottom: 1.5rem;

  label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: var(--text-primary);
  }

  input,
  textarea {
    width: 100%;
    padding: 0.8rem 1rem;
    border-radius: 8px;
    border: 1px solid var(--grey);
    font-size: 1rem;
    transition:
      border-color 0.3s,
      box-shadow 0.3s;
  }
}

.submit-btn {
  background-color: transparent;
  color: var(--primary);
  font-weight: 800;
  border: 2px solid var(--primary);

  &:hover {
    background-color: var(--primary);
    color: var(--white);
  }
}
</style>
