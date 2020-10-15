# LOADING THE LINEAR SOLVER
import pulp
from pulp import *

# ----------------------------------------------------- LINEAR SOLVER FUNCTIONS ---------------------------------------------------

# Please notice, for now it is static, but it will become dynamic, I know it's ugly for now.
def pulp_minimize_cost_1(post_data):

    # INIT VARIABLES
    Ingredients = []
    costs = {}
    calcium = {}
    proteins = {}
    fibers = {}

    # Getting ingredients names
    for obj in post_data["ingredients"]:
        Ingredients.append(obj["name"])

    # Getting ingredients params
    for obj in post_data["ingredients"]:
        costs[obj["name"]] = float(obj["cost"])
        calcium[obj["name"]] = float(obj["calcium"])
        proteins[obj["name"]] = float(obj["proteins"])
        fibers[obj["name"]] = float(obj["fibers"])

    # This is a minimization problem - C'est un problème de minimisation
    prob = LpProblem("MinimizeMyFoodCost", LpMinimize)

    # We create the variable dictionnary - On se sert du dictionnaire Ingredients pour créer nos variables
    ingredient_vars = LpVariable.dicts("Ingr",Ingredients,0)
    

    # This is the objective function - Notre function objectif s'exprime en euros ou en dollars
    prob += lpSum([costs[i] * ingredient_vars[i] for i in Ingredients]), "Cout total des ingrédients par boite de conserve de 1kg"

    # Conservation - La production totale est de 1 kg
    prob += lpSum([ingredient_vars[i] for i in Ingredients]) == 1 ,"conservation"

    # Constraints - On spécifie au solveur PULP Nos contraintes de qualité pour ne pas créer un paté de mauvaise qualité ...
    prob += lpSum([calcium[i]    * ingredient_vars[i] for i in Ingredients]) >= 0.008, "calciumRequirementMin"
    prob += lpSum([calcium[i]    * ingredient_vars[i] for i in Ingredients]) <= 0.012, "calciumRequirementMax"
    prob += lpSum([proteins[i]    * ingredient_vars[i] for i in Ingredients]) >= 0.22,  "proteinRequirementMin"
    prob += lpSum([fibers[i]      * ingredient_vars[i] for i in Ingredients]) <= 0.05,  "fiberRequirementMax"

    # POSSIBILITE Utilisation minimale en g par element
    # for p in Ingredients:
    #    prob += ingredient_vars[p] >= 10, f"min  for product {p}"

    #  Wrting the prob in a file - On écrit le P.l dans un fichier
    prob.writeLP("lps/MinimizeMyFoodCost.lp")
    prob.solve()

    # Print LP status - le statut du lp
    print ("Status:", LpStatus[prob.status])
    
    myResult ={}
    myResult["status"] = LpStatus [prob.status]
    
    # Print each prob variables - Chauqe variable de décision est affichée avec son nom et sa valeur trouvée par l'algo
    for v in prob.variables():
        print (v.name, "=", v.varValue)
        myResult[v.name] = v.varValue
        
    # Objective function result - Le résultat de la fonction objectif :
    print ("Cout total des ingrédients par boite de conserve de 1kg = ", value(prob.objective), "Centimes")
    
    # Objective function result - Le résultat de la fonction objectif est ici :
    myResult["TotalCost"] = value(prob.objective)
    myResult["PulpLpSummary"] = open("lps/MinimizeMyFoodCost.lp", 'r').read() 

    # Return the solution to the front end
    return   myResult
