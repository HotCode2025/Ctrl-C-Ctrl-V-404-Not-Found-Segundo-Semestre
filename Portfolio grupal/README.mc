# Portfolio Grupal - Tecnicatura en Programación UTN San Rafael

## 🎓 Sobre el Proyecto

Portfolio web del grupo de estudiantes de la Tecnicatura Universitaria en Programación de la UTN Facultad Regional San Rafael, Mendoza.

## 👥 Integrantes del Equipo

1. Aymar Stéfano
2. Capitani Santiago
3. Lucero Rocio
4. Mandile Guido
5. Martinez Trejo Gustavo
6. Mendoza Dolores
7. Mulinetti Delfina
8. Velasco Pablo
9. Zanatta Hugo

## 🛠️ Tecnologías Utilizadas

- **Vue.js 3** - Framework JavaScript
- **Vite** - Build tool
- HTML5, CSS3, JavaScript

## 📋 Distribución de Tareas por Integrante

### **Integrante 1: Aymar Stéfano**
**Archivo:** `src/components/NavBar.vue`
- Crear la barra de navegación superior
- Incluir logo y enlaces a las secciones
- Hacer que sea responsive (menú hamburguesa en móvil)

### **Integrante 2: Capitani Santiago**
**Archivo:** `src/components/HeroSection.vue`
- Crear la sección principal de presentación
- Incluir título del proyecto, nombre de la universidad
- Agregar una breve descripción del grupo

### **Integrante 3: Lucero Rocio**
**Archivo:** `src/components/AboutUs.vue`
- Crear sección "Sobre Nosotros"
- Describir quiénes somos como grupo
- Explicar la carrera y nuestros objetivos

### **Integrante 4: Mandile Guido**
**Archivo:** `src/components/TeamMembers.vue`
- Crear tarjetas para cada integrante del equipo
- Mostrar nombre, foto/avatar y rol de cada uno
- Hacer un grid responsive

### **Integrante 5: Martinez Trejo Gustavo**
**Archivo:** `src/components/Technologies.vue`
- Crear sección de tecnologías que aprendimos
- Mostrar Java, Python, JavaScript, MySQL, Git, GitHub
- Agregar iconos o logos de cada tecnología

### **Integrante 6: Mendoza Dolores**
**Archivo:** `src/components/Projects.vue`
- Crear sección de proyectos
- Mostrar proyectos realizados o en desarrollo
- Incluir descripción y tecnologías usadas en cada proyecto

### **Integrante 7: Mulinetti Delfina**
**Archivo:** `src/components/Skills.vue`
- Crear sección de habilidades
- Mostrar skills técnicas y blandas
- Puede incluir barras de progreso o badges

### **Integrante 8: Velasco Pablo**
**Archivo:** `src/components/ContactInfo.vue`
- Crear sección de información de contacto
- Incluir ubicación (San Rafael, Mendoza)
- Agregar enlaces a redes sociales del grupo o universidad

### **Integrante 9: Zanatta Hugo**
**Archivo:** `src/components/FooterSection.vue`
- Crear el footer del sitio
- Incluir copyright, links importantes
- Información adicional de la UTN

## 📦 Archivos del Proyecto

Este proyecto incluye los siguientes archivos que deben copiarse en las ubicaciones correctas:

### Archivos Raíz
- `package.json` - Dependencias del proyecto
- `vite.config.js` - Configuración de Vite
- `index.html` - Archivo HTML principal
- `.gitignore` - Archivos a ignorar por Git
- `README.md` - Este archivo
- `GUIA_INSTALACION.md` - Guía detallada de instalación
- `ASIGNACIONES_INDIVIDUALES.md` - Tareas específicas por integrante

### Carpeta src/
- `main.js` - Punto de entrada de la aplicación
- `App.vue` - Componente principal que integra todos los demás

### Carpeta src/components/ (9 componentes, uno para cada integrante)
1. `NavBar.vue` - Barra de navegación (Aymar Stéfano)
2. `HeroSection.vue` - Sección principal (Capitani Santiago)
3. `AboutUs.vue` - Sobre nosotros (Lucero Rocio)
4. `TeamMembers.vue` - Tarjetas del equipo (Mandile Guido)
5. `Technologies.vue` - Tecnologías (Martinez Trejo Gustavo)
6. `Projects.vue` - Proyectos (Mendoza Dolores)
7. `Skills.vue` - Habilidades (Mulinetti Delfina)
8. `ContactInfo.vue` - Información de contacto (Velasco Pablo)
9. `FooterSection.vue` - Pie de página (Zanatta Hugo)

