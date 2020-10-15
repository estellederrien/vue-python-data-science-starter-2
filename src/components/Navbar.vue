<template>
<div>
    <b-navbar toggleable="lg" class="bg">
        <b-navbar-brand href="#">
            <img src="../assets/screenshot.png" class="main_img" />

        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <b-nav-item>
                    <router-link class-active="active" to="/">
                        <b-icon icon="house-door" variant="success"></b-icon> {{ t('HOME') }}
                    </router-link>
                </b-nav-item>
                <b-nav-item-dropdown text="" right style="min-width: 20rem !important;">
                  <template slot="button-content"><b>{{ t('DROPDOWN_TITLE_1') }} </b></template>
                  <h5 class="dropdown-header"><b-icon icon="building" variant="success"></b-icon>  {{ t('FACTORIES_COMMON_CASES') }}</h5> 
           
                    <router-link class-active="active" to="/minimizeCost">
                        <b-icon icon="arrow-down" variant="success"></b-icon>
                        Minimize my 1kg food cost
                    </router-link><br />
                    
                     <div class="dropdown-divider"></div>
                     

                </b-nav-item-dropdown>
                <b-nav-item>
                     {{ t('VERSION') }} {{v}}
                </b-nav-item>

                <!-- <b-nav-item href="/industrial">Industrial optimisation</b-nav-item> -->
                <!-- <b-nav-item href="#" disabled>Disabled</b-nav-item> -->
            </b-navbar-nav>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
                <b-nav-form>
                    <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                    <b-button size="sm" class="my-2 my-sm-0" type="submit" disabled> {{ t('SEARCH') }}</b-button>
                </b-nav-form>

                <b-nav-item-dropdown text="" right>
                   <template slot="button-content"><b>{{ t('LANG') }} </b></template>
                    <b-dropdown-item @click="change_app_language('FRENCH')">FRENCH</b-dropdown-item>
                    <b-dropdown-item @click="change_app_language('ENGLISH')">ENGLISH</b-dropdown-item>
                    <b-dropdown-item @click="change_app_language('SPANISH')">ESPAGNOL</b-dropdown-item> 
                    <b-dropdown-item @click="change_app_language('DEUTSH')">DEUTSH</b-dropdown-item> 
                    <b-dropdown-item @click="change_app_language('CHINESE')">CHINESE</b-dropdown-item>
                    <b-dropdown-item @click="change_app_language('HINDI')">HINDI</b-dropdown-item>
                </b-nav-item-dropdown>

            <!--     <b-nav-item>
                    <router-link class-active="active" to="/register">
                        {{ t('REGISTER') }} 
                    </router-link>
                </b-nav-item>
                <b-nav-item>
                    <router-link class-active="active" to="/login">
                         {{ t('LOGIN') }} 
                    </router-link>
                </b-nav-item> -->

                <b-nav-item-dropdown right>
                    <!-- Using 'button-content' slot -->
                    <template v-slot:button-content>
                        <em> {{ t('USER') }} </em>
                    </template>
                    <b-dropdown-item href="#"> {{ t('PROFILE') }} </b-dropdown-item>
                    <b-dropdown-item href="#"> {{ t('SIGNOUT') }} </b-dropdown-item>
                </b-nav-item-dropdown>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</div>
</template>

<script>
// dev.env.js

export default {
    data() {
        return {
            v: ""
        };
    },
    components: {},
    computed: {},
    methods: {
        change_app_language(lang) {
            this.$translate.setLang(lang);
        }
    },
    created() {
        // APPLICATION_VERSION is coming from the vue.config.js file and is set in package.json
        this.v = APPLICATION_VERSION
        // Define what language you want to use.
        // This can be called in something like a header with a language selector menu
        // Or any other case, doesn't need to be called in all components, but
        // at least in one, so it sets the global language of the plugin
        this.$translate.setLang('ENGLISH');
    }
};
</script>

<style scoped>
.dropdown-menu a {
    padding: 5px;
}

.nav-item {
    color: black !important;
}

a {
    color: black !important;
}

.bg {
    background-color: #fef5e4 !important;
}
</style>
