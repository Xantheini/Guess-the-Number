from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100. ")

number = random.randint(1, 100)
attempts = 0

# Set difficulty level of game
def level(): 
  global attempts
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")
  if difficulty.lower().strip() == 'easy': 
    print("You have 10 attempts to guess the number correctly. ")
    attempts = 10
  elif difficulty.lower().strip() == 'hard': 
    print("You have 5 attempts to guess the number correctly. ") 
    attempts = 5
  else: 
    print("You have chosen an invalid difficult. ")
    level()

# Setting up guesses 
def game_guesses(): 
  global attempts

  while attempts > 0: 
    try: 
      guess = int(input("Make a guess: \n"))
    except ValueError: 
      print("Your guess was invalid. Please guess again. ")
      guess = int(input("Make a guess: \n"))
    if guess == number: 
      print("You guessed the number! Congrats! ") 
      break
    elif guess > number: 
      attempts = attempts - 1 
      print("Your guess was too high. ")
      print(f"You have {attempts} remaining. ")
    elif guess < number: 
      attempts = attempts - 1 
      print("Your guess was too low. ")
      print(f"You have {attempts} remaining. ")

  if attempts == 0: 
    print(f"You lose. The number was {number}.")

# Main Game 
def game(): 
  global number
  level()

  game_guesses()
  
  play_again = input("Would you like to play again? Type 'y' or 'n': \n")
  if play_again.lower().strip() == 'y': 
    number = random.randint(1, 100)
    game()
  else:
    print("Goodbye. ")

game()
