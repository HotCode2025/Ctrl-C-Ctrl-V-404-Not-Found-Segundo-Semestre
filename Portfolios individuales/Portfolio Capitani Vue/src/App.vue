<script setup>
import Education from './components/Education.vue'
import NavBar from './components/Navbar.vue'
import Profile from './components/Profile.vue'
import Technologies from './components/Technologies.vue'
import Projects from './components/Projects.vue'
import Contact from './components/Contact.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <!-- HTML Content with vue's tools -->
  <header>
    <!-- NavBar Component -->
    <NavBar />
  </header>

  <main>
    <!-- Profile Component -->
    <Profile />

    <!-- Education Component -->
    <Education />

    <!-- Technologies Component -->
    <Technologies />

    <!-- Projects Component -->
    <Projects />
  </main>
  <!-- Contact Component-->
  <Contact />

  <footer>
    <!-- Footer Component-->
    <Footer />
  </footer>
</template>

<style scoped></style>
