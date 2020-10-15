\* Maximize_Profit *\
Maximize
MaximizeProfit: 17 items__chair + 18 items__low_table + 9 items__stool
 + 7 items__table
Subject To
ct1: 7 items__chair + 5 items__low_table + 4 items__stool + 2 items__table
 <= 42
ct2: 2 items__chair + 2 items__low_table + items__stool + items__table <= 17
ct3: 3 items__chair + 3 items__low_table + 2 items__stool + items__table <= 24
Bounds
0 <= items__chair
0 <= items__low_table
0 <= items__stool
0 <= items__table
Generals
items__chair
items__low_table
items__stool
items__table
End
