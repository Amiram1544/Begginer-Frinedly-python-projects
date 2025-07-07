import random

# List of words
words = ["apple", "bananna", "kiwi", "coconut", "avocado", "mango"]

# Hangman stages
hangman = {
    0: ("   ",
        "   ",
        "   "),
    1: (" O ",
        "   ",
        "   "),
    2: (" O ",
        " | ",
        "   "),
    3: (" O ",
        "/| ",
        "    "),
    4: (" O ",
        "/|\\ ",
        "   "),
    5: (" O ",
        "/|\\ ",
        "/  "),
    6: (" O ",
        "/|\\ ",
        "/ \\ "),
}

# Function to display the hangman
def display_hangman(wrong_answers):
    for i in hangman[wrong_answers]:
        print(i)

# Function to display the hint
def display_hint(hint):
    print(" ".join(hint))

# Main function
def main():
    answer = random.choice(words)
    hint = "_" * len(answer)
    wrong_answers = 0
    guessed = set()
    is_running = True

    while is_running:
        display_hangman(wrong_answers)
        display_hint(hint)

        # Get user input
        guess = input("Enter your guess: ").lower()

        # Check if input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("!..INVALID INPUT..! Please enter a single letter.")
            continue

        # Check if letter has already been guessed
        if guess in guessed:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        # Add the guess to the guessed set
        guessed.add(guess)

        # Check if the guess is correct
        if guess in answer:
            new_hint = []

            # Update the hint
            for i in range(len(answer)):
                if answer[i] == guess:
                    new_hint.append(guess)
                else:
                    new_hint.append(hint[i])

            hint = "".join(new_hint)

        else:
            # Increment wrong answers if the guess is incorrect
            wrong_answers += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        # Check win condition
        if "_" not in hint:
            print(f"CONGRATULATIONS! You guessed the word: {answer}")
            is_running = False

        # Check lose condition
        elif wrong_answers == 6:
            display_hangman(wrong_answers)
            print(f"GAME OVER! The word was: {answer}")
            is_running = False

if __name__ == "__main__":
    main()



