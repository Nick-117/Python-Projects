#Number Guessing Game Objectives:
import random
from art import Logo
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# easy_lives = 10
# hard_lives = 5


# def easy_take_life(easy_lives):
#   return easy_lives - 1
  
  
# def hard_take_life(hard_lives):
#   return hard_lives - 1



  
  # neg_life = lives -= 1
  


chosen_number = random.randint(1, 100)

guessing_game = True

easy_lives = 10
hard_lives = 5


# if difficulty == "hard":
#   return  subtract_2
print(Logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100, what is it? ")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

while guessing_game is True:
  guess = int(input("make a guess: "))

  
  if guess == chosen_number:
    print("you got it!")
    guessing_game = False
    
    
  
  elif guess > chosen_number and difficulty == "easy":
    easy_lives -= 1
    print("Too High")
    print(f"You have {easy_lives} lives left.")
    
    # clear()

  elif guess > chosen_number and difficulty == "hard":
    hard_lives -= 1
    print("Too High.")
    print(f"You have {hard_lives} lives left")

  
  elif guess < chosen_number and difficulty == "easy":
    easy_lives -= 1
    print("Too Low")
    print(f"You have {easy_lives} lives left.")
    # easy_lives()

  elif guess < chosen_number and difficulty == "hard":
    hard_lives -= 1
    print("Too Low")
    print(f"You have {hard_lives} lives left")


  
  if easy_lives == 0 or hard_lives == 0:
    print(f"game over, the number was {chosen_number}.")
    guessing_game = False

    