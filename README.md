 🎮 Hangman Game

A simple "text-based Hangman game built with Python". The player has to guess a randomly selected word one letter at a time. The game allows a maximum of "6 incorrect guesses" before the player loses.

This project was created as part of "CodeAlpha Task 1".

---

 📌 Project Overview

Hangman is a classic word-guessing game. In this version, the computer randomly selects one word from a predefined list of five words. The player then attempts to reveal the hidden word by guessing one letter at a time.

For every correct guess, the corresponding letter is revealed. For every incorrect guess, the number of remaining attempts decreases.

The game continues until:

* 🎉 The player correctly guesses the entire word, or
* 💀 The player reaches 6 incorrect guesses.

---

 ✨ Features

* 🎲 Random word selection
* 📝 Five predefined words
* 🔤 One-letter-at-a-time guessing
* ❤️ Maximum 6 incorrect guesses
* 🔎 Displays correctly guessed letters
* 📋 Keeps track of previously guessed letters
* 🚫 Prevents repeated guesses
* ⚠️ Validates user input
* 💻 Simple console-based interface
* 🚫 No external API required
* 🚫 No database required
* 🚫 No external word file required

---

 🛠️ Technologies Used

| Technology    | Purpose                                   |
| ------------- | ----------------------------------------- |
| Python        | Main programming language                 |
| Random module | Selects a random word                     |
| While Loop    | Controls the game loop                    |
| If-Else       | Handles game logic                        |
| Lists         | Stores words, guesses, and hidden letters |
| Strings       | Handles words and user input              |

---

 📂 Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangman.py
└── README.md
```

 `hangman.py`

Contains the complete Hangman game implementation, including:

* Word selection
* User input
* Guess validation
* Correct/incorrect guess handling
* Game loop
* Win/lose conditions

 `README.md`

Contains the project documentation, instructions, features, and information about the project.

---

   🎯 Predefined Words

The game uses five predefined words:

```text
python
computer
programming
developer
keyboard
```

The `random` module selects one of these words when the game starts.

Example:

```python
words = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard"
]

word = random.choice(words)
```

---

  ⚙️ How the Game Works

   1. Select a random word

The computer randomly selects one word from the predefined list.

```python
word = random.choice(words)
```

  2. Hide the word

The letters are initially displayed as underscores.

For example:

```text
python
```

becomes:

```text
_ _ _ _ _ _
```

   3. Ask the player for a letter

The player enters one letter:

```text
Enter a letter: p
```

   4. Check the guess

If the letter exists in the word, it is revealed.

Example:

```text
p _ _ _ _ _
```

If the letter does not exist, the incorrect guess counter increases.

   5. Continue the game

The game continues until the player either:

* Guesses all letters correctly, or
* Makes 6 incorrect guesses.

---

   🖥️ Example Gameplay

```text
================================
       HANGMAN GAME
================================
Guess the word one letter at a time.
You have 6 incorrect guesses.

Word: _ _ _ _ _ _
Guessed letters:
Incorrect guesses: 0 / 6

Enter a letter: p
Correct guess!

Word: p _ _ _ _ _
Guessed letters: p
Incorrect guesses: 0 / 6

Enter a letter: x
Incorrect guess!

Word: p _ _ _ _ _
Guessed letters: p x
Incorrect guesses: 1 / 6
```

   Winning Example

```text
================================
🎉 Congratulations! You won!
The word was: python
================================
```

   Losing Example

```text
================================
💀 Game Over!
The word was: developer
================================
```

---

  🚀 Installation
 
  Prerequisites

You only need:

* Python 3.x
* A terminal or command prompt
* A code editor such as VS Code

Check whether Python is installed:

```bash
python --version
```

Example:

```text
Python 3.10.0
```

---

  ▶️ How to Run

   Step 1: Clone the repository

```bash
git clone https://github.com/hassaan492005/CodeAlpha_HangmanGame.git
```

   Step 2: Open the project directory

```bash
cd CodeAlpha_HangmanGame
```

   Step 3: Run the game

```bash
python hangman.py
```

The Hangman game will start in your terminal.

---

   🧠 Key Python Concepts Demonstrated

This project demonstrates several fundamental Python programming concepts.

   Random Selection

```python
random.choice(words)
```

Used to randomly select a word.

   Lists

```python
words = ["python", "computer", "programming", "developer", "keyboard"]
```

Used to store the predefined words and guessed letters.

   While Loop

```python
while wrong_guesses < max_wrong_guesses and "_" in display_word:
```

Used to keep the game running until a win or loss occurs.

  If-Else Statements

```python
if guess in word:
    print("Correct guess!")
else:
    print("Incorrect guess!")
```

Used to determine whether the player's guess is correct.

  Strings

Strings are used to store and process:

* Words
* Letters
* User input
* Game messages

---

 🛡️ Input Validation

The game checks whether the user enters a valid single letter.

For example, invalid inputs such as:

```text
12
abc
@
```

are rejected.

The player is asked to enter one letter at a time.

The game also prevents the player from guessing the same letter repeatedly.

---

 📊 Game Rules

| Rule                  | Description          |
| --------------------- | -------------------- |
| Words                 | 5 predefined words   |
| Guess type            | One letter at a time |
| Maximum wrong guesses | 6                    |
| Word selection        | Random               |
| Interface             | Console              |
| Graphics              | None                 |
| Audio                 | None                 |
| External API          | Not required         |
| Database              | Not required         |

---

🎓 Learning Objectives

This project helps demonstrate the following programming skills:

* Python fundamentals
* Variables and data types
* Lists
* Strings
* Loops
* Conditional statements
* User input
* Randomization
* Basic game logic
* Input validation
* Problem-solving

---

 🔮 Future Improvements

The current project intentionally follows the simplified CodeAlpha requirements. However, it could be expanded in the future with:

* 🧩 Larger word dictionaries
* ❤️ Visual Hangman stages
* 🏆 Score system
* 📈 Difficulty levels
* ⏱️ Timer
* 💾 High-score storage
* 🎨 Graphical user interface
* 🌐 Web version
* 🔊 Sound effects
* 👥 Multiplayer mode

---

 📜 Task Information

"Task:" Task 1 – Hangman Game

"Program Type:" Console Application

"Language:" Python

"Project Level:" Beginner

"Purpose:" Practice fundamental Python programming concepts through a simple interactive game.

---

 👨‍💻 Author

"Hassaan Hussain"

GitHub:
[https://github.com/hassaan492005](https://github.com/hassaan492005)

---

 📄 License

This project is created for "educational and learning purposes" as part of a CodeAlpha project/task.

---

 ⭐ Acknowledgement

This project was developed to practice Python programming fundamentals, including:

```text
random
while loops
if-else
strings
lists
user input
```

If you find this project useful, feel free to ⭐ the repository!
