// https://stackoverflow.com/questions/35045119/how-can-i-share-a-method-between-components-in-vue-js
export default {
    // THIS HELPER FUNCTION CONVERTS THE FRONT END DATA TO THE PYTHON PULP LINEAR COMPATIBLE FORMAT
    formatDataForPulp: async function(data) {

        // INIT PULP FORMAT VARIABLES
        var lpVars = []; // DECISION VARIABLES LIST NEEDED BY PULP
        var parameters = {}; // ITEMS PARAMETERS IN THE PULP FORMAT
        var constraints = {}; // CONSTRAINTS PARAMETERS IN THE PULP FORMAT

        //    STEP 1 FILLING DECISIONS VARIABLES FOR THE PULP LINEAR SOLVER  ( HE NEEDS A SIMPLE DECISION VARIABLE ** LIST)
        for (var x in data.items) {
            lpVars.push(data.items[x].name);
        }
        data.lpVars = lpVars;

        //  STEP 2 FILLING  ITEMS PARAMETERS FOR THE PULP LINEAR SOLVER ( HE NEEDS ** DICTIONNARIES)

        for (var i = 0, item;
            (item = data.items[i++]);) {
            for (var key in item) {
                delete item.img;
                // console.log(key + ":" + item[key])
                var name = item.name;
                if (!parameters["" + key + ""]) {
                    parameters["" + key + ""] = {};
                    parameters["" + key + ""][name] = item[key];
                } else {
                    parameters["" + key + ""][name] = item[key];
                }
            }
        }
        data.parameters = parameters;

        //  STEP 3 FILLING CONSTRAINTS FOR THE PULP LINEAR SOLVER ( HE NEEDS ** DICTIONNARIES)
        for (var i = 0, constraint;
            (constraint = data.constraints[i++]);) {
            constraints[constraint.name] = constraint.value;
        }
        data.constraints = constraints;

        return data;
    },
    // THIS EXPERIMENTAL SECOND HELPER FUNCTION CONVERTS THE FRONT END DATA TO THE PYTHON PULP LINEAR COMPATIBLE FORMAT
    formatDataForPulpExperimental: async function(data) {

    }
};