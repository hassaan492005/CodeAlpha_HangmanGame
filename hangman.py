import random

# 5 predefined words
words = ["python", "computer", "programming", "developer", "keyboard"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_wrong_guesses = 6
wrong_guesses = 0

# Display the hidden word
display_word = ["_"] * len(word)

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")
print()

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Incorrect guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("Enter a letter: ").lower().strip()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        print()
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        print()
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Correct guess!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        print("Incorrect guess!")

    print()

# Game result
if "_" not in display_word:
    print("================================")
    print("🎉 Congratulations! You won!")
    print("The word was:", word)
    print("================================")
else:
    print("================================")
    print("💀 Game Over!")
    print("The word was:", word)
    print("================================")