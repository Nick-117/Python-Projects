# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇




# Under 18.5 they are overweight COMPLETE
# over 18.5 but below 25 they have a normal weightover 25 but below 30 they are slightly overweight\over 30 but below 35 they are obese
# above 35 they are clinically obese
   
BMI = round(weight / height **2)



if BMI < 18.5:
    print(f"your BMI is {BMI}, you are underweight.")
    
if BMI > 18.5:
    print()
    if BMI < 25:
        print(f"Your BMI is {BMI}, you have a normal weight.")
if BMI > 25:
    print()
    if BMI < 30:
        print(f"Your BMI is {BMI}, you are slightly overweight.")

if BMI > 30:
    print()
    if BMI < 35:
        print(f"Your BMI is {BMI}, you are obese.")
    else:
        print(f"Your BMI is {BMI}, you are clinically obese.")





    
        

    
        

# it works! 1.75 / 85 = 28






