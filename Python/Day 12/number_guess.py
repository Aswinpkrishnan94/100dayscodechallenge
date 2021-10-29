from random import randint
from art import logo

# import random function library
import random
print(logo)

# Mode 1: Easy mode: User gets 10 chances to guess the number
def easy():
  print("You got 10 chances to guess the number\n")
  x=0
  while x<11:
    number=int(input("Guess a number between 1 and 100\n"))

    if number==comp_choice:
      print("You guessed it correct\n")
      return 0

    else:
      if number>comp_choice:
          print("high\n")
          x+=1
          continue
      else:
          print(" low\n")
          x+=1
          continue
  print("you lost all chances\n")
  print("computer choice was {comp_choice}")
  return 0
  
# Mode 2: User gets 5 chances to guess the number  
def hard():
  print("You got 5 chances to guess the number\n")
  x=0
  while x<5:
    number=int(input("Guess a number between 1 and 100\n"))

    if number==comp_choice:
      print("You guessed it correct\n")
      return 0

    else:
      if number>comp_choice:
        print("high\n")
        x+=1
        continue
      else:
        print("low\n")
        x+=1
        continue
  print("you lost all chances\n")
  print(f"computer choice was {comp_choice}")
  return 0

# welcome message
print("Welcome to the game\n")

# Computer randomly choose a number between 0 and 100
comp_choice=random.randint(0,100)

# Ask the user to select a mode for the game. Easy or Hard
choice=input("Easy or Hard? \n").lower()

if choice=="easy":
  easy()
else:
  hard()  






