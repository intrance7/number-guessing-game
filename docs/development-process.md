# Development Process

This file explains how I created the Number Guessing Game step by step and how I used Python, VS Code, Git, and GitHub during the development.

---

## 1. Starting the Project
I first created a folder named `number-guessing-game` and opened it in VS Code.  
Then I created a file called `main.py`, where I wrote the Python code for the game.

---

## 2. Making the Basic Game
I started with a simple version:
- Generated a random number.
- Asked the user to guess it.
- Printed messages like "Too high" or "Too low".
- Showed "Correct!" when the user guessed the number.

This helped me build the main game logic.

---

## 3. Adding Difficulty Levels
After the basic version worked, I added 3 difficulty levels:
- Easy (1–50, unlimited attempts)
- Medium (1–100, 10 attempts)
- Hard (1–200, 7 attempts)

I used `if` and `elif` statements to set the number range and attempts based on the user's choice.

---

## 4. Input Validation
At first, the game crashed when someone entered letters instead of numbers.  
So I added:
- `try` and `except`  
- Checks for ou
