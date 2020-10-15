<template>
<div class="main-form">

    <div class="row">
        <!-- SIDE  -->
        <div class="col-md-2">
            <img src="../assets/industry-1430036-1207834.webp" class="main_img">

            <h5> Minimize your food production cost </h5>
            <h5> Minimisez votre cout de production </h5>
            <h5 style="color:red"> Warning : Building ! </h5>
        </div>

        <!-- MAIN  -->
        <div class="col-md-10">
            <b-form @submit="onSubmit" v-if="show">
                <b-tabs active-nav-item-class="font-weight-bold  text-danger">
                    <b-tab title="L.P description" active>
                        <b-form-input v-model="lpDescription"></b-form-input><br>
                        <p>
                            <img src="../assets/9. staff_ulsu_ru_semushin_index_pilocus_gist_docs_myc_simplex_DemoCD_SIMPLEX_DemoTools_t6_index_87_html-1.jpg" style="max-width:1000px;"></img>
                        </p>
                    </b-tab>
                    <b-tab title="My Ingredients">

                        <b-card-group deck>
                            <b-card header-tag="header" footer-tag="footer" img-alt="Image" v-for="ingredient in ingredients" img-top :key="ingredient.name">

                                <img :src="require(`../assets/${ingredient.img}`)" v-bind:alt="img" alt="Image" class="card-img-top card-img-spe">

                                <template v-slot:header>
                                    <h6 class="mb-0">{{ingredient.name}}(Kg/Kg)</h6>
                                </template>
                                <br>
                                <b-card-text>Cost <span class="float-right"> {{ingredient.cost}} (cents/kg) $</span></b-card-text>
                                <range-slider class="slider" min="0" max="100" step="0.1" v-model="ingredient.cost"> </range-slider>

                                <b-card-text>Calcium <span class="float-right"> {{ingredient.calcium}} (kg/kg) </span></b-card-text>
                                <range-slider class="slider" min="0" max="1" step="0.001" v-model="ingredient.calcium"> </range-slider>

                                <b-card-text>Protein <span class="float-right"> {{ingredient.proteins}} (kg/kg) </span></b-card-text>
                                <range-slider class="slider" min="0" max="1" step="0.001" v-model="ingredient.proteins"> </range-slider>

                                <b-card-text>Fiber <span class="float-right"> {{ingredient.fibers}} (kg/kg) </span></b-card-text>
                                <range-slider class="slider" min="0" max="1" step="0.001" v-model="ingredient.fibers"> </range-slider>

                                <template v-slot:footer>
                                    <em class="float-right">Parameter me !</em>
                                </template>
                            </b-card>

                        </b-card-group>

                    </b-tab>
                    <b-tab title="My Constraints">
                        <b-card-group deck>
                            <b-card v-for="constraint in constraints" header-tag="header" footer-tag="footer" img-alt="Image" img-top :key="constraint.name">
                                <img :src="require(`../assets/${constraint.img}`)" alt="Image" class="card-img-top card-img-spe">
                                <template v-slot:header>
                                    <h6 class="mbs-0">{{constraint.name}}</h6>
                                </template>
                                <b-card-text>Requirement</b-card-text>
                                <!-- <range-slider class="slider" min="0" max="100" step="1" v-model="constraint.value"> </range-slider> -->
                                <vue-slider v-model="constraint.value"></vue-slider>
                                <span class="float-right"> Min : {{constraint.value[0]}} % - Max : {{constraint.value[1]}} %</span>

                                <template v-slot:footer>
                                    <em class="float-right">Parameter me !</em>
                                </template>
                            </b-card>
                        </b-card-group>
                    </b-tab>
                    <b-tab title="My Solver result">

                        <div class="row">
                            <div class="col-lg-4">

                                <b-card header="Reminder - Items and constraints :" class ="reminder">
                                    Items :
                                    <pre class="m-0">{{ ingredients }} </pre>
                                    Constraints :
                                    <pre class="m-0"> {{ constraints }}</pre>
                                </b-card>

                            </div>
                            <div class="col-lg-6">
                                <b-card header="Linear solver result">
                                    <pre class="m-0">{{ linearSolverResult }}</pre>
                                </b-card>
                                <b-card header="Pulp L.p description">

                                    <pre class="m-0">{{ PulpLpSummary }}</pre>

                                </b-card>
                            </div>
                            <div class="col-lg-2">
                                <b-button class="float-right" type="submit" variant="primary">Calculate solution with PULP</b-button>
                            </div>
                        </div>
                    </b-tab>
                </b-tabs>
            </b-form>
        </div>
    </div>
