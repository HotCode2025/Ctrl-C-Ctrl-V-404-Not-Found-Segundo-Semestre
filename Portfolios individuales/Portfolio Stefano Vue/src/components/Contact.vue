<template>
  <section id="contact" class="section">
    <div class="container">
      <h2 class="section-title">Contacto</h2>
      <p class="contact-description">
        ¿Quieres contactarme? Puedes escribirme a través de los siguientes
        medios:
      </p>
      <div class="contact-grid">
        <ul class="contact-list">
          <li>
            <a
              class="contact-link"
              href="mailto:stefanoaymar@gmail.com"
              aria-label="Enviar correo a Stefano"
            >
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                aria-hidden="true"
              >
                <path
                  d="M3 7.5C3 6.11929 4.11929 5 5.5 5H18.5C19.8807 5 21 6.11929 21 7.5V16.5C21 17.8807 19.8807 19 18.5 19H5.5C4.11929 19 3 17.8807 3 16.5V7.5Z"
                  stroke="#00796b"
                  stroke-width="1.2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M21 7L12 13L3 7"
                  stroke="#00796b"
                  stroke-width="1.2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <span class="contact-text">stefanoaymar@gmail.com</span>
            </a>
          </li>
          <li>
            <a
              class="contact-link"
              href="https://www.linkedin.com/in/stefano-aymar/"
              target="_blank"
              rel="noopener"
              aria-label="Ver perfil de LinkedIn"
            >
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                aria-hidden="true"
              >
                <path
                  d="M16 8C17.1046 8 18 7.10457 18 6C18 4.89543 17.1046 4 16 4C14.8954 4 14 4.89543 14 6C14 7.10457 14.8954 8 16 8Z"
                  stroke="#0A66C2"
                  stroke-width="1.2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M6 9V19"
                  stroke="#0A66C2"
                  stroke-width="1.2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M10 9V19"
                  stroke="#0A66C2"
                  stroke-width="1.2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M6 12H10"
                  stroke="#0A66C2"
                  stroke-width="1.2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <span class="contact-text">LinkedIn</span>
            </a>
          </li>
          <li>
            <a
              class="contact-link"
              href="https://github.com/stefanoaymar"
              target="_blank"
              rel="noopener"
              aria-label="Ver GitHub"
            >
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                aria-hidden="true"
              >
                <path
                  d="M12 2C8.13 2 5 5.13 5 9C5 12.87 7.87 15.74 11.74 15.97C12 15.99 12.11 15.79 12.11 15.61C12.11 15.46 12.11 14.86 12.11 14.12C9.07 14.73 8.45 13.16 8.45 13.16C8 11.99 7.27 11.66 7.27 11.66C6.18 11.02 7.34 11.04 7.34 11.04C8.53 11.11 9.11 12.25 9.11 12.25C10.18 13.96 11.93 13.45 12.66 13.22C12.75 12.49 13.02 11.99 13.32 11.71C10.96 11.42 8.48 10.5 8.48 7.43C8.48 6.56 8.81 5.86 9.37 5.31C9.26 5.03 8.95 4.13 9.47 3C9.47 3 10.29 2.67 12 4C13.71 2.67 14.53 3 14.53 3C15.05 4.13 14.74 5.03 14.63 5.31C15.19 5.86 15.52 6.56 15.52 7.43C15.52 10.5 13.03 11.41 10.66 11.7C11.05 12.06 11.38 12.76 11.38 13.77C11.38 15.2 11.36 16.39 11.36 16.61C11.36 16.79 11.47 16.99 11.74 16.97C15.62 16.73 18.48 13.87 18.48 10C18.48 5.13 15.37 2 12 2Z"
                  stroke="#333"
                  stroke-width="0.8"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <span class="contact-text">GitHub</span>
            </a>
          </li>
        </ul>
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
  margin-bottom: 1rem;
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

.contact-description {
  text-align: center;
  color: #34495e;
  font-size: 1.1rem;
  margin-bottom: 3rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.6;
}

.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  max-width: 900px;
  margin: 0 auto;
}

.contact-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: contents; /* allow grid children to layout uniformly */
}

.contact-list li {
  display: block;
}

.contact-link {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: #fff;
  padding: 1.2rem 1.4rem;
  border-radius: 1rem;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
  text-decoration: none;
  color: inherit;
  transition: transform 0.22s ease, box-shadow 0.22s ease,
    border-color 0.22s ease;
  border: 1px solid rgba(0, 0, 0, 0.04);
}

.contact-link svg {
  flex-shrink: 0;
  width: 44px;
  height: 44px;
  padding: 8px;
  border-radius: 10px;
  background: linear-gradient(135deg, #e0f7fa, #b2ebf2);
}

.contact-text {
  font-weight: 600;
  color: var(--color-heading);
  font-size: 1rem;
}

.contact-link:hover {
  transform: translateY(-6px);
  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.12);
  border-color: rgba(0, 121, 107, 0.15);
}

@media (max-width: 768px) {
  .section {
    padding: 2rem 1rem;
    margin-bottom: 2rem;
  }

  .section-title {
    font-size: 2rem;
  }

  .contact-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .contact-link {
    padding: 1rem;
  }

  .contact-link svg {
    width: 40px;
    height: 40px;
  }
}
</style>
