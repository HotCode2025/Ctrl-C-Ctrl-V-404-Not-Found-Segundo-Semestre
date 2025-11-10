<script setup>
import icono1 from "/src/assets/ProfTec.svg";

import {ref} from "vue";


const experiencias = ref([
    {
        id:1, 
        src: icono1, 
        titulo: "Near Tech SRL", 
        fecha: "Enero 2019 - actualidad", 
        parrafo: "Dentro de la empresa me desempeño en la implementación de sistemas ERP, brindando capacitación a usuarios finales y soporte técnico para la resolución de incidentes funcionales. También realizo consultas y mantenimientos en bases de datos SQL, trabajando en conjunto con áreas contables, comerciales y técnicas para asegurar una integración eficiente del sistema en cada empresa "
    },
   
]);
</script>

<template>
    <div class="card">
        <ul class="listado">
            <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
                <h3 class="titulo">{{ experiencia.titulo }}</h3> 
                <p class="fecha">{{ experiencia.fecha }}</p>
                
                <p>{{ experiencia.parrafo }}</p>
            </li> 
        </ul>
    </div>
</template>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    padding: 1rem;
    background-color: #523F55;
    border-radius: 15px;
    color: white;
    text-align: center;
}


.titulo {
    font-size: 28px;
    color:#DEAAE6;
    text-align: center;
   
}

.fecha {
    font-size: 1rem;
    color:whitesmoke;
    margin-bottom: 1rem;
    text-align: center;
}

.listado {
    display: flex;
    flex-direction: column;
}

.item {
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
}
</style>