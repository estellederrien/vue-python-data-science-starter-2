\* The_Whiskas_Problem *\
Minimize
Cout_total_des_ingrédients_par_boite_de_conserve_de_100g:
 0.013 Ingredient_chicken + 0.008 Ingredient_meat
Subject To
FatRequirement: 0.08 Ingredient_chicken + 0.1 Ingredient_meat >= 6
PercentagesSum: Ingredient_chicken + Ingredient_meat = 100
ProteinRequirement: 0.1 Ingredient_chicken + 0.1 Ingredient_meat >= 8
fibresRequirement: 0.001 Ingredient_chicken + 0.005 Ingredient_meat <= 2
saltRequirement: 0.002 Ingredient_chicken + 0.005 Ingredient_meat <= 0.4
End
