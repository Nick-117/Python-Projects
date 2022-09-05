# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# T
# R
# U
# E

# L
# O
# V
# E

# We need to see how often each of the letters above occur in each inputted person's name we then count and add combine(not adding) the value as a concatenated string. So if the total amount of letters for the word "TRUE" is 5 and the total for "LOVE" is 6- the result would be a 56("Your score is "x")


         #(x)      (<)              (>)
# If the score is less than 10 OR greater than 90 the message is: "Your score is "x". you go together like coke and mentos"
          # (print) 


        # (x)        ( >= 40 and <= 50 )
# if the score is between 40 and 50 the message is: "Your score is "x", you are alright together.
    #   (Print)


# otherwise, the message will just be their score: "Your score is "x"

# Example:

# Kanye West    Kim Kardashian
# T- 1        
# R- 1       
# U- 0        
# E- 2        

# L- 0        
# O- 0       
# V- 0      
# E- 2       

# 1.  We have turned all inputted named into high-caps, just like the letters - COMPLETE

# 2. We need to count the number of letters in the words "TRUE" and "LOVE" that are within the input names using the- print(x.count("letter")) function.  COMPLETE


name1_upper = name1.upper()

name2_upper = name2.upper()





# print(name1.count("t") + name2.count("t"))

# print(name1.count("t") + name2.count("t"))

# print(type(name1.count("t")))
# print(type(name2.count("t")))



# print(name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e"))
# print(name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e"))


# print(name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e"))
# print(name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e"))

# The above values are the integer values of the letters

name1_true = name1_upper.count("T") + name1_upper.count("R") + name1_upper.count("U") + name1_upper.count("E")
name1_love = name1_upper.count("L") + name1_upper.count("O") + name1_upper.count("V") + name1_upper.count("E")

name2_true = name2_upper.count("T") + name2_upper.count("R") + name2_upper.count("U") + name2_upper.count("E")
name2_love = name2_upper.count("L") + name2_upper.count("O") + name2_upper.count("V") + name2_upper.count("E")




# print(name1_true)
# print(name1_love)


# print(name2_true)
# print(name2_love)









combined_truev = str(name1_true + name2_true)

combined_lovev = str(name1_love + name2_love)


# print(type(combined_truev))
# print(type(combined_lovev))


love_score = combined_truev + combined_lovev

love_score_num = int(love_score)



if love_score_num < 10 or love_score_num > 90:
    print(f"Your score is {love_score_num}. you go together like coke and mentos.")

elif love_score_num > 40 and love_score_num < 50 and love_score_num < 90:
    print(f"Your score is {love_score_num}, you are alright together.")

elif love_score_num > 40 and love_score_num < 50:
    print(f"your score is {love_score_num}, you are alright together.")

else:
    print(f"Your score is {love_score_num}.")










import module_test


print(module_test.Ty)





