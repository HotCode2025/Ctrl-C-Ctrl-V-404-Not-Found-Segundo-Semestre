<template>
  <section id="equipo" class="team-section">
    <div class="container">
      <h2 class="section-title">Nuestro Equipo</h2>
      <p class="team-subtitle">
        Conoce a los 9 integrantes que conforman este grupo de trabajo
      </p>
      
      <div class="team-grid">
        <div 
          v-for="(member, index) in teamMembers" 
          :key="index"
          class="team-card"
        >
          <div class="card-inner">
            <div class="avatar" :style="{ background: member.color }">
              <span class="avatar-initials m">{{member.initials }}</span>
            </div>
            
            <div class="member-info">
              <h3 class="member-name">{{ member.name }}</h3>
              <p class="member-role">{{ member.role }}</p>
              <p class="member-description">{{ member.description }}</p>
            </div>
            
            <div class="member-social">
              <a href="#" class="social-link" aria-label="GitHub">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
              </a>
              <a href="#" class="social-link" aria-label="LinkedIn">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                </svg>
              </a>
            </div>
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
        {
          name: 'Aymar Stéfano',
          role: 'Desarrollador Frontend',
          description: 'Especializado en diseño de interfaces y experiencia de usuario.',
          initials: 'AS',
          color: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
        },
        {
          name: 'Capitani Santiago',
          role: 'Desarrollador Full Stack y Técnico Informatico',
          description: 'Apasionado por el desarrollo web, tanto frontend como backend.',
          initials: 'CS',
          color: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)'
        },
        {
          name: 'Lucero Rocio',
          role: 'Desarrolladora Backend',
          description: 'Enfocada en bases de datos y lógica de servidor.',
          initials: 'LR',
          color: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)'
        },
        {
          name: 'Mandile Guido',
          role: 'Desarrollador Frontend',
          description: 'Apasionado por crear experiencias web interactivas.',
          initials: 'MG',
          color: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)'
        },
        {
          name: 'Martinez Trejo Gustavo',
          role: 'Desarrollador Backend',
          description: 'Especializado en APIs y servicios web.',
          initials: 'MG',
          color: 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)'
        },
        {
          name: 'Mendoza Dolores',
          role: 'Desarrolladora Full Stack',
          description: 'Versatil en múltiples tecnologías y frameworks.',
          initials: 'MD',
          color: 'linear-gradient(135deg, #30cfd0 0%, #330867 100%)'
        },
        {
          name: 'Mulinetti Delfina',
          role: 'Desarrolladora Frontend',
          description: 'Creativa en diseño y maquetación web.',
          initials: 'MD',
          color: 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)'
        },
        {
          name: 'Velasco Pablo',
          role: 'Desarrollador Backend',
          description: 'Enfocado en optimización y rendimiento.',
          initials: 'VP',
          color: 'linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)'
        },
        {
          name: 'Zanatta Hugo',
          role: 'Desarrollador Full Stack',
          description: 'Interesado en tecnologías emergentes y DevOps.',
          initials: 'ZH',
          color: 'linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)'
        }
      ]
    }
  }
}
</script>

<style scoped>
.team-section {
  padding: 5rem 0;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 1rem;
  color: var(--color-dark);
}

.team-subtitle {
  text-align: center;
  font-size: 1.1rem;
  color: var(--color-text-light);
  margin-bottom: 3rem;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.team-card {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.team-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.card-inner {
  padding: 2rem;
  text-align: center;
}

.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin: 0 auto 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.avatar-initials {
  font-size: 2rem;
  font-weight: 700;
  color: white;
}

.member-info {
  margin-bottom: 1.5rem;
}

.member-name {
  font-size: 1.4rem;
  font-weight: 600;
  color: var(--color-dark);
  margin-bottom: 0.5rem;
}

.member-role {
  font-size: 1rem;
  color: var(--color-primary);
  font-weight: 500;
  margin-bottom: 0.75rem;
}

.member-description {
  font-size: 0.95rem;
  color: var(--color-text-light);
  line-height: 1.6;
}

.member-social {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.social-link {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--color-primary);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.social-link:hover {
  background: var(--color-secondary);
  transform: scale(1.1);
}

@media (max-width: 768px) {
  .team-grid {
    grid-template-columns: 1fr;
  }
}
</style>
