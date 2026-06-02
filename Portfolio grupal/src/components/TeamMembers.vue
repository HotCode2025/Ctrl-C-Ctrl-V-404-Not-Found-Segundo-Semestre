<template>
  <section id="equipo" class="team">
    <div class="container">
      <p class="section-subtitle">Las personas detrás del código</p>
      <h2 class="section-title">Nuestro Equipo</h2>
      <div class="section-divider"></div>

      <div class="team-grid">
        <div
          v-for="(member, index) in teamMembers"
          :key="index"
          class="team-card"
        >
          <div class="avatar">
            <span>{{ member.initials }}</span>
          </div>
          <div class="member-info">
            <h3 class="member-name">{{ member.name }}</h3>
            <p class="member-role">{{ member.role }}</p>
            <p class="member-desc">{{ member.description }}</p>
          </div>
          <div class="member-social">
            <a href="#" class="social-link" aria-label="GitHub">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
              </svg>
            </a>
            <a href="#" class="social-link" aria-label="LinkedIn">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'TeamMembers',
  data() {
    return {
      teamMembers: [
        { name: 'Aymar Stéfano',         role: 'Desarrollador Frontend',          description: 'Especializado en diseño de interfaces y experiencia de usuario.',      initials: 'AS' },
        { name: 'Capitani Santiago',      role: 'Full Stack & Técnico Informático', description: 'Apasionado por el desarrollo web, tanto frontend como backend.',         initials: 'CS' },
        { name: 'Lucero Rocio',           role: 'Desarrolladora Backend',           description: 'Enfocada en bases de datos y lógica de servidor.',                       initials: 'LR' },
        { name: 'Gabriel Jauregui',       role: 'Desarrollador Frontend',          description: 'Apasionado por crear experiencias web interactivas.',                    initials: 'GJ' },
        { name: 'Martinez Trejo Gustavo', role: 'Desarrollador Backend',            description: 'Especializado en APIs y servicios web.',                                 initials: 'MG' },
        { name: 'Mendoza Dolores',        role: 'Desarrolladora Full Stack',        description: 'Versátil en múltiples tecnologías y frameworks.',                        initials: 'MD' },
        { name: 'Mulinetti Delfina',      role: 'Desarrolladora Frontend',          description: 'Creativa en diseño y maquetación web.',                                  initials: 'MD' },
        { name: 'Andrea Vargas',          role: 'Desarrolladora Backend',           description: 'Enfocada en optimización y rendimiento del servidor.',                   initials: 'AV' },
        { name: 'Zanatta Hugo',           role: 'Desarrollador Full Stack',         description: 'Interesado en tecnologías emergentes y DevOps.',                         initials: 'ZH' }
      ]
    }
  }
}
</script>

<style scoped>
.team {
  padding: 7rem 0;
  background: var(--cream);
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  overflow: hidden;
}

.team-card {
  background: var(--white);
  padding: 2.25rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  transition: background 0.25s;
}

.team-card:hover {
  background: var(--cream);
}

.avatar {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--navy);
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(201,169,110,0.3);
}

.avatar span {
  font-family: 'Playfair Display', serif;
  font-size: 1rem;
  font-weight: 600;
  color: var(--gold);
  letter-spacing: 0.05em;
}

.member-info {
  flex: 1;
}

.member-name {
  font-family: 'Playfair Display', serif;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--navy);
  margin-bottom: 0.25rem;
}

.member-role {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--gold);
  margin-bottom: 0.75rem;
  font-weight: 500;
}

.member-desc {
  font-size: 0.88rem;
  color: var(--text-mid);
  line-height: 1.7;
}

.member-social {
  display: flex;
  gap: 0.75rem;
}

.social-link {
  width: 32px;
  height: 32px;
  border: 1px solid var(--border);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-mid);
  transition: all 0.25s;
}

.social-link:hover {
  border-color: var(--gold);
  color: var(--gold);
}

@media (max-width: 640px) {
  .team-grid { grid-template-columns: 1fr; }
}
</style>
