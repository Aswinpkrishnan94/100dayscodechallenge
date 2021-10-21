# To include Random function
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# A List is created
game=[rock, paper, scissors]

# User is asked to enter his choice
user_choice=int(input("What type do you choose? type 0 for Rock type 1 for Paper type 2 for Scissors\n"))

# Check if entered value is beyond scope
if user_choice<0 or user_choice>3 :
    print("Invalid option is selected\n")
else:
    print(f"You chose {game[user_choice]}\n")      # User's choice

# Computer randomly choose an option
computer_choice=random.randint(0,2)

print(f"Computer chose {game[computer_choice]}\n")   # computer's choice

if user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
  
# When both choose same option. Game is a draw
elif computer_choice == user_choice:
  print("It's a draw")
