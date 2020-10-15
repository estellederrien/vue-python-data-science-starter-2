import Vue from 'vue';
import Router from 'vue-router';
import Home from './components/Home.vue';
import MinimizeCost from './components/MinimizeCost.vue';


// IF THE APP SI SLOW, TRY TO LOAD COMPONENTS ASYNC
// SI L'APP EST LENTE , CHARGER LES COMPONENTS DE FACON ASYNCHRONE.
/* const AsyncPortfolioOptimization = () =>
    import ("./components/PortfolioOptimization.vue"); */

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
            path: '/',
            name: 'Home',
            component: Home
        },
        {
            path: '/MinimizeCost',
            name: 'MinimizeCost',
            component: MinimizeCost
        }
    ],
});