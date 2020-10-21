import "bootstrap/dist/css/bootstrap.css";
import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue";
import Vue from "vue";
import Vuex from "vuex";
import App from "./App.vue";
import router from "./router";
import Vuelidate from "vuelidate";
import Notifications from "vue-notification";
import VueTranslate from "vue-translate-plugin";
Vue.use(Vuelidate);
Vue.use(VueTranslate);
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(Notifications);
Vue.config.productionTip = false;
import Translations from './translations.js'
Vue.locales(Translations.get())


// ---------------------------VUEX DATA STORE - SHARING DATA BETWEEN COMPONENTS ! - VUEX MAGASIN DE DATA - PARTAGER DES DATAS ENTRE LES COMPONENTS -----------------------------------------------
/* INFORMATION : HOW TO USE IN COMPONENTS - COMMENT UTILISER CA DANS LES COMPONENTS  : 
SET USER ( WHEN YOU LOG IN): this.$store.commit('setUser', response.data)
GET USER : this.User = this.$store.getters.user
DELETE USER (WHEN YOU LOG OUT ): this.$store.commit('deleteUser') 
*/
Vue.use(Vuex);
const store = new Vuex.Store({
    state: {
        user: JSON.parse(localStorage.getItem("user") || "{}"),
        logged: false
    },
    mutations: {
        setUser(state, user) {
            localStorage.setItem("user", JSON.stringify(user));
            state.logged = true;
        },
        deleteUser(state) {
            console.log("USER DELETED");
            localStorage.removeItem("user");
            state.logged = false;
        }
    },
    getters: {
        user: state => {
            return state.user;
        }
    }
});
// ---------------------------------------------- END VUEX DATA STORE - SHARING DATA BETWEEN COMPONENTS !-------------------------------------



// ---------------------------------------------- END VUEX DATA STORE - SHARING DATA BETWEEN COMPONENTS !-------------------------------------
new Vue({
    router,
    render: h => h(App),
    store: store
}).$mount("#app");