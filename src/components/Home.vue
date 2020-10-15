<template>
<div class="main-form">
    <div class="row">
        <fieldset class="col-md-12">
            <legend> Introduction</legend>
            {{ t('INTRO') }}
            <br>
            <img class="img-thumbnail special-intro float-right " src="..\assets\logo_def.jpg"></img>
        </fieldset>
    </div>
</div </div>
</template>
<script>
// Importing libs
import axios from 'axios';
export default {
    data() {
        return {}
    },
    components: {
    },
    computed: {
    },
    methods: {
    },
    mounted() {
      
    }
}
</script>
<style>
fieldset {
    background-color: #fef5e4 !important;
    border-radius: 4px;
}
.special-intro {
    max-width: 300px
}
</style>
