\* Portfolio_Opt *\
Minimize
OBJ: 40 Potential_Investment_Antony_Hotels_
 + 30 Potential_Investment_Arkansas_REIT
 + 25 Potential_Investment_Atlantic_Lightning_
 + 65 Potential_Investment_Minocompo_System
 + 15 Potential_Investment_Nocal_Mining_Bond_
 + 20 Potential_Investment__Bedrock_Insurance_Annuity_____
Subject To
Investments: Potential_Investment_Antony_Hotels_
 + Potential_Investment_Arkansas_REIT
 + Potential_Investment_Atlantic_Lightning_
 + Potential_Investment_Certificate_of_deposit_
 + Potential_Investment_Minocompo_System
 + Potential_Investment_Nocal_Mining_Bond_
 + Potential_Investment_Saving_Account_
 + Potential_Investment__Bedrock_Insurance_Annuity_____ = 100000
Liquidity: Potential_Investment_Antony_Hotels_
 + Potential_Investment_Arkansas_REIT
 + Potential_Investment_Atlantic_Lightning_
 + Potential_Investment_Minocompo_System
 + Potential_Investment_Saving_Account_ >= 40000
Ratings: Potential_Investment_Certificate_of_deposit_
 + Potential_Investment_Minocompo_System
 + Potential_Investment_Saving_Account_
 + Potential_Investment__Bedrock_Insurance_Annuity_____ >= 50000
Returns: 0.125 Potential_Investment_Antony_Hotels_
 + 0.1 Potential_Investment_Arkansas_REIT
 + 0.071 Potential_Investment_Atlantic_Lightning_
 + 0.052 Potential_Investment_Certificate_of_deposit_
 + 0.2 Potential_Investment_Minocompo_System
 + 0.065 Potential_Investment_Nocal_Mining_Bond_
 + 0.04 Potential_Investment_Saving_Account_
 + 0.082 Potential_Investment__Bedrock_Insurance_Annuity_____ >= 7500
Save_and_CD: Potential_Investment_Certificate_of_deposit_
 + Potential_Investment_Saving_Account_ <= 30000
End
