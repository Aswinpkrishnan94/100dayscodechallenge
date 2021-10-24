import random
import hangman_graphics_1
import words

# To print Hangman Logo
print(logo)

# To determine state of the game
game_end = False
lives = len(stages) - 1

# Randomly chose a word in the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Display dashes for the user to enter his guesses
display = []
for _ in range(word_length):
    display += "_"

# Let the user enter his guess until the number of letters.
# If correct letter is guessed, add to a list, else reduce the life by 1
while not game_end:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_end = True
            print("You lose.")
  
  # If all the dashes are filled, the user win the game.  
    if not "_" in display:
        game_end = True
        print("You win.")

    print(stages[lives])