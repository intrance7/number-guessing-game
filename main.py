# Hi there! I am Tanishq , i have made this number guessing game with multiple difficulty levels and smart hints to make it more engaging. Enjoy playing! roll number: 2501410009 i have used chatgpt for english grammer/print statements. and emojis from google.


import random


def play_game():
    print("===========================================")
    print("🎮 WELCOME TO THE ADVANCED NUMBER GUESSING GAME 🎮")
    print("👨‍💻 Developed by: Tanishq")
    print("🆔 Roll Number: 2501410009")
    print("===========================================\n")

    print("Choose a difficulty level:")
    print("1️⃣  Easy   (1-50) – Unlimited attempts")
    print("2️⃣  Medium (1-100) – 10 attempts")
    print("3️⃣  Hard   (1-200) – 7 attempts")

    while True:
        try:
            choice = int(input("Enter your choice (1-2-3): "))
            if choice in [1, 2, 3]:
                break
            else:
                print("Invalid choice! Please select 1, 2, or 3.")
        except:
            print("Please enter a number only.")

    if choice == 1:
        number = random.randint(1, 50)
        attempts_left = None
        max_range = 50
        print("\n🟢 EASY MODE selected!")
    elif choice == 2:
        number = random.randint(1, 100)
        attempts_left = 10
        max_range = 100
        print("\n🟡 MEDIUM MODE selected!")
    else:
        number = random.randint(1, 200)
        attempts_left = 7
        max_range = 200
        print("\n🔴 HARD MODE selected!")

    print(f"\nI have selected a number between 1 and {max_range}. Can you guess it?\n")

    attempts = 0

    while True:
        # Attempts limit for Medium/Hard
        if attempts_left is not None and attempts >= attempts_left:
            print("❌ You ran out of attempts!")
            print(f"💡 The correct number was: {number}")
            break

        try:
            guess = int(input("👉 Enter your guess: "))
        except:
            print("⚠ Please enter a valid number!")
            continue

        attempts += 1

        if guess < number:
            print("📉 Too low!")
        elif guess > number:
            print("📈 Too high!")
        else:
            print("\n🎉🎉 CONGRATULATIONS! 🎉🎉")
            print(f"👏 You guessed the number in {attempts} attempts!")
            break

        # Smart hints
        if abs(guess - number) <= 5:
            print("🔥 You're very close!")
        elif abs(guess - number) <= 10:
            print("✨ Close! Keep trying!")

        # Show attempts left
        if attempts_left is not None:
            print(f"🔁 Attempts left: {attempts_left - attempts}\n")

    print("\n===========================================")
    print("       🎯 GAME OVER – THANK YOU 🎯")
    print("===========================================\n")


# Replay Feature
while True:
    play_game()
    again = input("🔄 Do you want to play again? (y/n): ").lower()
    if again != "y":
        print("👋 Thanks for playing! Goodbye!")
        break
