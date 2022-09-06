

import random
from art import logo
from art import vs
from game_data import data
from replit import clear

# def add_point():
add_score = 0
def add_score(add_score):
  """adds a point to the scoreboard."""
  # add_score = 0
  return add_score + 1


# def celeb_1():

  
# score = 0  
# game_over = False
# initial_run = True

def Higher_lower():
  score = 0  
  game_over = False
  initial_run = True
  
  while game_over == False:
    print(logo)  

    if score == 0:
          
      celeb1 = random.choice(data)

      list = []
      for name in celeb1:
        list.append(celeb1[name])

      celeb = list[0]
      occupation = list[2]
      address = list[3]
      celeb1_A = list[1]
      
    celeb2 = random.choice(data)
    
    # print(celeb1) - shows the selected list
    # print(celeb2)  
    
    
    list2 = []
    for name2 in celeb2:
      list2.append(celeb2[name2])
      
    
    # print(list)
    # print(list2)  organizes the different dictionary terms into a list
    
    
    celeb2 = list2[0]
    occupation2 = list2[2]
    address2 = list2[3]
    celeb2_B = list2[1]
    
    if score > 0:
      print(f"You're right! Current score: {score}")
      # celeb = celeb2
      # occupation = occupation2
      # address = address2
        
      
    A = f"Compare A: {celeb}. a {occupation} from {address}"
    print(A)
    
    print(vs)
    
    B = f"Against B: {celeb2} a {occupation2}, from {address2}"
  
    print(B)
  
  
    
    guess = input("who has more followers? Type 'A' or 'B'")
  
    
    
    if guess.upper() == "A" and celeb1_A > celeb2_B:
      score = add_score(score)
      # print(f"Correct! You have {score} point.")
      celeb = celeb2
      occupation = occupation2
      address = address2
      celeb1_A = celeb2_B
      clear()
      
  
      # add function for point tracking'
    elif guess.upper() == "B" and celeb1_A < celeb2_B:
      score = add_score(score)
      # print(f"Correct! you have {score} point.")
      celeb = celeb2
      occupation = occupation2
      address = address2
      celeb1_A = celeb2_B
      clear() 
       
    else:
      print("Sorry, that's wrong.")
      clear()
      game_over = True
      
   
  if game_over == True:
    print(logo)
    print(f"Sorry that's wrong, Final score: {score}")
    
Higher_lower()









  
# final score goes in the string





# print(vs)

# input("Who has more followers? Type 'A' or 'B':")
