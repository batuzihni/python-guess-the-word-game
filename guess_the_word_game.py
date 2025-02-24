secret = 'python'
guesses = ''
turns = 6

print("Welcome to the 'Guess the Word' game!")
print(f'You have {turns} turns to guess the word.')

# main game loop
while turns > 0:
    missed = 0  # Variable to track missed letters

    # Show the current progress of the guessed word
    for char in secret:
        if char in guesses:
            print(char, end=" ")  # Show correct guessed letter
        else:
            print("_", end=" ")  # Show dash for missing letter
            missed += 1

    print()  # Move to the next line

    # If there are no missed letters, the game is won
    if missed == 0:
        print("Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter.")
        continue

    if guess in guesses:
        print("You already guessed that letter.")
        continue

    guesses += guess

    # Incorrect guess handling
    if guess not in secret:
        turns -= 1
        print(f"Wrong guess! You have {turns} turns left.")

    # Game over check
    if turns == 0:
        print(f"Game over! The word was: {secret}")
        break

    print("-------------------------")  # Separator between turns
