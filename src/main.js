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




// -----------------------------------------------TRANSLATIONS -----------------------------------------------
Vue.locales({
    FRENCH: {

        // NAVBAR COMPONENT TRANSLATIONS AND // HOME COMPONENT TRANSLATIONS
        FACTORIES_COMMON_CASES: "Cas habituels en usine",
        FOOD_COMMON_CASES: "Cas habituels en nourriture",
        PORTFOLIOS_COMMON_CASES: "Cas habituels en portefeuille",

        INTRO: `Bienvenue dans le starter vue.js + Python pulp solveur linéaire,
        Choisissez un cas de programmation linéaire dans le menu. 
        L'application est en cours de création.
        Les solveurs linéaires permettent de résoudre les problèmes contenant beaucoup de variables.`,
        HOME: "Accueil",
        DROPDOWN_TITLE_1: "Cas de programmation linéaire",
        VERSION: "VERSION",
        SEARCH: "Chercher",
        LANG: "Langue",
        REGISTER: "Enregistrement",
        LOGIN: "Identification",
        USER: "Utilisateur",
        INTRODUCTION: "INTRODUCTION",
        PROFILE: "Mon PROFIL",
        SIGNOUT: "Sortir",
        // REGISTER COMPONENT TRANSLATIONS
        FIRST_NAME: "Prénom",
        LAST_NAME: "Nom",
        EMAIL: "Meil",
        PASSWORD: "Mot de passe",
        PRIVACY_MESSAGE: "En créer ce compte, vous adhérez à nos ",
        PRIVACY_TERMS: " Termes",
        RESET: "Initialiser",
        ALREADY_HAVE_AN_ACCOUNT_MESSAGE: " Vous avez déjà un compte ?",
        CONNECT: "Se connecter",
        FILL_FORM_MESSAGE: "Merci de remplir le forumlaire suivant ",
        // LOGIN COMPONENT TRANSLATIONS
        CONNECT_YOUR_ACCOUNT: "Connectez vous à votre compte",
        NEW_THERE: "Nouveau ici ?",
        // MAXIMIZEPROFIT1.VUE
        TITLE_1: "Maximiser le profit de votre usine 1",
        LP_DESC: "Description du P.L",
        MY_ITEMS: "Mes objets",
        MY_CONSTRAINTS: "Mes contraintes",
        MY_SOLVER_RESULT: "Mon résultat de solveur",
        MENU: "Menu",
        ADD_ITEM: "Ajouter un objet",
        PARAMETER_ME: "Paramétrez moi !",
        CALCULATE_SOLUTION_PULP: "Calculez la solution avec PULP",
        MARGIN: "Marge",
        LABOUR_TIME: "Temps de travail",
        FINITION_TIME: "Temps de finition",
        MAX_COMMERCIAL_DEMAND: "Demande commerciale Max",
        MIN_COMMERCIAL_DEMAND: "Demande commerciale Min",


    },
    ENGLISH: {
        // NAVBAR COMPONENT TRANSLATIONS
        FACTORIES_COMMON_CASES: "Factory templates",
        FOOD_COMMON_CASES: "Food templates",
        PORTFOLIOS_COMMON_CASES: "Portfolios templates",
        // HOME COMPONENT TRANSLATIONS
        INTRO: `Welcome to the vue + Python Pulp Linear programming full stack starter.
        Choose a linear programming case in the navbar menu. The app is in building state.
        Linear solvers allow to solve problems containing a lot of variables.`,
        HOME: "Home",
        DROPDOWN_TITLE_1: "Linear programming templates",
        VERSION: "Version",
        SEARCH: "Search",
        LANG: "Lang",
        REGISTER: "Register",
        LOGIN: "Login",
        USER: "User",
        INTRODUCTION: "Introduction",
        PROFILE: "My profile",
        SIGNOUT: "Signout",
        // REGISTER COMPONENT TRANSLATIONS
        FIRST_NAME: "FirstName",
        LAST_NAME: "LastName",
        EMAIL: "Email",
        PASSWORD: "Password",
        PRIVACY_MESSAGE: "By reserving an account, you agree to our ",
        PRIVACY_TERMS: " Privacy Terms",
        RESET: "Reset",
        ALREADY_HAVE_AN_ACCOUNT_MESSAGE: " Already have an account?",
        CONNECT: "Connect",
        FILL_FORM_MESSAGE: "Please fill the following form  ",
        // LOGIN COMPONENT TRANSLATIONS
        CONNECT_YOUR_ACCOUNT: "Connect your account",
        NEW_THERE: "New there ?",
        // MAXIMIZEPROFIT1.VUE
        TITLE_1: "Maximize your factory profit 1",
        LP_DESC: "L.p description",
        MY_ITEMS: "My items",
        MY_CONSTRAINTS: "My constraints",
        MY_SOLVER_RESULT: "My solver result",
        MENU: "Menu",
        ADD_ITEM: "Add an item",
        PARAMETER_ME: "Parameter me !",
        CALCULATE_SOLUTION_PULP: "Calculate solution using Pulp !",
        MARGIN: "",
        LABOUR_TIME: "",
        FINITION_TIME: "",
        MAX_COMMERCIAL_DEMAND: "",
        MIN_COMMERCIAL_DEMAND: "",

    },
    DEUTSH: {
        // NAVBAR COMPONENT TRANSLATIONS
        FACTORIES_COMMON_CASES: "Werkseitige häufige Fälle",
        FOOD_COMMON_CASES: "Häufige Fälle von Lebensmitteln",
        PORTFOLIOS_COMMON_CASES: "Portfolios häufige Fälle",
        // HOME COMPONENT TRANSLATIONS
        INTRO: `Willkommen beim Full-Stack-Starter von vue + Python Pulp Linear.
                Wählen Sie im Navigationsmenü einen linearen Programmierfall. Die App befindet sich im Gebäudezustand.
                Mit linearen Lösern können Probleme gelöst werden, die viele Variablen enthalten. `,
        HOME: "zu Hause ",
        DROPDOWN_TITLE_1: "Linearer Programmierfall",
        VERSION: "VERSION",
        SEARCH: "Suche ",
        LANG: "LANG",
        REGISTER: "Registrieren",
        LOGIN: "Einloggen ",
        USER: "Benutzer",
        INTRODUCTION: "Einführung",
        PROFILE: "Mein Profil",
        SIGNOUT: "Ausloggen",
        // REGISTER COMPONENT TRANSLATIONS
        FIRST_NAME: "Vorname",
        LAST_NAME: "Nachname",
        EMAIL: "Email",
        PASSWORD: "Passwort",
        PRIVACY_MESSAGE: "Durch die Reservierung eines Kontos stimmen Sie unserem zu",
        PRIVACY_TERMS: "Datenschutzbestimmungen",
        RESET: "Zurücksetzen",
        ALREADY_HAVE_AN_ACCOUNT_MESSAGE: "Haben Sie bereits ein Konto?",
        CONNECT: "Verbinden",
        FILL_FORM_MESSAGE: "Bitte füllen Sie das folgende Formular aus",
        // LOGIN COMPONENT TRANSLATIONS
        CONNECT_YOUR_ACCOUNT: "Verbinden Sie Ihr Konto",
        NEW_THERE: "Neu dort?",
        // MAXIMIZEPROFIT1.VUE
        TITLE_1: "Maximieren Sie Ihren Fabrikgewinn 1",
        LP_DESC: "Linear Program Beschreibung",
        MY_ITEMS: "Meine Sachen",
        MY_CONSTRAINTS: "Meine Einschränkungen",
        MY_SOLVER_RESULT: "Mein Löserergebnis",
        MENU: "Speisekarte",
        ADD_ITEM: "Fügen Sie einen Artikel hinzu",
        PARAMETER_ME: "Parameter mich!",
        CALCULATE_SOLUTION_PULP: "Berechnen Sie die Lösung mit Pulp !",
        MARGIN: "",
        LABOUR_TIME: "",
        FINITION_TIME: "",
        MAX_COMMERCIAL_DEMAND: "",
        MIN_COMMERCIAL_DEMAND: "",




    },
    SPANISH: {
        // NAVBAR COMPONENT TRANSLATIONS
        FACTORIES_COMMON_CASES: "Casos comunes de fábrica",
        FOOD_COMMON_CASES: "Casos comunes de alimentos",
        PORTFOLIOS_COMMON_CASES: "Portafolios casos comunes",
        // HOME COMPONENT TRANSLATIONS
        INTRO: `
                Bienvenido al iniciador de pila completa de programación lineal vue + Python Pulp.
                Elija un caso de programación lineal en el menú de la barra de navegación.La aplicación está en estado de construcción.
                Los solucionadores lineales permiten resolver problemas que contienen muchas variables.
                `,
        HOME: "Casa",
        DROPDOWN_TITLE_1: "Caso de programación lineal",
        VERSION: "Versión",
        SEARCH: "Buscar",
        LANG: "Lang",
        REGISTER: "Registrarse",
        LOGIN: "Iniciar sesión",
        USER: "Usuaria",
        INTRODUCTION: "INTROduccion",
        PROFILE: "Mi perfil",
        SIGNOUT: "desconectar",
        // REGISTER COMPONENT TRANSLATIONS
        FIRST_NAME: "Nombre ",
        LAST_NAME: "Apellido ",
        EMAIL: "Correo electrónico",
        PASSWORD: "Contraseña",
        PRIVACY_MESSAGE: "Al reservar una cuenta, acepta nuestro",
        PRIVACY_TERMS: "Condiciones de privacidad",
        RESET: "Reset",
        ALREADY_HAVE_AN_ACCOUNT_MESSAGE: "¿Ya tienes una cuenta?",
        CONNECT: "Conectar",
        FILL_FORM_MESSAGE: "Por favor, complete el siguiente formulario",
        // LOGIN COMPONENT TRANSLATIONS
        CONNECT_YOUR_ACCOUNT: "Conecta tu cuenta",
        NEW_THERE: "¿Nuevo allí?",
        // MAXIMIZEPROFIT1.VUE
        TITLE_1: "Maximice el beneficio de su fábrica 1",
        LP_DESC: "L.p descripción",
        MY_ITEMS: "Mis cosas",
        MY_CONSTRAINTS: "Mis limitaciones",
        MY_SOLVER_RESULT: "Mi resultado de solucionador",
        MENU: "Menu",
        ADD_ITEM: "Agregar un artículo",
        PARAMETER_ME: "Parametrizarme !",
        CALCULATE_SOLUTION_PULP: "Calcule la solución usando pulp !",
        MARGIN: "",
        LABOUR_TIME: "",
        FINITION_TIME: "",
        MAX_COMMERCIAL_DEMAND: "",
        MIN_COMMERCIAL_DEMAND: "",



    },
    HINDI: {
        // NAVBAR COMPONENT TRANSLATIONS
        FACTORIES_COMMON_CASES: "कारखाने आम मामलों",
        FOOD_COMMON_CASES: "खाद्य आम मामलों",
        PORTFOLIOS_COMMON_CASES: "विभागों आम मामलों",
        // HOME COMPONENT TRANSLATIONS
        INTRO: `
                Vue + पायथन पल्प रैखिक प्रोग्रामिंग फुल स्टैक स्टार्टर में आपका स्वागत है।
                नावबार मेनू में एक रैखिक प्रोग्रामिंग केस चुनें। एप्लिकेशन निर्माण की स्थिति में है।
                लीनियर सॉल्वर बहुत अधिक चर वाली समस्याओं को हल करने की अनुमति देते हैं। `,
        HOME: " घर घर",
        DROPDOWN_TITLE_1: "रैखिक प्रोग्रामिंग का मामलाe",
        VERSION: "संस्करण",
        SEARCH: "खोज",
        LANG: "लैंग",
        REGISTER: "रजिस्टर करें",
        LOGIN: "लॉग इन करें",
        USER: "उपयोगकर्ता",
        INTRODUCTION: "परिचय",
        PROFILE: "मेरी प्रोफाइल",
        SIGNOUT: "प्रस्थान करें",
        // REGISTER COMPONENT TRANSLATIONS
        FIRST_NAME: "पहला नाम",
        LAST_NAME: "उपनाम ",
        EMAIL: "ईमेल",
        PASSWORD: "कुंजिका",
        PRIVACY_MESSAGE: "खाता जलाकर, आप हमारे लिए सहमत हैं",
        PRIVACY_TERMS: "गोपनीयता व शर्तें",
        RESET: "रीसेट",
        ALREADY_HAVE_AN_ACCOUNT_MESSAGE: "पहले से ही एक खाता है ?",
        CONNECT: "जुडिये",
        FILL_FORM_MESSAGE: "कृपया निम्नलिखित फॉर्म भरें",
        // LOGIN COMPONENT TRANSLATIONS
        CONNECT_YOUR_ACCOUNT: "अपना खाता कनेक्ट करें",
        NEW_THERE: "वहाँ नया है ?",
        // MAXIMIZEPROFIT1.VUE
        TITLE_1: "अपने कारखाने के लाभ को अधिकतम करें",
        LP_DESC: "रैखिक कार्यक्रम का वर्णन",
        MY_ITEMS: "मेरे आइटम",
        MY_CONSTRAINTS: "मेरी अड़चन है",
        MY_SOLVER_RESULT: "मेरा सॉल्वर रिजल्ट",
        MENU: "मेन्यू",
        ADD_ITEM: "सामान जोडें",
        PARAMETER_ME: "मुझे पैरामीटर",
        CALCULATE_SOLUTION_PULP: "पल्प का उपयोग करके समाधान की गणना करें !",
        MARGIN: "",
        LABOUR_TIME: "",
        FINITION_TIME: "",
        MAX_COMMERCIAL_DEMAND: "",
        MIN_COMMERCIAL_DEMAND: "",
    },
    CHINESE: {
        // NAVBAR COMPONENT TRANSLATIONS
        FACTORIES_COMMON_CASES: "工厂常见情况",
        FOOD_COMMON_CASES: "食品常见案例",
        PORTFOLIOS_COMMON_CASES: "投资组合常见案例",
        // HOME COMPONENT TRANSLATIONS
        INTRO: `
                欢迎使用vue + Python Pulp线性编程完整堆栈入门。
                在导航栏菜单中选择一个线性编程条件。 该应用程序处于构建状态。
                线性求解器可以解决包含很多变量的问题。 `,
        HOME: " 家",
        DROPDOWN_TITLE_1: "线性规划案例",
        VERSION: "版",
        SEARCH: "搜索",
        LANG: "郎",
        REGISTER: "寄存器",
        LOGIN: "登录",
        USER: "用户",
        INTRODUCTION: "介绍",
        PROFILE: "我的简历",
        SIGNOUT: "登出",
        // REGISTER COMPONENT TRANSLATIONS
        FIRST_NAME: "名字",
        LAST_NAME: "姓",
        EMAIL: "电子邮件",
        PASSWORD: "密码",
        PRIVACY_MESSAGE: "预订帐户即表示您同意我们的",
        PRIVACY_TERMS: "隐私权和条款",
        RESET: "重启",
        ALREADY_HAVE_AN_ACCOUNT_MESSAGE: "已经有帐号了？",
        CONNECT: "连接",
        FILL_FORM_MESSAGE: "请填写以下表格",
        // LOGIN COMPONENT TRANSLATIONS
        CONNECT_YOUR_ACCOUNT: "连接您的帐户",
        NEW_THERE: "新来的？",
        // MAXIMIZEPROFIT1.VUE
        TITLE_1: "最大化您的工厂利润",
        LP_DESC: "线性程序说明",
        MY_ITEMS: "我的物品",
        MY_CONSTRAINTS: "我的约束",
        MY_SOLVER_RESULT: "我的求解器结果",
        MENU: "菜单",
        ADD_ITEM: "新增项目",
        PARAMETER_ME: "参数我",
        CALCULATE_SOLUTION_PULP: "用纸浆计算溶液!",
        MARGIN: "",
        LABOUR_TIME: "",
        FINITION_TIME: "",
        MAX_COMMERCIAL_DEMAND: "",
        MIN_COMMERCIAL_DEMAND: "",
    }
});
// ---------------------------------------------- END VUEX DATA STORE - SHARING DATA BETWEEN COMPONENTS !-------------------------------------
new Vue({
    router,
    render: h => h(App),
    store: store
}).$mount("#app");