</div>
</template>

<script>
// Importing libs
import axios from 'axios';

// https://github.com/NightCatSama/vue-slider-component
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/antd.css'

// https://github.com/ktsn/vue-range-slider
import RangeSlider from 'vue-range-slider'

// you probably need to import built-in style
import 'vue-range-slider/dist/vue-range-slider.css'

export default {
    data() {
        return {
            ingredients: [{
                    "name": "Flour (Limestone)",
                    "cost": 10.0,
                    "calcium": 0.38,
                    "proteins": 0,
                    "fibers": 0,
                    "img": "flour.webp"
                },
                {
                    "name": "Corn",
                    "cost": 30.5,
                    "calcium": 0.001,
                    "proteins": 0.09,
                    "fibers": 0.02,
                    "img": "single-ear-corn-isolated-on-260nw-793795156.webp"
                },
                {
                    "name": "Soy",
                    "cost": 90.0,
                    "calcium": 0.002,
                    "proteins": 0.50,
                    "fibers": 0,
                    "img": "OIP.yU-tKXJfFTuHH6QXDdPj6wHaE7.jpg"
                }
            ],
            constraints: [{
                    "name": "Calcium",
                    "value": [8, 12],
                    "img": "calcium.jpg"
                },
                {
                    "name": "Proteins",
                    "value": [22, 100],
                    "img": "proteins.png"
                },
                {
                    "name": "Fibers",
                    "value": [5, 100],
                    "img": "fibers.jpg"
                }
            ],
            show: true,
            linearSolverResult: {},
            lpDescription: "Minimize my 1kg food cost !",
            PulpLpSummary: "",
            img: ""

        }
    },
    components: {
        VueSlider,
        RangeSlider
    },
    computed: {
        total: function () {
            return this.value * 10
        }
    },
    methods: {

        getLinearSolver() {
            const path = '/api/minimize_cost_1';
            var data = {
                "ingredients": this.ingredients,
                "constraints": this.constraints
            }
            axios.post(path, data)
                .then((res) => {
                    this.linearSolverResult = res.data;

                    // Designing the PULP Lp desc coming from pulp
                    this.PulpLpSummary = this.linearSolverResult.PulpLpSummary;
                    this.PulpLpSummary.replace(new RegExp('\r?\n', 'g'), '<br />');

                    // Removing the PulpLpSUmmary from the main JSON result
                    delete this.linearSolverResult.PulpLpSummary;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
        onSubmit(evt) {
            evt.preventDefault()
            this.getLinearSolver()
        },
        reset() {

            location.reload()
            // evt.preventDefault()
            // Reset our form values TODO

            // Trick to reset/clear native browser form validation state
            this.show = false
            this.$nextTick(() => {
                this.show = true
            })
        }
    }
}
</script>

<style>
@media (min-width:1024px) {

    .img-spe {
        max-height: 250px;
        min-height: 250px;
    }

}

fieldset {
    background-color: #fef5e4 !important;
    border-radius: 4px;
}

.main_form {
    margin: 30px;
}

.main_img {
    width: 150px
}

legend {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 4px;
    color: var(--purple);
    font-size: 17px;
    font-weight: bold;
    padding: 3px 5px 3px 7px;
    width: auto;
}

.slider {
    /* overwrite slider styles */
    width: 100%;
}
</style>
