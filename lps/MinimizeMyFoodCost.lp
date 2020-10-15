\* MinimizeMyFoodCost *\
Minimize
Cout_total_des_ingrédients_par_boite_de_conserve_de_1kg: 30.5 Ingr_Corn
 + 10 Ingr_Flour_(Limestone) + 90 Ingr_Soy
Subject To
calciumRequirementMax: 0.001 Ingr_Corn + 0.38 Ingr_Flour_(Limestone)
 + 0.002 Ingr_Soy <= 0.012
calciumRequirementMin: 0.001 Ingr_Corn + 0.38 Ingr_Flour_(Limestone)
 + 0.002 Ingr_Soy >= 0.008
conservation: Ingr_Corn + Ingr_Flour_(Limestone) + Ingr_Soy = 1
fiberRequirementMax: 0.02 Ingr_Corn <= 0.05
proteinRequirementMin: 0.09 Ingr_Corn + 0.5 Ingr_Soy >= 0.22
End
