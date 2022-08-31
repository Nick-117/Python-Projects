# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
# remember, it's PEMDASLR-multiplication is equal to division & Addition is equal to Subtraction, its all depending on who is closest to the left.
 
# BMI calculation 
 
 
height_equat_1 = (height[0])
height_equat_2 = (height[1])
height_equat_3 = (height[2])

Whole_number = (height_equat_1 + height_equat_2 + height_equat_3)

New_Whole_Number = float(Whole_number)


# print(type(New_Whole_Number))
# This is the FINAL conversion for HEIGHT

weight_equat_1 = (weight[0])
weight_equat_2 = (weight[1])

Whole_weight = (weight_equat_1 + weight_equat_2)

Inte_Whole_Weight = int(Whole_weight)

# This is the FINAL conversion for WEIGHT


Final_outcome = int(Inte_Whole_Weight / (New_Whole_Number **2))
print(Final_outcome)