### Carpeta src/assets/styles/
- `main.css` - Estilos globales

## 🚀 Instrucciones de Instalación y Configuración

### Requisitos Previos
- Node.js (versión 16 o superior) - Descargar de https://nodejs.org/
- npm (se instala con Node.js)
- Git - Descargar de https://git-scm.com/
- Editor de código (recomendado: VS Code)

### Paso 1: Configuración Inicial (Responsable: Coordinador del grupo)

```bash
# Crear el proyecto Vue con Vite
npm create vite@latest portfolio-utn-grupo -- --template vue

# Entrar al directorio
cd portfolio-utn-grupo

# Instalar dependencias
npm install

# Crear estructura de carpetas
mkdir src/components
mkdir src/assets
```

### Paso 2: Subir el Boilerplate a GitHub (Responsable: Coordinador)

```bash
# Inicializar git
git init

# Agregar archivos
git add .

# Hacer commit
git commit -m "Initial commit - Boilerplate del proyecto"

# Crear repositorio en GitHub y conectar
git remote add origin https://github.com/USUARIO/portfolio-utn-grupo.git

# Subir a GitHub
git push -u origin main
```

### Paso 3: Cada Integrante Trabaja en su Componente

**Proceso para cada integrante:**

1. **Clonar el repositorio:**
```bash
git clone https://github.com/USUARIO/portfolio-utn-grupo.git
cd portfolio-utn-grupo
npm install
```

2. **Crear una rama con tu nombre:**
```bash
git checkout -b feature/tu-nombre
```

3. **Tomar tu archivo del Drive y colocarlo en `src/components/`**

4. **Probar que funcione:**
```bash
npm run dev
```

5. **Hacer commit y push:**
```bash
git add .
git commit -m "Agregado componente NombreDelComponente"
git push origin feature/tu-nombre
```

6. **Crear Pull Request en GitHub y esperar aprobación**

### Paso 4: Integración Final

El coordinador del grupo irá haciendo merge de cada Pull Request y resolviendo conflictos si los hay.

## 📁 Estructura del Proyecto

```
portfolio-utn-grupo/
├── public/
├── src/
│   ├── assets/
│   │   └── styles/
│   │       └── main.css
│   ├── components/
│   │   ├── NavBar.vue          (Aymar)
│   │   ├── HeroSection.vue     (Capitani)
│   │   ├── AboutUs.vue         (Lucero)
│   │   ├── TeamMembers.vue     (Mandile)
│   │   ├── Technologies.vue    (Martinez Trejo)
│   │   ├── Projects.vue        (Mendoza)
│   │   ├── Skills.vue          (Mulinetti)
│   │   ├── ContactInfo.vue     (Velasco)
│   │   └── FooterSection.vue   (Zanatta)
│   ├── App.vue
│   └── main.js
├── index.html
├── package.json
├── vite.config.js
└── README.md
```

## 🎨 Guía de Estilo

- **Colores principales:** 
  - Primario: #6366f1 (Indigo)
  - Secundario: #8b5cf6 (Púrpura)
  - Acento: #ec4899 (Rosa)
  
- **Fuente:** Sistema (sans-serif)

- **Espaciado:** Usar múltiplos de 4px (8px, 16px, 24px, 32px, etc.)

## 💡 Consejos para el Trabajo en Equipo

1. **Comunicación:** Usen un grupo de WhatsApp/Discord para coordinar
2. **Convenciones:** Mantengan el mismo estilo de código
3. **Comentarios:** Comenten su código para que otros lo entiendan
4. **Pruebas:** Siempre prueben que su componente funcione antes de hacer push
5. **Ayuda mutua:** Si alguien tiene problemas, ayúdense entre todos

## 🐛 Solución de Problemas Comunes

### Conflictos de Merge
Si hay conflictos, coordinen con el equipo para resolverlos juntos.

### Componente no se muestra
Verifiquen que hayan importado correctamente el componente en `App.vue`.

### Errores de npm
Prueben eliminando `node_modules` y `package-lock.json`, luego ejecuten `npm install` nuevamente.

## 📞 Contacto

**Universidad:** UTN Facultad Regional San Rafael  
**Ubicación:** San Rafael, Mendoza, Argentina  
**Carrera:** Tecnicatura Universitaria en Programación

---

**¡Éxitos en el proyecto! 🚀**