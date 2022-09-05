#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random	
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇





random_number = random.randint(0, 1)


if random_number == 0:
    print("Tails")

else:
    print("Heads")




















# we need to write a code that makes it so that t randomly tells the user "heads"
# or "tails". they need to be capitalized. The number that is generated needs to be used to print out "heads" or "tails".