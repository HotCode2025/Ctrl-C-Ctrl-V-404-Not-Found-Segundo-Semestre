<template>
  <div id="portfolio-app">
    <NavBar />
<Technologies />
<!--     <HeroSection />

    <AboutUs />

    <TeamMembers />
    
    
    
    <Projects />
    
    <Skills />
    
    <ContactInfo /> -->
    
    <FooterSection />
  </div>
</template>

<script>

import NavBar from './components/NavBar.vue'
import Technologies from './components/Technologies.vue'
/* import HeroSection from './components/HeroSection.vue'
import AboutUs from './components/AboutUs.vue'
import TeamMembers from './components/TeamMembers.vue'

import Projects from './components/Projects.vue'
import Skills from './components/Skills.vue'
import ContactInfo from './components/ContactInfo.vue' */

import FooterSection from './components/FooterSection.vue' 
export default {
  name: 'App',
  components: {
    NavBar,
/*     HeroSection,
    AboutUs,
    TeamMembers,
    Technologies,
    Projects,
    Skills,
    ContactInfo, */
    FooterSection 
  }
}
</script>

<style scoped>
#portfolio-app {
  width: 100%;
  min-height: 100vh;
}
</style>