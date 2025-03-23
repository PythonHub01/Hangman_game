# Hangman Game

A simple command-line Hangman game built with Python. Guess the secret word letter by letter before you run out of attempts!

## 🎯 Game Overview
- **Objective**: Guess a 5-letter secret word by suggesting letters.
- **Attempts**: You have 8 attempts to guess the word correctly.
- **Words**: The game randomly selects a word from a predefined list of 5-letter words.

### 📝 Current Word List
- `magic` (Inspired by *Harry Potter*)
- `rings` (Inspired by *Lord of the Rings*)
- `spide` (Inspired by *Spiderman*)
- `batma` (Inspired by *Batman*)

## 🕹️ How to Play
1. Run the game.
2. You'll see a sequence of underscores (`_`) representing the 5 letters of the secret word.
3. Enter a letter (`a-z`) when prompted.
4. If the letter is in the word, it will appear in the correct position(s).
5. If the letter is not in the word, you lose one attempt.
6. Keep guessing until you either:
   - Guess the word correctly (**You win!** 🎉).
   - Run out of attempts (**You lose!** ❌).

## ✨ Features
✅ Displays the number of remaining attempts after each guess.  
✅ Prevents duplicate guesses and invalid inputs (e.g., numbers or multiple characters).  
✅ Provides feedback on correct and incorrect guesses.  

## 🛠️ Requirements
- **Python**: Version 3.x (No additional libraries required).

## 🚀 How to Run
1. Clone or download this repository.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the script:
   ```bash
   python hangman.py
   ```

## 🎮 Example Gameplay
```
********************
Welcome To Hangman Game
********************
_ _ _ _ _
Attempts remaining: 8
Please select a letter (a-z): m
You guessed correctly!
m _ _ _ _
Attempts remaining: 8
Please select a letter (a-z): x
Sorry, you guessed wrong!
m _ _ _ _
Attempts remaining: 7
```

## ⚙️ Customization
- **To change the word list**, edit the `words_list` variable in the code with your own 5-letter words.
- **To adjust the number of attempts**, modify the condition `wrong_guesses != 8` and update the attempts display logic.

## 🔮 Future Improvements
- Add a graphical interface.
- Expand the word list with categories or a dictionary file.
- Include a scoring system.

## 📜 License
This project is **open-source** and free to use or modify.

Enjoy playing **Hangman**! 🎉

