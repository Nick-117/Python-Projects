# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# A Leap year falls into steps:

# 1: it at least needs to be able to be cleanly divisible by 4,
# 2: cannot be cleanly divisible by 100/ IF it is, than it must be cleanly divisible by 400

# Non-Leap year steps

# 1: cannot be divisible by 4, if it is than-
# 2: It cannot be cleanly divisible by 100 if it is, than-
# 3: It cannot be cleanly divisible by 400

# all division problems in python end up as a float, whole numbers are represented by a zero in decimal value so I need a way to ensure that the decimal value is zero to determine if its a whole number.





four_year = (year / 4)


hundred_year = (year / 100)

fourhundred_year = (year / 400)







from math import *

if (four_year).is_integer():
    print("leap Year")

# if this is true, then you move onto to the next which is 100
    if (hundred_year.is_integer()):
        print("leap year")
        if (fourhundred_year.is_integer()):
             print("leap year")
else:
    print("Not leap year")

  






