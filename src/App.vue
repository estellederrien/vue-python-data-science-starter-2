<template>
<div id="app">
    <navbar />
    <router-view />

</div>
</template>

<script>
import navbar from './components/Navbar.vue'

export default {
    components: {
        navbar // register component
    }
}
</script>

<style>
/* """""""""""""""""""""""""""""""""""""""""""""""""""""" GENERAL MEDIAS QUERIES""""""""""""""""""""""""""""""""""""""""""""""""" */

/* Extra small devices (phones, 600px and down) */
@media only screen and (max-width: 600px) {
  
}

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (min-width: 600px) {

  
}

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {

    .b-card-perso {
        min-width: 20rem !important;
        max-width: 30% !important;
    }
    .card-img-spe {
      max-width: 100% !important;
      max-height: 110px!important;
       min-height: 110px!important;
  }
  

}

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {

    .b-card-perso {
        min-width: 15rem ;
        margin-bottom: 1em !important;
    }
    .card-img-spe {
     max-width: 100% !important;
      max-height: 160px!important;
       min-height: 160px!important;
  }
  
}

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {

    .b-card-perso {
        min-width: 15rem ;
        margin-bottom: 1em !important;
    }
    .card-img-spe { 
      max-width: 100% !important;
      max-height: 220px!important;
       min-height: 220px!important;
  }
 
}

.main-form {
    margin: 20px;
    padding: 20px;
}

.input-group-text{
    font-size: 0.8rem !important;
}

.dropdown-item {
    color: black !important;
    text-decoration: none;
    background-color: transparent !important;
}

.dropdown-item:hover {
    color: red !important;
    text-decoration: none;
    background-color: lightgrey !important;
}

.nav-tabs {
    margin-bottom: 10px;
}

.reminder{
    max-height:60vh;
    overflow:auto;
}
</style>
