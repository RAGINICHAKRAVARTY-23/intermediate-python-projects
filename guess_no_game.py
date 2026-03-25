from random import randint 
from logo import game_logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check user's guess against the actual number
def check_answer(user_guess , actual_answer , turns):
  """Checks answer against guess , returns the number of turns remaining."""
  if user_guess > actual_answer:
    print("Too High.")
    return turns - 1
  elif user_guess < actual_answer:
    print("Too Low.")
    return turns - 1
  else:
    print(f"Yes! the answer is {actual_answer}")
#function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard'.")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
     return HARD_LEVEL_TURNS

def game():
  print(game_logo)
  #choosing a number between 1 to 100
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100.")
  answer = randint(1,100)
  turns = set_difficulty()
  #repeat the guessing functionality if they get it wrong 
  guess = 0
  while guess != answer:

    print(f"You have {turns} attempts remaining to guess the number.")
    #let the user guess a number
    guess = int(input("Make a guess:\n"))
    turns = check_answer(guess , answer, turns)
    if turns == 0:
      print(f"You have run out of guesses , you loose!\nThe correct answer was {answer}")
      return
    elif guess != answer:
      print("Guess again!")
  #track the number of turns and reduce by 1 if they get it wrong

game()

